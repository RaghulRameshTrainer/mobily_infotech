class Account():
    def __init__(self,fname,lname,pancard,deposit):
        self.fname=fname
        self.lname=lname
        self.__balance=deposit   #public, protected(_), private(__)
        self.pan=pancard
        self.userid=fname.casefold()+self.pan[-4:]
        self.password=self.pan[:4].casefold()+'@123'

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount):
        self.__balance=self.__balance+amount