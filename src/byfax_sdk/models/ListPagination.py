from attr import dataclass

@dataclass
class ListPagination:
    pageNumber: int
    pageSize: int

    def Get(self):
        return {
            'pageNumber': self.pageNumber,
            'pageSize': self.pageSize
        }