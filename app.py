# TEXT/BINARY FILE BASED EMPLOYEE MANAGEMENT SYSTEM
# CURD
# Create Update Read Delete

import pickle
import os

# FUNCTION TO ADD AN EMPLOYEE
def addEmp():
    file = open("employee.dat","ab")
    empId = input("\n\tEnter Employee ID : ")
    empName = input("\tEnter Employee Name : ")
    empAdd = input("\tEnter Employee Address : ")
    empSal = input("\tEnter Employee Salary : ")
    pickle.dump(empId,file)
    pickle.dump(empName,file)
    pickle.dump(empAdd,file)
    pickle.dump(empSal,file)
    print("\n\tEmployee Added Successfully!\n\n")
    input("Press Enter To Continue...")
    file.close()

# FUNCTION TO VIEW ALL EMPLOYEES
def viewAllEmp():
    file = open("employee.dat","rb")
    try:
        count = 0
        while(True):
            data = pickle.load(file)
            print(data,end="  ")
            count=count+1
            if(count%4==0):
                print()
    except EOFError as e:
        print("\n\tHere Are All Employees Details\n\n")
        input("Press Enter To Continue...")
    file.close()

# FUNCTION TO VIEW AN EMPLOYEE BY HIS/HER EMPLOYEE ID
def viewEmp():
    file = open("employee.dat","rb")
    print("\n\n\tEnter Employee ID : ",end="")
    empId = input()
    userFound = 0
    try:
        while(True):
            data = pickle.load(file)
            if(data==empId):
                print("\n\tEmployee ID : ",data)
                print("\tEmployee Name : ",pickle.load(file))
                print("\tEmployee Address : ",pickle.load(file))
                print("\tEmployee Salary : ",pickle.load(file))
                userFound = 1
    except EOFError:
        if(userFound==1):
            print("\n\n\tHere is Your Employee")
        else:
            print("\n\n\tEmployee Not Found!")
        input("Press Enter To Continue...")
    file.close()

# FUNCTION TO DELETE AN EMPLOYEE
def deleteEmp():
    empFile = open("employee.dat","rb")
    tempFile = open("temp.dat","ab")
    print("\n\tEnter Employee ID To Delete : ",end="")
    empId = input()
    userFound = 0
    try:
        while(True):
            data = pickle.load(empFile)
            if(data==empId):
                pickle.load(empFile)
                pickle.load(empFile)
                pickle.load(empFile)
                userFound = 1
            else:
                pickle.dump(data,tempFile)
    except EOFError:
        if(userFound==1):
            print("\n\n\tEmployee Deleted Successfully!")
        else:
            print("\n\n\tEmployee Not Found!")
        input("\n\nPress Enter To Continue...")
    empFile.close()
    tempFile.close()
    os.remove("employee.dat")
    os.rename("temp.dat","employee.dat")

# FUNCTION TO COUNT NUMBER OF EMPLOYEES
def totalEmp():
    file = open("employee.dat","rb")
    count = 0
    try:
        while(True):
            pickle.load(file)
            count=count+1
    except EOFError:
        print("\n\n\tTotal Employees :",count//4)
        input("\n\nPress Enter To Continue...")
    file.close()
  
# FUNCTION TO UPDATE INFORMATION OF AN EMPLOYEE
def updateEmp():
    empFile = open("employee.dat","rb")
    tempFile = open("temp.dat","ab")
    empId = input("\n\tEnter Employee ID To Update : ")
    userFound = 0
    try:
        while(True):
            data = pickle.load(empFile)
            if(data==empId):
                pickle.dump(data,tempFile)
                name = pickle.load(empFile)
                pickle.dump(name,tempFile)
                print("Employee ID :",data)
                print("Employee Name :",name)
                empAdd = input("\tEnter Address : ")
                empSal = input("\tEnter Salary : ")
                pickle.dump(empAdd,tempFile)
                pickle.dump(empSal,tempFile)
                # for skip employee previous detail
                pickle.load(empFile)
                pickle.load(empFile)
                userFound = 1
            else:
                pickle.dump(data,tempFile)
    except EOFError :
        if(userFound == 1):
            print("\n\tEmployee Updated Successfully!")
        else:
            print("\n\tEmployee Not Found!")
        input("\n\nPress Enter To Continue...")
    empFile.close()
    tempFile.close()
    os.remove("employee.dat")
    os.rename("temp.dat","employee.dat")


# DASHBOARD
while(True):
    print("\n\t**** EMPLOYEE MANAGEMENT SYSTEM ****")
    print("\n\t1. Add Employee")
    print("\t2. View All Employee")
    print("\t3. View An Employee By Employee ID")
    print("\t4. Delete An Employee")
    print("\t5. Total Employee")
    print("\t6. Update An Employee")
    print("\t7. Exit")
    print("\n\tEnter Your Choice : ",end="")
    ch = int(input())
    if(ch==7):
        print("\n\t--- Bye-Bye User!")
        break
    elif(ch==1):
        addEmp()
    elif(ch==2):
        viewAllEmp()
    elif(ch==3):
        viewEmp()
    elif(ch==4):
        deleteEmp()
    elif(ch==5):
        totalEmp()
    elif(ch==6):
        updateEmp()
    else:
        print("\nWrong Entered!\nTry Again!")
        input("\iMyTrans")
