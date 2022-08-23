from flask import Flask, request

app = Flask(__name__)


class response_format:
    def __init__(self) -> None:
        self.response = {"status": "OK"}

    def set(self, message):
        self.response["status"] = message

    def get(self):
        return self.response


response = response_format()


@app.route("/api/v1/status", methods=["GET", "POST"])
def status():
    if request.method == "POST":
        response.set(request.get_json()["status"])
        return request.get_json(), 201

    elif request.method == "GET":
        return response.get(), 200


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000)
