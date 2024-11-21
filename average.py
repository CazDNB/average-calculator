import os

grades = []

def add_grade():
    grade = input('Input your grade: \n')
    try:
        grade = int(grade)
        if grade > 0:
            print(f'You added {grade}')
            grades.append(grade)
        else: 
            print('The number must be above 0')
        
    except:
        print('Please input a valid grade. \n')
        


def see_grades():
    for x in grades:
        print(x)

def average_caclulate():
    average = sum(grades) / len(grades)
    print (f'{average:.2f}')
    



def menu():
    print('''
***************************************
**** Welcome to the grade averager ****
***************************************
          
Please select an option:

(1) Add grades
(2) See Grades added
(3) Calculate average grade
(0) Exit
''')

menu()

option = (input('Select an option: '))

while option != '0':
    if option == '1':
        add_grade()
    elif option == '2':
        see_grades()
        os.system('pause')
    elif option == '3':
        average_caclulate()
    else:
        print("Please press 1, 2, 3 or 0\n")
        print()
    
    print()
    menu()
    option = (input('Select an option: '))

print('Thanks for using my program! Goodbye!')
os.system('pause')
os.system('cls')