from bank import Account

acc=Account('Karthick','Rajesh','AGTHR5454F',5000)
print(acc.userid)
print(acc.password)
print(acc._Account__balance)
acc._Account__balance=10000000
print(acc._Account__balance)


