PRODUCT
-------------------

byFax is an online faxing platform that allows you to send and receive faxes without fax machines or any other devices directly in your browser or through the API integration presented here.
More information about the platform and its abilities can be found on the <a href="https://byfax.biz">byFax</a> website (https://byfax.biz).


REQUIREMENTS
------------

The minimum requirement for this project is Python 3.6


SERVICES
------------

To get started with the API, you need to create a byFax application and get the api-key and api-secret to authorize your application to the API.
As you implement your solution, you have a fully functional test environment at https://sandbox.byfax.biz
When your solution is complete, the base url for services changes to the production environment to https://api.byfax.biz
See the services list below.

- cover - cover page management. <a href="https://api.byfax.biz/soap/1.1/cover" targe='__blank'>[Detailed description and WSDL link]</a>
- document - fax documents cache management. <a href="https://api.byfax.biz/soap/1.1/document" targe='__blank'>[Detailed description and WSDL link]</a>
- faxout - sending fax and monitoring delivery status and downloading faxes as PDF files. <a href="https://api.byfax.biz/faxout" targe='__blank'>[Detailed description and WSDL link]</a>
- faxin/message - obtain list of received faxes and downloading as PDF files. <a href="https://api.byfax.biz/soap/1.1/faxin/message" targe='__blank'>[Detailed description and WSDL link]</a>
- faxin/inventory - receiving data about assigned virtual fax-numbers. <a href="https://api.byfax.biz/soap/1.1/faxin/inventory" targe='__blank'>[Detailed description and WSDL link]</a>


SAMPLES
------------

## Authorization
The application is authorized to the API using a special SOAP header that contains api-key and api-secret. The header is represented by a UsernameToken object.

The authorization header is passed in every request, the connection to the API has no sessions and no additional tokens.

```python
# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create the appropriate service object and pass parameters. Cover service as an example
coverService = ApiServiceCoverSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)
```

## Cover pages. List
Cover Pages are available for more personalized faxing in byFax. The system has already been loaded with a basic set of cover pages, which are available via API as well as in the byFax customer portal.

Both portal users and API developers in their applications have the ability to add own custom cover pages. The cover page is a DocX file with predefined placeholders that are replaced with the sender and recipient data during the sending process.

```python
# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create the appropriate service object and pass parameters.
coverService = ApiServiceCoverSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# call "ListCovers" function and obtain response
responce = coverService.ListCovers()
print('ListCovers')
print(responce)    
```      

## Cover pages. Add new
To add a cover page, you should upload a DocX file to the system and setup its name.

```python
# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create the appropriate service object and pass parameters.
coverService = ApiServiceCoverSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# call "AddCover" function and obtain response
responce = coverService.AddCover(
    filePath='/home/my-cover.docx', title='New Cover')
print('AddCover')
print(responce)
```

## Preloading a document
In case the same file must be sent several times or to many recipients, the system provides the ability to upload a document and save it for further reuse.

```python
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
```

## Sending a fax (common submission way)
The system provides many options to pass to send fax request - loading documents directly within the request, using previously uploaded documents, using a cover page, submit fax in high or standard quality, submit fax in text or photo mode, submit fax for one or more documents in the request, submit fax for one or more recipients, setting your own fax header format, setting the number of retries in case the number is busy, etc. Below there is an example of using the most common options.

```python
# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create "faxout" service object and fill base params
faxoutService = ApiServiceFaxoutSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# Sender identification. At least one of properties is required
senderContact = FaxContact(Name='sender name', 
                           Company='sender company',
                           Number='+375991111111', 
                           Timezone=None)

recipientContact = FaxContact(Name='recipient name', 
                              Company='recipient company',
                              Number='+375991111111', 
                              Timezone=None)
// Submission broadcast refID.
// Unique within your API account
// Should be unique for each submission
// Uncomment this line to set at your side otherwise API will generate.

# Recipient object. Number and Name/Company are required.
# messageRef - Message refID. Unique within your API account. Should be unique for each recipient. Put your identifier or keep empty to let API generate and return
# Header - override fax-page header for the recipient,
# Subject - overrider cover-page subject for the recipient,
recipient = FaxRecipient(FaxContact=recipientContact,
                         messageRef=None,
                         sendRef=None,
                         Header=None,
                         Subject=None,
                         Greeting=None)

# Call "Submit" API function to push fax into the queue
# broadcastRef - Submission refID. Unique within your API account. Should be unique for each submission. Put your identifier or keep empty to let API generate and return
# Header - Fax page header format
# Subject - Cover page subject, keep empty if cover page is not set
# busyRetry - Total number of call retry in case of Busy or NoAnswer
# sendAt - date-time with timezone to send the fax at. Keep empty to send immediately
# coverRef - CoverPage reference ID returned by ListCovers or AddCover
# coverText - cover page text, keep empty if cover page is not set
request = ApiRequestFaxjobSubmit(broadcastRef=None,
                                 sendRef=None,
                                 Header='{DateTime} {Timezone}|From: {FromNumber} To: {ToNumber}|page <CurPage> from <CurPages>',
                                 Subject='',
                                 Priority=1,
                                 busyRetry=3,
                                 sendAt=None,
                                 sendQuality=FaxQuality.FINE,
                                 sendMode=FaxMode.TEXT,
                                 Sender=senderContact,
                                 Recipients=[recipient.Get()],
                                 Documents=['/home/my-file.png'],
                                 coverRef=None,
                                 coverText=None)

responce = faxoutService.Submit(request)
print('Submit\n'+str(responce))

# Fill list of recipients to check status for
countMessages = ApiRequestFaxjobCountMessages(messageRefs=[responce.reportRecipients[0].messageRef])
# Add and fill pagination data
pagination = ListPagination(0,10)

# Call "ListRecipients" API function to obtain recipients status
responce = faxoutService.ListRecipients(listRequest=countMessages,listPagination=pagination)
print('ListRecipients\n'+str(responce))
```

## Sending a fax (prepared TIFF submission)
This method was specifically designed to send a prepared TIFF file to a single recipient. The method is used only if the TIFF file is prepared on the application`s side and it must be sent without going through the byFax document preparation system. Using this method application should pass only the following data, sender details (Sender object), recipient details (Recipient object), the unique identifier of the container (broadcastRef parameter) and the prepared TIFF file (document object). The full text of the fax header could also be passed to be placed at the top of the page. If the header is already placed to all pages of the document, then the header parameter is passed as empty string. Here is an example of using this function.

```python
# Replace with your credentials from application settings
apiKey = 'YOUR-API-KEY'
apiSecret = 'YOUR-API-SECRET'

# Replace with https://api.byfax.biz for production
url = 'https://sandbox.byfax.biz'

# Create "faxout" service object and fill base params
faxoutService = ApiServiceFaxoutSoapClient(
    apiKey=apiKey, apiSecret=apiSecret, url=url)

# Sender identification. At least one of properties is required
senderContact = FaxContact(Name='sender name', 
                    Company='sender company',
                    Number='+375991111111', 
                    Timezone=None)

# Recipient identification. At least one of properties is required
recipientContact = FaxContact(Name='recipient name', 
                    Company='recipient company',
                    Number='+375992222222', 
                    Timezone=None)                    

# Recipient object. Number and Name/Company are required.
recipient = FaxRecipient(FaxContact=recipientContact,
                         messageRef='',
                         sendRef=None,
                         Header=None,
                         Subject=None,
                         Greeting=None)

# Call "Submit" API function to push fax into the queue. Only single recipient and single TIFF file allowed.
# broadcastRef - Submission refID. Unique within your API account. Should be unique for each submission. Put your identifier or keep empty to let API generate and return
# Header - Fax page header format
# Subject - Cover page subject, keep empty if cover page is not set
# busyRetry - Total number of call retry in case of Busy or NoAnswer
request = ApiRequestFaxjobMessage(broadcastRef=None,
                                 sendRef=None,
                                 messageRef=None,
                                 Header='{DateTime} {Timezone}|From: {FromNumber} To: {ToNumber}|page <CurPage> from <CurPages>',
                                 Subject=None,
                                 Priority=1,
                                 busyRetry=3,
                                 Sender=senderContact,
                                 Recipient=recipient.Get(),
                                 DocumentPath=['/home/my-file.tiff'])

responce = faxoutService.SubmitMessage(request)
print('SubmitMessage\n'+str(responce))

# Fill list of recipients to check status for
countMessages = ApiRequestFaxjobCountMessages(messageRefs=[responce.reportRecipients[0].messageRef])
# Add and fill pagination data
pagination = ListPagination(0,10)

# Call "ListRecipients" API function to obtain recipients status
responce = faxoutService.ListRecipients(listRequest=countMessages,listPagination=pagination)
print('ListRecipients\n'+str(responce))
```


Still have questions?
------------

If you still have any questions, or the samples above are not informative enough, you are able get more detailed information about API functions, objects and enumerations in the detailed description of each service (links can be found above), you can also contact us via helpdesk or JivoSite. We are always glad to hear suggestions and ideas for expanding or improving both the byFax API and our entire product.

At the moment, only the basic functionality of the byFax portal is available in our open API, if you need to expand the capabilities or add fundamentally new functions, we are always happy to discuss.

If you are a Java, Ruby, Go or other programming language developer and would like to help improving the byFax API SDK, we will be glad to have your help developing SDKs in other languages.
