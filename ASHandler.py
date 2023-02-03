import datetime

from Validater import Validater


def nullstring(dateTime):
    if dateTime is not None and dateTime == 0:
        return "00"
    elif dateTime is not None and dateTime < 10:
        return "0" + str(dateTime)
    elif dateTime is not None:
        return str(dateTime)

class ArbeitsscheinHandler:
    def __init__(self):
        self.AS = 'Arbeitsschein'
        self.As2P = 'Arbeitsschein2Page'
        self.Vali = Validater()
        self.allZGrund = ['ZGRUND', 'Z-GRUND', '2-grund']
        self.Seite = 'Seite'
        self.ZustellungGrund = ['200', '510', '520', '530', '540', '560', '351', '352', '30A', '30B', '30C', '30E',
                                '30F', '31D', '31F', '31R', '31S', '39S', '39O', '39P', '030', '035', '050']
        self.ArbeitsscheinSentence = ['arbeitsauftrag', 'entsprechend', 'regelwerk', 'ordnungsgemäß', 'vollständig']

    def isPageArbeitsschein(self, pageName):

        # Returns True if the PageName belongs to a 'Arbeitsschein'

        if self.AS in pageName or self.isDefinedName(pageName) or self.As2P in pageName:
            return True
        else:
            return False

    def specifieUnspecifiedDoc(self, destinationFiles, unspecifiedPage):

        # Tries to return a specified Name for the 'Arbeitsschein'
        # DestinationFiles: List of all DestinationFileNames
        # UnspecifiedPage: Name of the currently unspecified Page.

        DefinedPage = ''
        if self.As2P in unspecifiedPage:
            for idx, Page in enumerate(destinationFiles):
                if self.As2P in Page:
                    if idx == 0:
                        return 'IgnorePage'
                    if self.isDefinedName(destinationFiles[idx - 1]):
                        return destinationFiles[idx - 1]
            return 'IgnorePage'

        for Page in destinationFiles:
            if self.isDefinedName(Page):
                if DefinedPage == '':
                    DefinedPage = Page
                elif DefinedPage != Page:
                    return unspecifiedPage
        return DefinedPage


    def isDefinedName(self, pageName):

        # Checks if the Dokument ist a 'ArbeitsscheinName' which is defined.

        PageNameParts = pageName.split('_')
        if (len(PageNameParts) != 3 or not self.Vali.isFazNr(PageNameParts[0]) or
                not (len(PageNameParts[1]) <= 8 and len(PageNameParts[1]) >= 6) or
                not PageNameParts[1].isnumeric() or
                not self.isZustellungGrund(PageNameParts[2])):
            return False
        return True

    def isArbeitsschein(self, multipleTokens):

        # Checks if the word 'Arbeitsschein' is in the Document

        multipleTokens = self.Vali.lowercastTokens(multipleTokens)
        if ('arbeitsschein' in multipleTokens or
                len(set(self.ArbeitsscheinSentence) - set(multipleTokens)) == 0):
            return True

    def isZustellungGrund(self, token):
        if token in self.ZustellungGrund:
            return True
        return False

