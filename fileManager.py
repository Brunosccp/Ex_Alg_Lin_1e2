from os import path

class FileManager:

    def getVectorTxt(self, fileName):
        file = open(fileName, "r")
        fileContent = file.read()

        return fileContent