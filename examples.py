from matrix import Matrix
from vector import Vector
from stats import Statistics
from graph import Graph
import numpy as np

matrixLib = Matrix()
vectorLib = Vector()
statsLib = Statistics()
graphLib = Graph()


# Show binomial distribution of 5 dice rolls
binomial = statsLib.getBinomialDistribution((1/6), 5)
graphLib.show([{
  "type": "line",
  "lines": [binomial]
}])

# Poisson distribution where mean is 3
poissonDist = statsLib.getPoissonDistribution(3)
graphLib.show([{
  "type": "bar",
  "bars": poissonDist
}], False)