import matplotlib.pyplot as plt


class Painter:
    def __init__(self, graph):
        self.graph = graph
        self.fig = plt.figure(figsize=(11, 11))
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim([85, 130])
        self.ax.set_ylim([15, 50])
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.grid(False)

    def draw(self):
        for i in range(self.graph.n_city):
            for j in range(i, self.graph.n_city):
                x = (self.graph.cities[0, i], self.graph.cities[0, j])
                y = (self.graph.cities[1, i], self.graph.cities[1, j])
                lw = self.graph.info[i, j] * 2.0
                self.ax.plot(x, y, 'ko-', linewidth=lw)
        plt.pause(0.001)

    def draw_best(self, best_road):
        n_city = self.graph.n_city

        plt.cla()
        plt.title("Travelling Salesman Problem")
        for i in range(n_city):
            h = best_road[i]
            t = best_road[(i+1) % n_city]
            x = (self.graph.cities[0, h], self.graph.cities[0, t])
            y = (self.graph.cities[1, h], self.graph.cities[1, t])
            self.ax.plot(x, y, 'ko-', linewidth=2.0)
        plt.pause(0.001)

    @staticmethod
    def show():
        plt.show()
