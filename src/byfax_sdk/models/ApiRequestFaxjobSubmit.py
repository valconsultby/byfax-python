from byfax_sdk.FaxFile import FaxFile as File
from attr import dataclass
from datetime import datetime
from byfax_sdk.models.FaxQuality import FaxQuality
from byfax_sdk.models.FaxMode import FaxMode
from byfax_sdk.models.FaxContact import FaxContact
from byfax_sdk.models.FaxRecipient import FaxRecipient


@dataclass
class ApiRequestFaxjobSubmit:
    broadcastRef: str
    sendRef: str
    Header: str
    Subject: str
    Priority: int
    busyRetry: int
    sendAt: datetime
    sendQuality: FaxQuality
    sendMode: FaxMode
    Sender: FaxContact
    Recipients: list[FaxRecipient]
    Documents: list[str]
    coverRef: str
    coverText: str

    def Get(self):
        documents = []
        for i in self.Documents:
            documents.insert(0, File.CreateDocumentFile(filePath=i))
        return {
            'broadcastRef': self.broadcastRef,
            'sendRef': self.sendRef,
            'Header': self.Header,
            'Subject': self.Subject,
            'Priority': self.Priority,
            'busyRetry': self.busyRetry,
            'sendAt': self.sendAt,
            'sendQuality': self.sendQuality.name,
            'sendMode': self.sendMode.name,
            'Sender': self.Sender,
            'Recipients': self.Recipients,
            'Documents': documents,
            'coverRef': self.coverRef,
            'coverText': self.coverText,
        }
