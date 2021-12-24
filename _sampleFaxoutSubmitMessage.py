from byfax_sdk.models.FaxContact import FaxContact
from byfax_sdk.models.FaxRecipient import FaxRecipient
from byfax_sdk.ApiServiceFaxoutSoapClient import ApiRequestFaxjobMessage
from byfax_sdk.ApiServiceFaxoutSoapClient import ListPagination
from byfax_sdk.ApiServiceFaxoutSoapClient import ApiRequestFaxjobCountMessages
from byfax_sdk.ApiServiceFaxoutSoapClient import ApiServiceFaxoutSoapClient

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
