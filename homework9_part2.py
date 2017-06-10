import pickle
def load_data():
    try:
        filename = open('employee_pickle.dat', 'rb')
        user_dir = pickle.load(filename)
        print('Opened Pickles')
        filename.close()
        return user_dir
    except:
        print('Opened Aux File')
        filename=open('employee.dat','r')
        user_dir={}
        home_dir={}
        for line in filename:
            data=line.split(',')
            if len(data)==5:
                home_dir['Name']=data[0]
                home_dir['Employee_ID']=data[1]
                home_dir['Department']=data[2]
                home_dir['Title']=data[3]
                home_dir['Salary']=data[4]
                user_dir[data[0]]=home_dir
        return user_dir



def show_stats(user_dir):
    dept_temp={}
    emp_count = 0
    dept_count = 0
    for k in user_dir.keys():
        print(user_dir[k])
        emp_count += 1
    for user_dir[
    for dept not in user_dir['Department']:
        user_dir[dept]=1
        dept_count += 1
    else:
        user_dir['Department'] = user_dir['Department'] + 1
        dept_count += 1
    print(user_dir['Department'])
        

    print('The company has',emp_count,'employees.')
def add_employee(user_dir, Name, Employee_ID, Department, Title, Salary):
    if Name in user_dir:
        print("This employee already exists.")
    else:
       home_dir={}
       home_dir['Name']=Name
       home_dir['Employee_ID']=Employee_ID
       home_dir['Department']=Department
       home_dir['Title']=Title
       home_dir['Salary']=Salary
       user_dir[Name]=home_dir
       return user_dir

def search_id(user_dir, id):
   if id in user_dir:
        print('Displaying statistics for: ',Name)
        for key,values in user_dir[Name].items():
            print(key,":\t", values)
   else:
       print('The employee not found')

def search_name(user_dir, Name):
   if Name in user_dir:
        print('Displaying statistics for: ',Name)
        for key,values in (user_dir[Name].items()):

            print(key,":\t", values)
   else:
       print('The employee not found')

def delete_employee(user_dir, Name):
   if(Name in user_dir):
       del user_dir[Name]
       print(Name, 'has been deleted.')
   else:
       print('no employee to be deleted')
   return user_dir

def save_data(user_dir):
   filename=open('employee_pickle.dat', 'wb')
   pickle.dump(user_dir, filename)
   #for i in user_dir:
    #   line=user_dir[i]['Name']+','+user_dir[i]['Employee_ID']+','+user_dir[i]['Department']+','+user_dir[i]['Title']+','+user_dir[i]['Salary']+'\n'
    #   filename.write(line)
   filename.close()


def main():
    user_dir=load_data()
    while(True):
        print('1. Add an Employee')
        print('2. Find an Employee (By Name)')
        print('3. Find an Employee (By EID)')
        print('4. Delete an Employee')
        print('5. Display Statistics')
        print('6. Exit')
        menu=int(input('Enter your choice: '))
        if(menu==1):
            Name=input('Name:').capitalize()
            Employee_ID=input('Employee_ID: ')
            Department=input('Department: ')
            Title=input('Title:')
            Salary=input('Salary:')
            user_dir=add_employee(user_dir, Name, Employee_ID, Department, Title, Salary)
        elif(menu==2):
            Name=input('Name: ').capitalize()
            search_name(user_dir, Name)
        elif(menu==3):
            id=input('Please enter the employee ID to search: ')
            search_id(user_dir, id)
        elif(menu==4):
            Name=input('Name:')
            user_dir=delete_employee(user_dir, Name)
        elif(menu==5):
            show_stats(user_dir)
        else:
            save_data(user_dir)
            break

main()
