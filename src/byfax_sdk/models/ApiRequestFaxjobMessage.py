from attr import dataclass
from byfax_sdk.models.FaxContact import FaxContact
from byfax_sdk.FaxFile import FaxFile as File


@dataclass
class ApiRequestFaxjobMessage:
    broadcastRef: str
    sendRef: str
    messageRef: str
    Header: str
    Subject: str
    Priority: int
    busyRetry: int
    DocumentPath: str
    Recipient: FaxContact
    Sender: FaxContact

    def Get(self):
        return {
            'broadcastRef': self.broadcastRef,
            'sendRef': self.sendRef,
            'messageRef': self.messageRef,
            'Header': self.Header,
            'Subject': self.Subject,
            'Priority': self.Priority,
            'busyRetry': self.busyRetry,
            'Recipient': self.Recipient.Get(),
            'Sender': self.Sender.Get(),
            'Document': File.CreateDocumentFile(filePath=self.DocumentPath),
        }
