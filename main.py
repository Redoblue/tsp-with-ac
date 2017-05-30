from optparse import OptionParser

from colony import *
from graph import *
from painter import *

parser = OptionParser()
parser.add_option("-p", "--pheromone", action="store", type="float", dest="pheromone",
                  default=5.0, help="amount of pheromone for per ant in one tour")
parser.add_option("-n", "--nepoch", action="store", type="int", dest="nepoch",
                  default=100, help="number of total epoches")
parser.add_option("-e", "--evarate", action="store", type="float", dest="evarate",
                  default=0.8, help="rate of evaporation")
(options, args) = parser.parse_args()

# options
N_ANT = 34
Q = options.pheromone
NP = options.nepoch
EVA_RATE = options.evarate

# global variables
best_dist = 100000.0
n = 0
best_road = []
dist_loss = []

# instances
graph = Graph()
painter = Painter(graph)
colony = Colony(graph, N_ANT, Q)

# main loop
while n < NP:
    colony.assign()
    tmp_dist, tmp_road = colony.tour(EVA_RATE)

    if tmp_dist < best_dist:
        dist_loss.append(best_dist - tmp_dist)
        best_dist = tmp_dist
        best_road = tmp_road

    # print info
    print("{} : {}".format(n, best_dist))

    # draw the best road
    painter.draw_best(best_road)

    n += 1
painter.show()
