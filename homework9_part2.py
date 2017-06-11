
import pickle
def load_data():
    try:
        filename = open('employee_pickle.dat', 'rb')
        user_dir = pickle.load(filename)
        print('Opened Pickles')
        filename.close()
        return user_dir
    except FileNotFoundError:
        print('Loading Failed. Creating new file.')
        return {}
        
def show_stats(user_dir):
    dept_temp={}
    emp_count = 0
    for k,v in user_dir.items():
        dep_name = user_dir[k]['Department']

        if dep_name in dept_temp:
            dept_temp[dep_name]['count']+=1
        else:
            dept_temp[dep_name] = {'count': 1}

        emp_count += 1
    for k,v in dept_temp.items():
        print('Department {} has {} employees'.format(k, v['count']))
    print('The company has',emp_count,'employees.')

    
def add_employee(user_dir, Name, Employee_ID, Department, Title, Salary):
    if Name in user_dir:
        print("This employee already exists.")
    if Employee_ID in user_dir:
        print('This EID is already in use.')
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
        try:
            print('1. Add an Employee')
            print('2. Find an Employee (By Name)')
            print('3. Find an Employee (By EID)')
            print('4. Delete an Employee')
            print('5. Display Statistics')
            print('6. Exit')
            menu=int(input('Enter your choice: '))
            if(menu==1):
                Name=input('Name: ').capitalize()
                Employee_ID=input('Employee_ID: ')
                Department=input('Department: ')
                Title=input('Title: ')
                Salary=input('Salary: ')
                user_dir=add_employee(user_dir, Name, Employee_ID, Department, Title, Salary)
            elif(menu==2):
                Name=input('Name: ').capitalize()
                search_name(user_dir, Name)
            elif(menu==3):
                id=input('Please enter the employee ID to search: ')
                search_id(user_dir, id)
            elif(menu==4):
                Name=input('Name: ')
                user_dir=delete_employee(user_dir, Name)
            elif(menu==5):
                show_stats(user_dir)
            else:
                save_data(user_dir)
                break
        except ValueError:
            print('Incorrect value, please try again.')
    
main()
