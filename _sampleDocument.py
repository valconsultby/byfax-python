from byfax_sdk.ApiServiceDocumentSoapClient import ApiServiceDocumentSoapClient

# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create "document " API service and pass API key-secret and url data
documentService = ApiServiceDocumentSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# Call Api function "uploadDocument" to upload a document to cache
uploadResponce = documentService.UploadDocument(
    fileName='/home/my-file.png')
print(uploadResponce)

