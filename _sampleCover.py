from byfax_sdk.ApiServiceCoverSoapClient import ApiServiceCoverSoapClient

# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create "cover" service object and fill base params
coverService = ApiServiceCoverSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# call "ListCovers" function and obtain response
responce = coverService.ListCovers()
print('ListCovers')
print(responce)

# call "AddCover" function and obtain response
responce = coverService.AddCover(
    filePath='/home/my-cover.docx', title='New Cover')
print('AddCover')
print(responce)

# call "RenameCover" function and obtain response
# coverRef - reference ID returned by ListCovers or AddCover
renameResponce = coverService.RenameCover(
    coverRef='coverRef', title='New Title')
print('RenameCover')
print(renameResponce)

# call "GetCover" function and obtain response
# coverRef - reference ID returned by ListCovers or AddCover
GetCoverResponce = coverService.GetCover(coverRef='coverRef')
print('GetCover')
print(GetCoverResponce)

# call "ReloadCover" function and obtain response
# coverRef - reference ID returned by ListCovers or AddCover
responce = coverService.ReloadCover(
    filePath='/home/my-cover.docx', coverRef='coverRef')
print('ReloadCover')
print(responce)

# call "DeleteCover" function and obtain response
# coverRef - reference ID returned by ListCovers or AddCover
responce = coverService.DeleteCover(coverRef='coverRef')
print('DeleteCover')
print(responce)
