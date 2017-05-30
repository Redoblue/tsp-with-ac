import numpy as np


class Graph(object):
    def __init__(self):
        self.n_city = 34
        self.cities = np.zeros([2, self.n_city], dtype=np.float16)
        self.map = np.zeros([self.n_city, self.n_city], dtype=np.float16)
        self.info = np.ones([self.n_city, self.n_city], dtype=np.float16)

        self.generate()

    def _dist(self, ci1, ci2):
        dx = self.cities[0, ci1] - self.cities[0, ci2]
        dy = self.cities[1, ci1] - self.cities[1, ci2]
        return np.linalg.norm((dx, dy), 2)

    def generate(self):
        with open('china.csv', 'r') as f:
            k = 0
            for line in f:
                ll = line.strip().split(';')
                self.cities[0, k] = float(ll[1])
                self.cities[1, k] = float(ll[2])
                k += 1

        for i in range(self.n_city):
            for j in range(i+1, self.n_city):
                d = self._dist(i, j)
                self.map[i, j] = d
                self.map[j, i] = d
