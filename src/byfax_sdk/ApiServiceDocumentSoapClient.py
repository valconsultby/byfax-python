from types import FrameType
import zeep
from byfax_sdk.models.FaxMode import FaxMode
from byfax_sdk.models.FaxQuality import FaxQuality
from byfax_sdk.FaxFile import FaxFile as File


class ApiServiceDocumentSoapClient:

    __wsdl = None
    __usernameTockenHeader = None

    def __init__(self, apiKey, apiSecret, url):
        self.__wsdl = url+'/soap/1.1/document?WSDL'
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

    def UploadDocument(self, fileName: str):
        responce = self.__client.service.uploadDocument(
            _soapheaders=[self.__usernameTockenHeader],
            uploadDocument=File.CreateDocumentFile(filePath=fileName))
        return responce

    def DownloadDocument(self, documentRef: str):
        responce = self.__client.service.downloadDocument(
            _soapheaders=[self.__usernameTockenHeader],
            documentRef=documentRef)
        return responce

    def GetDocumentPreview(self, documentRef: str, faxQuality: FaxQuality, faxMode: FaxMode):
        responce = self.__client.service.getDocumentPreview(
            _soapheaders=[self.__usernameTockenHeader],
            documentRef=documentRef,
            quality=faxQuality.name,
            conversion=faxMode.name)
        return responce
