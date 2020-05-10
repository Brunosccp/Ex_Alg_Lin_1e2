from mathHelper import MathHelper
import copy

class LinearSystem:

    dimension: int

    def solveByCramer(self, matrix, resultVector):
        self.dimension = MathHelper.getMatrixDimension(matrix)
        matrixDeterminant = self.determinant(matrix)

        coFactorResult = []
        for i in range(len(matrix)):
            auxMatrix = self.rowReplace(matrix, i, resultVector)
            auxMatrixDet = self.determinant(auxMatrix)
            coFactorResult.append(auxMatrixDet)

        result = []
        for dFactor in coFactorResult:
            factor = dFactor/matrixDeterminant
            result.append(factor)

        return result

    def rowReplace(self, matrix, row, vector):
        mutableMatrix = copy.deepcopy(matrix)

        for i in range(self.dimension):
            mutableMatrix[i][row] = vector[i]

        return mutableMatrix
            

    def determinant(self, matrix): 
        aux = [0] * self.dimension 
        total = 1 
        determinant = 1
        mutableMatrix = copy.deepcopy(matrix)
    
        for i in range(0,self.dimension): 
            index=i
    
            while(mutableMatrix[index][i] == 0 and index < self.dimension): 
                index+=1
        
                if(index == self.dimension):
                    return 0
    
            if(index != i): 
                for j in range(0,self.dimension): 
                    mutableMatrix[index][j],mutableMatrix[i][j] = mutableMatrix[i][j],mutableMatrix[index][j] 
                determinant = determinant*int(pow(-1,index-i)) 
        
            for j in range(0,self.dimension): 
                aux[j] = mutableMatrix[i][j] 
            
            for j in range(i+1,self.dimension): 
                value1 = aux[i] 
                value2 = mutableMatrix[j][i]
    
                for k in range(0,self.dimension): 
                    mutableMatrix[j][k] = (value1*mutableMatrix[j][k]) - (value2*aux[k]) 
                total = total * value1
    
        for i in range(0,self.dimension): 
            determinant = determinant*mutableMatrix[i][i] 
    
        determinant = int(determinant/total)

        return determinant