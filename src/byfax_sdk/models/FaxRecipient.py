from byfax_sdk.models.FaxContact import FaxContact
from byfax_sdk.models.FaxGreeting import FaxGreeting

class FaxRecipient:

    def __init__(self, FaxContact: FaxContact, messageRef, sendRef, Header, Subject, Greeting: FaxGreeting):
        self.FaxContact = FaxContact
        self.sendRef = sendRef
        self.Header = Header
        self.Subject = Subject
        self.messageRef = messageRef
        if(type(Greeting)== FaxGreeting):
            self.Greeting = Greeting.Get()
            
        if(type(Greeting)!= FaxGreeting):
            self.Greeting = None


    def Get(self):
        return {
            'Name': self.FaxContact.Name,
            'Company': self.FaxContact.Company,
            'Number': self.FaxContact.Number,
            'messageRef': self.messageRef,
            'sendRef': self.sendRef,
            'Header': self.Header,
            'Subject': self.Subject,
            'Greeting': self.Greeting,
        }