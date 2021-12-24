from byfax_sdk.models.FaxMode import FaxMode
from byfax_sdk.models.FaxQuality import FaxQuality
from byfax_sdk.models.ApiRequestFaxjobSubmit import ApiRequestFaxjobSubmit
from byfax_sdk.models.FaxContact import FaxContact
from byfax_sdk.models.FaxRecipient import FaxRecipient
from byfax_sdk.ApiServiceFaxoutSoapClient import ListPagination
from byfax_sdk.ApiServiceFaxoutSoapClient import ApiRequestFaxjobCountMessages
from byfax_sdk.ApiServiceFaxoutSoapClient import ApiServiceFaxoutSoapClient
from datetime import datetime

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
