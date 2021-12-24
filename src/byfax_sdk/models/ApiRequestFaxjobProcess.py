from attr import dataclass


@dataclass
class ApiRequestFaxjobProcess:
    broadcastRefs: list[str]
    messageRefs: list[str]
    sendRefs: list[str]

    def Get(self):
        return {
            'broadcastRefs': self.broadcastRefs,
            'sendRefs': self.sendRefs,
            'messageRefs': self.messageRefs
        }