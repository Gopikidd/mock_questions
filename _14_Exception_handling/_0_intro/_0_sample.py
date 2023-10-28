
# Exception handling
'''
Traceback (most recent call last):
  File "C:/Users/madhu/git_projects/_14_Exception_handling/mypractice/test1.py", line 11, in <module>
    print("Result is ", in_val + 10)
TypeError: must be str, not int

Everything is an object in Python***

'''
print("----Before exception1-----")
print("----Before exception2-----")
list1 = [11, 22, 33, 45]  # from UI, from Database json.loads(user_data)
print("List data : ", list1[5])
print("----After exception-----")

'''
During Exception:
-----------------
1. Create object: It will create object of IndexError with message
                            IndexError("list index out of range")
                   Loads class  : 
                            It will load the exception class IndexError object                
                                     ===> Employee(100,'Madhu',15000)
3. Throws exception class object
        - Not handled: Throws to console 
        - Handled    : Throws to except block
       
'''
print(100/0)

in_val = int(input("Enter value : "))
print("Result is ", in_val + '10')
print("End of program")
