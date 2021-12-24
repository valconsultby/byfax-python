from attr import dataclass
from datetime import datetime
from byfax_sdk.models.ListPagination import ListPagination


@dataclass
class ApiRequestFaxjobCountBroadcasts:
    broadcastRefs: list[str]
    dateFrom: datetime
    dateTill: datetime

    def Get(self):
        return {
            'broadcastRefs': self.broadcastRefs,
            'dateFrom': self.dateFrom,
            'dateTill': self.dateTill,
        }

    def GetList(self, listPagination: ListPagination):
        return {
            'broadcastRefs': self.broadcastRefs,
            'dateFrom': self.dateFrom,
            'dateTill': self.dateTill,
            'pagination': listPagination.Get(),
        }
