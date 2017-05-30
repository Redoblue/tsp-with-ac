import math
import random

import numpy as np

from ant import Ant


class Colony:
    def __init__(self, graph, n_ant, q):
        self.alpha = 2
        self.beta = 2
        self.q = q
        self.graph = graph
        self.n_ant = n_ant
        self.ants = [Ant() for _ in range(n_ant)]

    def _possibility(self, i, j):
        tau = self.graph.info[i, j]
        eta = 1.0 / self.graph.map[i, j]
        p = math.pow(tau, self.alpha) * math.pow(eta, self.beta)
        return p

    @staticmethod
    def _roulette(p_list):
        p_cdf = np.cumsum(p_list)
        rand = random.random()
        for i in range(len(p_cdf)):
            if p_cdf[i] >= rand:
                return i

    def assign(self):
        for i in range(self.n_ant):
            self.ants[i].reset()
            self.ants[i].pos = i
            self.ants[i].tabu.append(i)

    def step(self):
        for ant in self.ants:
            available = [j for j in range(self.graph.n_city) if j not in ant.tabu]
            p_list = []
            p_sum = 0.0
            for k in available:
                p = self._possibility(ant.pos, k)
                p_list.append(p)
                p_sum += p
            for k in range(len(p_list)):
                p_list[k] /= p_sum

            most_possible_city = available[self._roulette(p_list)]

            ant.dist += self.graph.map[ant.pos, most_possible_city]
            ant.pos = most_possible_city
            ant.tabu.append(most_possible_city)

    def tour(self, eva_rate):
        n_city = self.graph.n_city
        for _ in range(n_city - 1):
            self.step()

        # add the last one
        for ant in self.ants:
            ant.dist += self.graph.map[ant.tabu[0], ant.tabu[8]]

        # update info
        dinfo = np.zeros((n_city, n_city), dtype=np.float16)
        for ant in self.ants:
            dtau = self.q / ant.dist
            for i in range(n_city - 2):
                dinfo[ant.tabu[i], ant.tabu[i+1]] += dtau
                dinfo[ant.tabu[i+1], ant.tabu[i]] += dtau
        self.graph.info = self.graph.info * eva_rate + dinfo

        min_ant = min(self.ants, key=lambda a: a.dist)

        return min_ant.dist, min_ant.tabu