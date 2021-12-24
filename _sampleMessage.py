from byfax_sdk.models.ApiRequestMessageCount import ApiRequestMessageCount
from byfax_sdk.ApiServiceMessageSoapClient import ApiServiceMessageSoapClient

apiKey = 'BZZf95261F9Rpbd7'
apiSecret = '7kEGONiBxGSrX6tUdialNA1HZAbgmPXuFrxLNx1A4yNfI3YqIuRyPVyZf6xHccRZ'
url = 'https://beta-api.byfax.biz'

documentService = ApiServiceMessageSoapClient(apiKey, apiSecret, url)

ApiRequestCountFaxes=ApiRequestMessageCount(0,10)

responce = documentService.CountFaxes(ApiRequestCountFaxes)
print('CountFaxes')
print(responce)

ApiRequestCountFaxes=ApiRequestMessageCount(0,10)

responce = documentService.ListFaxes(ApiRequestCountFaxes)
print('ListFaxes')
print(responce)
