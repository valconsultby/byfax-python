from attr import dataclass


@dataclass
class ApiRequestMessageCount:
    pageNumber: int
    pageSize: int 

    def Get(self):
        return {
            'pagination': {
                'pageNumber': 1,
                'pageSize': 10
            }
        }
