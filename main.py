from vectorManager import MatrixManager
from linearTransformation import Rotation
from linearSystem import LinearSystem

matrixManager = MatrixManager()
matrix = matrixManager.getMatrixFromFile("Example.txt")
matrix2 = matrixManager.getMatrixFromFile("Example2.txt")
vectorResult = matrixManager.getVectorFromFile("ExampleVectorResult.txt")

vectorRotation = Rotation()
rotatedMatrix = vectorRotation.rotate(matrix, 45)

print("Exemplo de matrix 2x2 rotacionada:")
print(matrix)
print("rotacionando 45 graus")
print(rotatedMatrix)

linearSystem = LinearSystem()
cramerResult = linearSystem.solveByCramer(matrix2, vectorResult)

print("\nExemplo de resolução de sistema linear com teorema de cramer:")
print(matrix2)
print(vectorResult)
print("Vetor com resultados:")
print(cramerResult)