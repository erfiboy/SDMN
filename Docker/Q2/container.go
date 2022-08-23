package main

import (
	"io/ioutil"
	"log"
	"math/rand"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"syscall"
	"time"
)

// go run main.go run <cmd> <args>
func main() {
	switch os.Args[1] {
	case "run":
		run()
	case "child":
		child()
	default:
		panic("usage: go run container.go run <hostname> <memory>")
	}
}

func run() {
	cmd := exec.Command("/proc/self/exe", append([]string{"child"}, os.Args[2:]...)...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.SysProcAttr = &syscall.SysProcAttr{
		Cloneflags: syscall.CLONE_NEWUTS | syscall.CLONE_NEWPID | syscall.CLONE_NEWNS | syscall.CLONE_NEWNET,
	}
	cmd.Run()
}

func create_separate_filesystem(container_name string) {
	if err := os.Mkdir(container_name, os.ModePerm); err != nil {
		log.Fatal(err)
	} else {

		cmd := exec.Command("/bin/sh", "-c", "sudo tar -xvf ubuntu.tar -C "+container_name)
		cmd.Run()
		if err != nil {
			log.Fatal(err)
		}
	}
}

func child() {
	source := rand.NewSource(time.Now().UnixNano())
	new_random := rand.New(source)
	uid := strconv.Itoa(new_random.Intn(100000))
	container_name := "/container_" + uid

	cg(uid)

	if len(os.Args) == 4 {
		limit_memory_usage(uid)
	}

	create_separate_filesystem(container_name)

	cmd := exec.Command("bash")
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	syscall.Sethostname([]byte(os.Args[2]))
	syscall.Chroot(container_name)
	os.Chdir("/")
	syscall.Mount("proc", "proc", "proc", 0, "")

	cmd.Run()

	syscall.Unmount("proc", 0)
}

func cg(uid string) {
	cgroups := "/sys/fs/cgroup/"
	pids := filepath.Join(cgroups, "pids")
	os.Mkdir(filepath.Join(pids, uid), 0755)
	must(ioutil.WriteFile(filepath.Join(pids, uid+"/pids.max"), []byte("20"), 0700))
	must(ioutil.WriteFile(filepath.Join(pids, uid+"/notify_on_release"), []byte("1"), 0700))
	must(ioutil.WriteFile(filepath.Join(pids, uid+"/cgroup.procs"), []byte(strconv.Itoa(os.Getpid())), 0700))
}

func limit_memory_usage(uid string) {
	cgroups := "/sys/fs/cgroup/"
	memory := filepath.Join(cgroups, "memory")
	os.Mkdir(filepath.Join(memory, uid), 0755)

	memory_size, _ := strconv.Atoi(os.Args[3])

	must(ioutil.WriteFile(filepath.Join(memory, uid+"/memory.limit_in_bytes"), []byte(strconv.Itoa(memory_size*1000)), 0700))
	must(ioutil.WriteFile(filepath.Join(memory, uid+"/tasks"), []byte(strconv.Itoa(os.Getpid())), 0700))
	must(ioutil.WriteFile(filepath.Join(memory, uid+"/cgroup.procs"), []byte(strconv.Itoa(os.Getpid())), 0700))
}

func must(err error) {
	if err != nil {
		panic(err)
	}
}
