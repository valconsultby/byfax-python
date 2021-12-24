from byfax_sdk.FaxFile import FaxFile as File


class FaxGreeting:
    def __init__(self, greetingRef, languageISO, greetingTitle, filePath):
        self.greetingRef = greetingRef
        self.languageISO = languageISO
        self.greetingTitle = greetingTitle
        self.greetingFile = File.CreateFile(filePath=filePath)

    def Get(self):
        return {
            'greetingRef': self.greetingRef,
            'languageISO': self.languageISO,
            'greetingTitle': self.greetingTitle,
            'greetingFile': self.greetingFile,
        }
