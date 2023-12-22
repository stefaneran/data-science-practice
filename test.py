from matrix import Matrix
from vector import Vector
from stats import Statistics
from graph import Graph
import numpy as np

matrixLib = Matrix()
vectorLib = Vector()
statsLib = Statistics()
graphLib = Graph()

data = [1.200, 0.800, 1.100]
mean = statsLib.getHarmonicMean(data)
print(mean)