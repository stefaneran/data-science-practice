import math

class Statistics:

  def getArithmeticMean(self, data):
    sum = 0
    length = len(data)
    for x in data:
      sum += x
    return sum / length
  
  def getGeometricMean(self, data):
    product = data[0]
    length = len(data)
    for i in range(length):
      if (i == 0):
        continue
      product *= data[i]
    return math.pow(product, (1 / length))
  
  def getHarmonicMean(self, data):
    denomSum = 0
    length = len(data)
    for x in data:
      denomSum += 1 / x 
    return length / denomSum
  
  def getMedian(self, data):
    data.sort()
    length = len(data)
    if length % 2 == 0:
      aIndex = round((length / 2) - 1)
      bIndex = round(length / 2)
      a = data[aIndex]
      b = data[bIndex]
      return (a + b) / 2
    else:
      return data[math.floor(length / 2)]
    
  def getMode(self, data):
    collection = {}
    for x in data:
      if not x in collection:
        collection[x] = 1
      else: 
        collection[x] += 1
    return [x for x, y in collection.items() if y == max(collection.values())]

  def getVariance(self, data):
    mean = self.mean(data)
    length = len(data)
    sum = 0
    for x in data:
      sum += (x - mean) ** 2
    return sum / length
  
  def getStandardDeviation(self, data):
    variance = self.getVariance(data)
    return math.sqrt(variance)
  
  def getExpectedValue(self, probability, numOfTries):
    binomialDist = self.getBinomialDistribution(probability, numOfTries)
    sum = 0
    for numOfSuccess in range(numOfTries + 1):
      sum += numOfSuccess * binomialDist["y"][numOfSuccess]
    print(sum)
    return sum
  
  def getBinomialDistribution(self, probability, numOfTries):
    distribution = []
    for numOfSuccess in range(numOfTries + 1):
      coeficient = (math.factorial(numOfTries) / (math.factorial(numOfSuccess) * math.factorial(numOfTries - numOfSuccess)))
      successProbability = math.pow(probability, numOfSuccess)
      failureProbability = math.pow((1 - probability), numOfTries - numOfSuccess)
      experimentProbability = coeficient * successProbability * failureProbability
      distribution.append(experimentProbability)
    return {
      "x": range(0, numOfTries + 1),
      "y": distribution
    }
  
  def getPoissonDistribution(self, poisson):
    distribution = []
    for numOfSuccess in range(poisson * 2):
      successProbability = (math.pow(poisson, numOfSuccess) * math.pow(math.e, (-1 * poisson))) / math.factorial(numOfSuccess)
      distribution.append(successProbability)
    return {
      "x": range(0, poisson * 2),
      "y": distribution
    }
    

    
  
  
