from attr import dataclass
from datetime import datetime


@dataclass
class ApiRequestFaxjobCountMessages:
    broadcastRefs: list[str]
    messageRefs: list[str]
    dateFrom: datetime
    dateTill: datetime

    def Get(self):
        return {
            'broadcastRefs': self.broadcastRefs,
            'messageRefs': self.messageRefs,
            'dateFrom': self.dateFrom,
            'dateTill': self.dateTill,
        }

    def GetList(self, listPagination):
        return {
            'broadcastRefs': self.broadcastRefs,
            'messageRefs': self.messageRefs,
            'dateFrom': self.dateFrom,
            'dateTill': self.dateTill,
            'pagination': listPagination.Get(),
        }
