import matplotlib.pyplot as plt
import numpy as np

class Graph:

  def __init__(self):
    fig, ax = plt.subplots()
    self.fig = fig
    self.ax = ax

  def plotLines(self, lines):
    for line in lines:
      self.ax.plot(line["x"], line["y"])

  def plotBars(self, bars):
    self.ax.bar(bars["x"], bars["y"], 1, edgecolor="white", linewidth=0.5)

  def plotVectors(self, vectorsData):
    originArray = [[], []]
    for i in range(len(vectorsData)):
      originArray[0].append(0)
      originArray[1].append(0)
    origin = np.array(originArray)
    vectors = np.array(vectorsData)
    self.ax.quiver(*origin, vectors[:,0], vectors[:,1], angles='xy', scale_units='xy', scale=1)

  def show(self, graphs, grid):
    for graph in graphs:
      if graph["type"] == "line":
        self.plotLines(graph["lines"])
      if (graph["type"] == "bar"):
        self.plotBars(graph["bars"])
      if graph["type"] == "vector":
        self.plotVectors(graph["vectors"])
    if grid:
      plt.grid()
    plt.show()

