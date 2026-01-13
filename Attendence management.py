Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#GET NUMBER OF STUDENT IN THE CLASS:-

n = int(input("Enter number of students in the class"))
present_count = 0
absent_count = 0
for rollno in range(1, n+1):
    print("Enter roll no student",rollno,"is present or absent following option 1 or 2 \n 1. present \n 2. absent")
    status = input()

    #CHECK STATUS:-
...     if status == '1':
...         present_count += 1
...     elif status == '2':
...         absent_count += 1
...     else:
...         print("Please select either 1 or 2 options")
... 
...     print("Total student in the class:",n)
...     print("Number of students present:",present_count)
...     print("Number of students absent:",absent_count)
...     percentage = (present_count / n) * 100
...     print("Attendnce Report:",percentage)
... 
... 
...     #GET NUMBER OF STUDENT IN THE CLASS:-
... 
... n = int(input("Enter number of students in the class"))
... present_count = 0
... absent_count = 0
... rollno = 1 #VARIABLE INITIALIZATION
... while rollno <= n: #CONDITION
...     print("Enter roll no student",rollno,"is present or absent following option 1 or 2 \n 1. present \n 2. absent")
...     status = input()
... 
...     #CHECK STATUS:-
...     if status == '1':
...         present_count += 1
...         rollno += 1
...     elif status == '2':
...         absent_count += 1
...         rollno += 1
...     else:
...         print("Please select either 1 or 2 options")
... 
...     print("Total student in the class:",n)
...     print("Number of students present:",present_count)
...     print("Number of students absent:",absent_count)
...     percentage = (present_count / n) * 100
