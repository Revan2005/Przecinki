# -*- coding: utf-8 -*-
__author__ = 'Koralgoll'

import sys

from src.Parser import Parser

def main(argv=sys.argv):
    parser = Parser()

    # Generate training data
    lexStr = parser.getLexFromXML("../docs/samePopularnonaukowe/uczace/")
    result = parser.parseLex(lexStr)
    parser.printToFile("../docs/samePopularnonaukowe/parsingOutput/train.data", result)

    #lexStr = parser.xxx("../docs/samePopularnonaukowe/uczace/")
    #parser.printToFile("../docs/samePopularnonaukowe/parsingOutput/train.data", lexStr)
    # Generate testing data
    lexStr = parser.getLexFromXML("../docs/samePopularnonaukowe/testowe/kap")
    result = parser.parseLex(lexStr)
    parser.printToFile("../docs/samePopularnonaukowe/parsingOutput/test.data", result)


if __name__ == "__main__":
    main()
