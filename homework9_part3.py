# I also included a "Show All Employees" kind of section because I thought "why not add something back and hope to get a few points back for late turn in. :("
# I'm turning this in with part 2 because it's all I had time for and couldn't extend anymore. :(
# Sorry! I've also loved your class. I'm going to be pursuing python as a career choice as I move into DevOps.
# 

import pickle

class Employee(object):
    Name = None
    Employee_ID = None
    Department = None
    Title = None
    Salary = None

    def __init__(self, Name, Employee_ID, Department, Title, Salary):
        self.Name = Name
        self.Employee_ID = Employee_ID
        self.Department = Department
        self.Title = Title
        self.Salary = Salary


def load_data():
    try:
        filename = open('employee_pickle.dat', 'rb')
        user_dir = pickle.load(filename)
        print('Opened Pickles')
        filename.close()
        return user_dir
    except Exception:
        print('Loading Failed. Creating new file.')
        return {}

def show_employees(user_dir):
    for k in user_dir:
        print(user_dir[k].Name,user_dir[k].Department)


def show_stats(user_dir):
    dept_temp = {}
    dept_sal_temp = {}
    emp_count = 0
    company_salary = []
    avg_salary = 0
    for k,v in user_dir.items():
        dep_name = user_dir[k].Department
        dep_sal = user_dir[k].Salary
        company_salary.append(int(user_dir[k].Salary))
        if dep_name in dept_temp:
            dept_temp[dep_name]['count'] += 1
            dept_temp[dep_name]['salary_list'].append(int(dep_sal))
        else:
            dept_temp[dep_name] = {'count': 1, 'salary_list': [int(dep_sal)]}

        emp_count += 1
        avg_salary = sum(company_salary)/emp_count

    for k,v in dept_temp.items():
        print('{} has {} employees'.format(k, v['count']))
        print('The highest salary in {} is ${}'.format(k, max(v['salary_list'])))
        print('The lowest salary in {}  ${}'.format(k, min(v['salary_list'])))
        print('The average salary of {} is {}'.format(k, round(sum(v['salary_list'])/len(v['salary_list']))))

    print('The highest paid person in the company makes', max(company_salary))
    print('The lowest paid person in the company makes', min(company_salary))
    print('The company has',emp_count,'employees.')
    print('The average company salary is', round(avg_salary),'.')

def add_employee(user_dir, Name, Employee_ID, Department, Title, Salary):
    if Name in user_dir:
        print("This employee already exists.")

    if Employee_ID in user_dir:
        print('This EID is already in use.')

    else:
       user_dir[Name] = Employee(Name, Employee_ID, Department, Title, Salary)
       return user_dir

def search_id(user_dir, id):

    print('Displaying statistics for: ', id)
    not_found = True

    for key,values in user_dir.items():
        if values.Employee_ID == id:
            for k,v in values.__dict__.items():
                print(k,":\t", v)
            return

    print('The employee not found')

def search_name(user_dir, Name):
   if Name in user_dir:
        print('Displaying statistics for: ',Name)
        for key,values in (user_dir[Name].__dict__.items()):
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
            print('6. Display Employees')
            print('7. Exit')
            menu=int(input('Enter your choice: '))
            if(menu==1):
                Name=input('Name:').capitalize()
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
            elif(menu==6):
                show_employees(user_dir)
            elif(menu==7):
                save_data(user_dir)
                break
            else:
                print('Incorrect input, please try again!')
        except ValueError:
            print('Incorrect input. Please try again')

main()
