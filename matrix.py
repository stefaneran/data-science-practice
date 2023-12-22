class Matrix:

  def checkIfValid(self, matrix):
    columns = {}
    for row in matrix:
      numOfColumns = len(row)
      if not numOfColumns in columns:
        columns[numOfColumns] = 1
      else:
        columns[numOfColumns] += 1
    return len(columns) == 1
  
  
  def checkIfCanPerformAddition(self, leftMatrix, rightMatrix):
    leftDimension = self.getDimensions(leftMatrix)
    rightDimension = self.getDimensions(rightMatrix)
    isRowEqual = leftDimension[0] == rightDimension[0]
    isColumnEqual = leftDimension[1] == rightDimension[1]
    return isRowEqual and isColumnEqual
  
  
  def checkIfCanMultiply(self, leftMatrix, rightMatrix):
    leftDimension = self.getDimensions(leftMatrix)
    rightDimension = self.getDimensions(rightMatrix)
    return leftDimension[1] == rightDimension[0]
  

  def getDimensions(self, matrix):
    isValid = self.checkIfValid(matrix)
    if not isValid:
      return "Error: Invalid matrix (getDimensions)"
    numOfRows = len(matrix)
    numOfColumns = len(matrix[0])
    return [numOfRows, numOfColumns]
  

  def addition(self, leftMatrix, rightMatrix, operation):
    canAddOrSub = self.checkIfCanPerformAddition(leftMatrix, rightMatrix)
    if not canAddOrSub:
      return "Error: Cannot add or subtract"
    numOfRows = len(leftMatrix)
    resultMatrix = []
    for rowIdx in range(numOfRows):
      for colIdx in range(numOfRows):
        leftValue = leftMatrix[rowIdx][colIdx]
        rightValue = operation * rightMatrix[rowIdx][colIdx]
        if len(resultMatrix) == rowIdx:
          resultMatrix.append([])
        resultMatrix[rowIdx].append(leftValue + rightValue)
    return resultMatrix
  

  def multiplication(self, leftMatrix, rightMatrix):
    canMultiply = self.checkIfCanMultiply(leftMatrix, rightMatrix)
    if not canMultiply:
      return "Error: Cannot multiply"
    numOfLeftRows = len(leftMatrix)
    numOfRightRow = len(rightMatrix)
    numOfRightColumns = len(rightMatrix[0])
    resultMatrix = []
    # iterate over rows (left)
    for leftRowIdx in range(numOfLeftRows):
      # iterate colNum (right)
      for rightColIdx in range(numOfRightColumns):
        # iterate rowNum (right)
        sum = 0
        for rightRowIdx in range(numOfRightRow):
          leftValue = leftMatrix[leftRowIdx][rightRowIdx]
          rightValue = rightMatrix[rightRowIdx][rightColIdx]
          sum += leftValue * rightValue
        if len(resultMatrix) == leftRowIdx:
          resultMatrix.append([])
        resultMatrix[leftRowIdx].append(sum)
    return resultMatrix