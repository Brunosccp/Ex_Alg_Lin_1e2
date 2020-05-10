from fileManager import FileManager

class MatrixManager:

    def getMatrixFromFile(self, name):
        fileManager = FileManager()
        matrixString = fileManager.getVectorTxt(name)

        matrix = self.__createMatrixArray(matrixString)

        return matrix

    def getVectorFromFile(self, name):
        fileManager = FileManager()
        vectorString = fileManager.getVectorTxt(name)

        vector = self.__createVectorArray(vectorString)

        return vector

    def __createMatrixArray(self, matrixString):
        dimension = self.__getMatrixDimension(matrixString)

        readableString = matrixString.replace("\n", ",")
        matrixString = readableString.split(",")

        matrixValues = []
        for string in matrixString:
            value = float(string)
            matrixValues.append(value)

        matrix = []
        for i in range(0,dimension):
            subVector = []
            for j in range(0,dimension):
                value = matrixValues[i*dimension + j]
                subVector.append(value)
            matrix.append(subVector)
        
        return matrix

    def __createVectorArray(self, vectorString):
        vectorString = vectorString.split(",")

        vector = []
        for value in vectorString:
            vector.append(float(value))

        return vector

    def __getMatrixDimension(self, vectorString):
        vectorDimension = vectorString.count("\n") + 1
        return vectorDimension