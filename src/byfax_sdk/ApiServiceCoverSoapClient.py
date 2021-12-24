import zeep

from byfax_sdk.FaxFile import FaxFile as File


class ApiServiceCoverSoapClient:

    __wsdl = None
    __usernameTockenHeader = None

    def __init__(self, apiKey, apiSecret, url):
        self.__wsdl = url+'/soap/1.1/cover?WSDL'
        self.__usernameTockenHeader = zeep.xsd.Element(
            'UsernameToken',
            zeep.xsd.ComplexType([
                zeep.xsd.Element(
                    'Username', zeep.xsd.String()),
                zeep.xsd.Element(
                    'Password', zeep.xsd.String()),
            ])
        )
        self.__usernameTockenHeader = self.__usernameTockenHeader(
            Username=apiKey, Password=apiSecret)
        self.__client = zeep.Client(wsdl=self.__wsdl)

    def AddCover(self, filePath: str, title: str):
        responce = self.__client.service.addCover(
            _soapheaders=[self.__usernameTockenHeader],
            file=File.CreateFile(filePath=filePath),
            title=title)
        return responce

    def ReloadCover(self,  filePath: str, coverRef: str):
        responce = self.__client.service.reloadCover(
            _soapheaders=[self.__usernameTockenHeader],
            coverRef=coverRef,
            file=File.CreateFile(filePath=filePath))
        return responce

    def DeleteCover(self, coverRef: str):
        responce = self.__client.service.deleteCover(
            _soapheaders=[self.__usernameTockenHeader], coverRef=coverRef)
        return responce

    def DownloadCover(self, coverRef: str):
        responce = self.__client.service.downloadCover(
            _soapheaders=[self.__usernameTockenHeader], coverRef=coverRef)
        return responce

    def GetCover(self, coverRef: str):
        responce = self.__client.service.getCover(
            _soapheaders=[self.__usernameTockenHeader], coverRef=coverRef)
        return responce

    def ListCovers(self):
        responce = self.__client.service.listCovers(
            _soapheaders=[self.__usernameTockenHeader])
        return responce

    def RenameCover(self, coverRef: str, title: str):
        responce = self.__client.service.renameCover(
            _soapheaders=[self.__usernameTockenHeader], coverRef=coverRef, title=title)
        return responce
