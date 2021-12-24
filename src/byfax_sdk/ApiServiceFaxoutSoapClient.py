import zeep
from byfax_sdk.models.ApiRequestFaxjobCountBroadcasts import ApiRequestFaxjobCountBroadcasts
from byfax_sdk.models.ApiRequestFaxjobCountMessages import ApiRequestFaxjobCountMessages
from byfax_sdk.models.ApiRequestFaxjobMessage import ApiRequestFaxjobMessage
from byfax_sdk.models.ApiRequestFaxjobProcess import ApiRequestFaxjobProcess
from byfax_sdk.models.ApiRequestFaxjobSubmit import ApiRequestFaxjobSubmit
from byfax_sdk.models.ListPagination import ListPagination


class ApiServiceFaxoutSoapClient:

    def __init__(self, apiKey, apiSecret, url):
        self.__wsdl = url+'/soap/1.1/faxout?WSDL'
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

    def Delete(self, messageRef: str):
        responce = self.__client.service.Delete(
            _soapheaders=[self.__usernameTockenHeader], messageRef=messageRef)
        return responce

    def Download(self, messageRef: str, isPdf: bool):
        responce = self.__client.service.Download(
            _soapheaders=[self.__usernameTockenHeader], messageRef=messageRef, isPdf=isPdf)
        return responce

    def GetBalance(self):
        responce = self.__client.service.getBalance(
            _soapheaders=[self.__usernameTockenHeader])
        return responce

    def CheckTiffExists(self, tiffRef: str):
        responce = self.__client.service.checkTiffExists(
            _soapheaders=[self.__usernameTockenHeader], tiffRef=tiffRef)
        return responce

    def CountBrodcasts(self,  countBrodcasts: ApiRequestFaxjobCountBroadcasts):
        responce = self.__client.service.countBrodcasts(
            _soapheaders=[self.__usernameTockenHeader], countBrodcasts=countBrodcasts .Get())
        return responce

    def ListBrodcasts(self,  countBrodcasts: ApiRequestFaxjobCountBroadcasts, listPagination: ListPagination):
        responce = self.__client.service.listBrodcasts(
            _soapheaders=[self.__usernameTockenHeader], countBrodcasts=countBrodcasts.GetList(listPagination))
        return responce

    def СountRecipients(self,  listRequest: ApiRequestFaxjobCountMessages):
        responce = self.__client.service.countRecipients(
            _soapheaders=[self.__usernameTockenHeader], listRequest=listRequest.Get())
        return responce

    def ListRecipients(self,  listRequest: ApiRequestFaxjobCountMessages, listPagination: ListPagination):
        responce = self.__client.service.listRecipients(
            _soapheaders=[self.__usernameTockenHeader], listRequest=listRequest.GetList(listPagination))
        return responce

    def Cancel(self,  cancelRequest: ApiRequestFaxjobProcess):
        responce = self.__client.service.Cancel(
            _soapheaders=[self.__usernameTockenHeader], cancelRequest=cancelRequest.Get())
        return responce

    def Pause(self,  cancelRequest: ApiRequestFaxjobProcess):
        responce = self.__client.service.Pause(
            _soapheaders=[self.__usernameTockenHeader], cancelRequest=cancelRequest.Get())
        return responce

    def Resubmit(self,  cancelRequest: ApiRequestFaxjobProcess):
        responce = self.__client.service.Resubmit(
            _soapheaders=[self.__usernameTockenHeader], cancelRequest=cancelRequest.Get())
        return responce

    def Resume(self,  cancelRequest: ApiRequestFaxjobProcess):
        responce = self.__client.service.Resume(
            _soapheaders=[self.__usernameTockenHeader], cancelRequest=cancelRequest.Get())
        return responce

    def SubmitMessage(self,  submitRequest: ApiRequestFaxjobMessage):
        responce = self.__client.service.SubmitMessage(
            _soapheaders=[self.__usernameTockenHeader], submitRequest=submitRequest.Get())
        return responce

    def Submit(self,  submitRequest: ApiRequestFaxjobSubmit):
        responce = self.__client.service.Submit(
            _soapheaders=[self.__usernameTockenHeader], submitRequest=submitRequest.Get())
        return responce
