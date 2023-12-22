from matrix import Matrix
from vector import Vector
from stats import Statistics
from graph import Graph
import numpy as np

matrixLib = Matrix()
vectorLib = Vector()
statsLib = Statistics()
graphLib = Graph()

dataX = [30, 35, 40, 25, 35]
dataY = [5, 8, 8, 4, 5]
covariance = statsLib.getCovariance(dataX, dataY)
correlation = statsLib.getCorrelation(dataX, dataY)
print("Covariance:", covariance, "\nCorrelation:", correlation)