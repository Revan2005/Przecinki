# -*- coding: utf-8 -*-
__author__ = 'Koralgoll'

import os
import codecs
from xml.etree.ElementTree import ElementTree


class Parser():
    def __init__(self):
        pass

    def getLexFromXML(self, fileDirPath):
        # If file or directory does not exists
        if os.path.exists(fileDirPath) == False:
            return ""

        # Declare lexycon string as UTF-8
        lexStr = u""
        tree = ElementTree()
        # List of file names in directory
        fileList = []

        # Get file path correct for current OS
        fileDirPath = os.path.normpath(fileDirPath)

        # If path leads to directory
        if os.path.isfile(fileDirPath) == False:
            # If directory is empty
            if os.listdir(fileDirPath) == []:
                return ""

            # Get all .xml files
            for fileName in os.listdir(fileDirPath):
                if fileName.endswith(".xml"):
                    fileList.append(fileName)
        # If path leads to actual file
        else:
            if fileDirPath.endswith(".xml"):
                fileList.append(os.path.basename(fileDirPath))
                fileDirPath = os.path.dirname(fileDirPath)

        print("Collecting lexicons...")
        for fileName in fileList:
            tree.parse(os.path.join(fileDirPath, fileName))
            xmlRoot = tree.getroot()

            # For each chunk
            for chunk in xmlRoot.findall("chunk"):
                # For each sentence
                for sentence in chunk.findall("sentence"):
                    # For each token
                    for token in sentence.findall("tok"):
                        # For each lexycon
                        for lex in token.findall("lex"):
                            # If 'disamb' exists and equals 'true'
                            if ("disamb" in lex.attrib) and (lex.attrib["disamb"] == "1"):
                                # If 'interp' exists
                                if lex.find("ctag").text == "interp":
                                    # If lexycon contains comma
                                    if lex.find("base").text == ",":
                                        lexStr += " comma_after "
                                        break
                                    else:
                                        lexStr += " other_after "
                                        break
                                else:
                                    lexStr += "\n" + token.find("orth").text + " " + lex.find("base").text + " " + lex.find("ctag").text
                                break
                    # End of sentence
                    lexStr += "\n"
        # End of loop
        print("Done")
        return lexStr

    def parseLexDefault(self, lexStr):
        result = ""
        print("Parsing...")
        for line in lexStr.split("\n"):
            words = line.split(" ")
            if len(words) == 1:
                result += "\n"
                continue

            result += words[0] + " " + words[1]

            if len(words) == 3:
                result += " nothing"
            else:
                result += " " + words[2]

            result += "\n"
        # End of loop
        print("Done")
        return result

    def parseLex(self, lexStr):
        liczbaKolumn = 4
        result = ""
        print("Parsing...")
        for line in lexStr.split("\n"):
            words = line.split(" ")
            if len(words) == liczbaKolumn-1:
                dodacNothing = True
            else:
                dodacNothing = False
            if len(words) > liczbaKolumn :
                words = words[:liczbaKolumn]
            for word in words:
                result += word + " "
            if dodacNothing:
                result += " nothing"
            result += "\n"
        print("Done")
        return result

    def printToFile(self, filePath, strLine):
        with codecs.open(filePath, "w", "UTF-8") as file:
            file.write(strLine)
            file.close()
