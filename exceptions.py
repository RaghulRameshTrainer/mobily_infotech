'''
4 clauses in exceptions:
try
except
else
finally
'''
try:
    with open('day.txt','r') as fo:
        print(fo.read())
    res=5+6
    print("RESULT:", res)
    #print(lst[0])
    age=int(input("Enter you age:"))
    if age<0 or age>100:
        raise ValueError('Age should be between 0-100 only.')
    else:
        print('age is : ', age)
except FileNotFoundError as e:
    print("Error while reading the file.",e)
except TypeError as e:
    print("Error while performing an addition.",e)
except ValueError as e:
    print("AGE ERROR:",e)
except Exception as e:
    print("NEW ERROR",e)
else:
    print('Else runs when there is no exception!')
finally:
    print("Irrespective of the exception, finally runs")
print("I am next line in my program")