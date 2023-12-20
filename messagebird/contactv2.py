from messagebird.base import Base
from messagebird.base_list import BaseList


class Contactv2(Base):

    def __init__(self):
        self.id = None
        self.href = None
        self.displayName = None
        self.firstName = None
        self.lastName = None
        self.country = None
        self.avatar = None
        self.status = None
        self.Identifiers = None
        self.languages = None
        self.gender = None
        self.attributes = None
        self._createdDatetime = None
        self._updatedDatetime = None


    print('si entra')
    

  

    @property
    def createdDatetime(self):
        return self._createdDatetime

    @createdDatetime.setter
    def createdDatetime(self, value):
        y = self._createdDatetime = self.value_to_time(value)
        print(y)
    


    @property
    def updatedDatetime(self):
        return self._updatedDatetime

    @updatedDatetime.setter
    def updatedDatetime(self, value):
        self._updatedDatetime = self.value_to_time(value)

