class Vector:

  def add(self, leftVector, rightVector):
    return [
      leftVector[0] + rightVector[0],
      leftVector[1] + rightVector[1]
    ]
  
  def subtract(self, leftVector, rightVector):
    return [
      leftVector[0] - rightVector[0],
      leftVector[1] - rightVector[1]
    ]