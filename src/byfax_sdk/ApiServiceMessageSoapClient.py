import zeep

from ApiRequestMessageCount import ApiRequestMessageCount


class ApiServiceMessageSoapClient:

    def __init__(self, apiKey, apiSecret, url):
        self._wsdl = url+'/soap/1.1/faxin/message?WSDL'
        self._usernameTockenHeader = zeep.xsd.Element(
            'UsernameToken',
            zeep.xsd.ComplexType([
                zeep.xsd.Element(
                    'Username', zeep.xsd.String()),
                zeep.xsd.Element(
                    'Password', zeep.xsd.String()),
            ])
        )
        self._usernameTockenHeader = self._usernameTockenHeader(
            Username=apiKey, Password=apiSecret)

        self._client = zeep.Client(wsdl=self._wsdl)

    def DeleteFax(self, messageRef: str):
        responce = self._client.service.deleteFax(
            _soapheaders=[self._usernameTockenHeader], messageRef=messageRef)
        return responce

    def DownloadFax(self, messageRef: str, isPDF: bool):
        responce = self._client.service.downloadFax(
            _soapheaders=[self._usernameTockenHeader], messageRef=messageRef, isPDF=isPDF)
        return responce

    def CountFaxes(self, listRequest: ApiRequestMessageCount):
        responce = self._client.service.countFaxes(
            _soapheaders=[self._usernameTockenHeader], listRequest=listRequest.Get())
        return responce

    def ListFaxes(self, listRequest: ApiRequestMessageCount):
        responce = self._client.service.listFaxes(
            _soapheaders=[self._usernameTockenHeader], listRequest=listRequest.Get())
        return responce
