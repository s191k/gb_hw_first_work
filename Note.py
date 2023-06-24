from datetime import datetime


class Note:

    count = 0

    def __init__(self, id=None, head=None, body=None, createDate=None):
        if id == None :
            Note.count += 1
            self.id = Note.count
        else:
            self.id = id

        self.head = head
        self.body = body

        if createDate == None:
            self.createDate = str(datetime.now())
        else:
            self.createDate = createDate

    def __repr__(self):
        return "\nid : " + str(self.id) +   "\nhead : " + str(self.head) +   "\nbody : " + str(self.body) +   "\ncreateDate : " + str(self.createDate)
