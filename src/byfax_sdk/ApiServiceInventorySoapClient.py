import zeep

class ApiServiceInventorySoapClient:

    def __init__(self, apiKey, apiSecret, url):
        self.__wsdl = url+'/soap/1.1/faxin/inventory?WSDL'
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

    def ListCountries(self):
        responce = self.__client.service.listDidGroups(
            _soapheaders=[self.__usernameTockenHeader])
        return responce

    def ListDids(self):
        responce = self.__client.service.listDids(
            _soapheaders=[self.__usernameTockenHeader])
        return responce

    def ListDidGroups(self, countryCodeA3: str,stateCodeA2: str):
        responce = self.__client.service.listDidGroups(
            _soapheaders=[self.__usernameTockenHeader],countryCodeA3 = countryCodeA3,stateCodeA2 = stateCodeA2)
        return responce
        
    def GetDidGroup(self, groupRef: str):
        responce = self.__client.service.getDidGroup(
            _soapheaders=[self.__usernameTockenHeader],groupRef = groupRef)
        return responce
        
    def ListStates(self, groupRef: str):
        responce = self.__client.service.listStates(
            _soapheaders=[self.__usernameTockenHeader],groupRef = groupRef)
        return responce