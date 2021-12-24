from attr import dataclass


@dataclass
class FaxContact:
    Name: str
    Company: str
    Number: str
    Timezone: str

    def Get(self):
        return {
            'Name': self.Name,
            'Company': self.Company,
            'Number': self.Number,
            'Timezone': self.Timezone,
        }
