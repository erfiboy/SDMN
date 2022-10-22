# SDMN Course 2022

## LTE Implementation in Atoll

## Due date: 5 Mordad 1401

## ______________________________________________________

## Part 1 : LTE Scenario (10 Points)

In this part we are going to define an LTE scenario. Necessary information is given below.

Import “ir_Tehran_3D” map and place your sites in a hexagonal topology around (537729,
3956981) point as center. Note that a hexagonal grid includes one site at center and 6 other sites
in hexagon corners.

Inter-site distance = 400m

Each site includes 3 sectors with azimuth 0, 120, 240

Initial mechanical downtilts = 0

Antenna height = 30m

Antenna type: 65deg 18dBi 4Tilt 2100MHz

Initial max power of each cell = 43dBm

Cells frequency band: E-UTRA Band 1 - 1 0MHz

Now you have to draw a computation zone to work on. The coordinates for you computation zone:

( 536912 , 3956308 ), ( 536912 , 3957592 ), ( 538646 , 3957592 ), ( 538646 , 3956308 )

Deliverables: screenshot of your computation zone and the sites inside it.

## Part 2: Working with predictions ( 20 Points)

Run 2 predictions. One for signal level and one for carrier to noise and interference.

Set the resolution of predictions on 1m. provide a screenshot for each prediction and answer the
following questions.

1. As you can see, with our initial setting some areas in computation zone suffer from poor signal
level. Discuss the reasons briefly.
2. In C / (N +I) prediction, the central areas seem to have poor condition. What do you think is the
reason of this situation?


3. Imagine we increase max power of all cells from 43 dBm to 50dBm. How do you think this
affects our network’s signal level and interference condition? (No simulation needed)

### Part 3 : Frequency Planning ( 20 Points)

Allocate a channel number to each cell with a reuse distance of 500m using Automatic Frequency
Planning (AFP) module in Atoll.

1. What does the reuse distance parameter in AFP do?
2. How much bandwidth and how many resource blocks does each cell have after frequency
planning?
3. Imagine a user in our network. What do you think utilizing a resource block by this specific user
depends on? Do all users throughout the network utilize a resource block equally? Why?

Now run a new prediction for carrier to noise and interference.

4. Provide a screenshot and compare this prediction to the one obtained in Part2. Discuss the
difference and the reason.

Note that from now on we use the allocated channels for the following parts.

### Part 4 : Automatic Cell Planning ( 25 + 5 Points)

In this part we are going to optimize the network performance using ACP module in Atoll.

Define an ACP setup with the following settings and run it. Then provide a screenshot of ACP
Objective Graph and optimization Statistics Report. Any setting that is not mentioned below
remains unchanged with default value.

Objectives for optimization: RSRP & CINR with equal weights.

Resolution: 5m.

Iterations: recommended value by Atoll.

Antenna reconfigurations: Azimuth (default variation and step)

LTE cells reconfigurations: Max Power (min, max) = (30, 50)

1. One of the most important fields in cellular networks optimization is Coverage and Capacity
Optimization (CCO). How do you think RSRP & CINR objectives can improve the network’s
coverage and capacity condition? (Talk about the relation between these Key Performance
Indicators (KPIs) and coverage and capacity technically.)
2. Run new predictions for signal level and carrier to noise and interference after committing the
changes that ACP suggested. Provide screenshots and compare the results of signal level to Part
and C / (N + I) to Part3. Discuss the results.
3. As you can see in ACP module, there is a section for Load Balancing (LB). explain what does
LB do and how does it affect the network performance. (No simulation needed)


4. Suppose that you are assigned to balance the load throughout a network in reality. Do you think
considering LB as the only objective improves network performance? Discuss your answer.
5. Imagine you are going to optimize a network in real world. Which parameters do you choose to
reconfigure? (Hint: consider the feasibility)

6(Bonus). Feel free to use any reconfiguration in ACP module to improve the network’s RSRP &
CINR condition as much as possible. Discuss the reconfigurations that you chose and their effects
on the network. Provide Statistics Report screenshot. (No other screenshot needed)

### Part 5 : A simple LTE network example ( 25 + 5 Points)

In this problem we are going to inspect a small part of a large LTE network. Imagine we have one
cell with 10Mhz bandwidth. 90 percent of the cell resources are occupied. 3 users are trying to
connect to the network. User x CQI index is 3 and it demands 500Kbps of throughput, User y CQI
index is 15 and it demands 2 .5Mbps of throughput and user z CQI index is 11 and it demands 1.
Mbps of throughput. Cell’s scheduling policy is “best CQI”. Assume that one resource block only
can be assigned to one user. (No simulation is needed for Part 6 )

(Hint: “best CQI” scheduling policy sorts the priorities of resource allocation based on CQI index.
In other words, best is first!)

1. Calculate each user’s throughput.
2. What is the final value of the cell load?
3. Is the cell saturated after resource allocation? If yes, which optimization technique from last
parts do you suggest to implement on this network to mitigate the problems?

## 4. What problems do you think a saturated cell will cause in a network? Explain briefly.

5. Explain the relation between SINR and Cell Load. (Hint: how the SINR values of users affect
Cell Loads in network)

6 (Bonus). What scheduling policy do you suggest to make the resource allocation for 3 users fair?



