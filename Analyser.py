# Handels the Analysation

from OCR import OCRHanlder
import os
from ASHandler import *


class AnalyseHandler:
    def __init__(self, PDFFiles, destination):

        # Sets up the File which Analyses and sets up Destination Path Folder.

        self.PDFOriginal = PDFFiles
        self.DestinationPath = destination
        self.OCRH = OCRHanlder()
        self.ash = ArbeitsscheinHandler()

    def run(self):

        # OCRs the PDF and Analyses the File afterwarth

        for file in self.PDFOriginal:
            self.OCRH.OCRFile(file)
            for Nr in range(self.OCRH.NrOfPages()):
                self.savePage(Nr, file)

    def savePage(self, pageNr, file):
        tokens = self.OCRH.GetTokenForPage(pageNr)
        tokens = self.OCRH.cleanTokens(tokens)
        self.asNr = None

        for i in tokens:
            if (len(i) == 9 and i.isnumeric() and i.startswith("10")) or (i.startswith("9") and i.isnumeric and len(i) == 8):
                self.asNr = i

        try:
            parts = file.split(".p")

            self.name = parts[0] + self.asNr
        except:
            self.name = "adada"
            pass

        print(self.name)

        self.asNr = None

        self.checkFile()

        os.chdir(os.path.dirname(file))

        os.rename(os.path.basename(file), self.name+".pdf")

    def checkFile(self):
        if os.path.exists( self.name+".pdf"):
            self.name = self.name + "I"

            self.checkFile()