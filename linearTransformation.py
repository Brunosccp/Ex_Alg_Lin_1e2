import math
from mathHelper import MathHelper
import numpy as np

class Rotation:

    rotateMatrix = []
    radians: float

    def rotate(self, matrix, degrees):
        dimension = MathHelper.getMatrixDimension(matrix)
        self.radians = math.radians(degrees)
        self.__setRotateMatrix(matrix, dimension)

        rotatedMatrix = self.__getRotatedMatrix(matrix)

        readableMatrix = self.__getReadableMatrix(rotatedMatrix)

        return readableMatrix

    def __setRotateMatrix(self, matrix, dimension):

        if dimension == 2:
            self.rotateMatrix = [
                [math.cos(self.radians), - math.sin(self.radians)],
                [math.sin(self.radians), math.cos(self.radians) ]
            ]
        else:
            print("ERROR: Rotate matrix just implemented for 2 dimensions")

    def __getRotatedMatrix(self, matrix):
        npMatrix = np.array(matrix)
        npRotateMatrix = np.array(self.rotateMatrix)

        npResult = np.matmul(npMatrix, npRotateMatrix)
        result = npResult.tolist()

        return result

    def __getReadableMatrix(self, matrix):
        mutableMatrix = matrix

        for i in range(0, len(mutableMatrix)):
            for j in range(0, len(mutableMatrix[i])):
                mutableMatrix[i][j] = round(mutableMatrix[i][j], 2)

        return mutableMatrix