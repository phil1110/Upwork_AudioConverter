import base64
import os


class AudioConverter:
    def __init__(self, filepath, targetpath):
        self.filepath = filepath
        self.targetpath = targetpath

    def __readfile(self):
        try:
            if os.path.exists(self.filepath):
                encodedString = open(self.filepath).read()

                if encodedString.__contains__("data:audio/aac;base64,"):
                    encodedString = encodedString.replace("data:audio/aac;base64,", "")

                return encodedString

            else:
                raise Exception("File does not exist")
        except Exception as error:
            return error

    def __writefile(self, decodedString):
        try:
            targetFile = open(self.targetpath, "wb")
            targetFile.write(decodedString)

            return 0

        except Exception as error:
            return error

    def Convert(self):
        try:
            encodedString = self.__readfile()

            decodedString = base64.b64decode(encodedString)

            result = self.__writefile(decodedString)

            if result == 0:
                print("Program executed successfully!")
                return True

            else:
                raise Exception(result)

        except Exception as error:
            print("ERROR! Details: " + error)

            if os.path.exists(self.targetpath):
                os.remove(self.targetpath)

            return False
