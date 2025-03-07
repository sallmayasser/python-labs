import os
import re
from datetime import datetime

# users = [{"email": "salma@gmail.com", "password": "123456789"},{"email": "yasser@gmail.com", "password": "123456789"}]

# projects = [
# {'title': "project1", 'details': "here is project1", "target": 100000, "created_by": 'salma@gmail.com', "start_date": "03-06-2025", "end_date": "10-06-2025"},
# {'title': "project2", 'details': "here is project2", "target": 500000, "created_by": 'yasser@gmail.com', "start_date": "03-07-2025", "end_date": "10-07-2025"}
# ]


users = []
projects = []
logged_user = ""
format = "%d-%m-%Y"
today = datetime.today().date()


def register():

    mobile_regex = r'^(010|011|012|015)\d{8}$'
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    while True:
        first_name = input("Enter you first name: ").strip().lower()
        if first_name.isalpha():
            break
        else:
            print("Please enter valid first name")

    while True:
        last_name = input("Enter you last name: ").strip().lower()
        if last_name.isalpha():
            break
        else:
            print("Please enter valid last name")

    while True:
        email = input("Enter your Email: ").strip().lower()

        if not re.match(email_regex, email):
            print("Please enter a valid email address.")
            continue

        if any(user['email'] == email for user in users):
            print("This email already exists. Please try a different one.")
            continue

        break

    while True:
        mobile = input("Enter you Mobile:").strip()
        if re.match(mobile_regex, mobile):
            break
        else:
            print("Please enter valid mobile number")

    while True:
        password = input("Enter your password: ").strip()
        if len(password) > 8:
            break
        else:
            print("password length must be at least 8 char")

    while True:
        confirm_password = input("Enter your confirm password: ").strip()
        if password == confirm_password:
            break
        else:
            print("confirm password doesn't match the password")

    users.append({'firstName': first_name,
                 'lastName': last_name,
                  'email': email,
                  'mobile': mobile,
                  'password': password})


def login():
    global logged_user
    while True:
        print("Welcome to the login page!\n")
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        while True:
            email = input("Enter you Email:").strip().lower()
            if re.match(email_regex, email):
                break
            else:
                print("Please enter valid Email")

        password = input("Enter your password: ").strip()

        for user in users:
            if user['email'] == email and user['password'] == password:
                logged_user = user['email']
                return user

        print("\n**invalid email or password!**")
        choice = input(
            "\nDo you want to go back to main menu ? [y] for Yes & [any key] for No :\n").lower()
        if choice == "y":
            os.system("clear")
            break

        os.system("clear")


def logout():
    global logged_user
    logged_user = None
    print(" You have successfully logout ")


def add_start_date(format, today):
    while True:
        try:
            start = input("Enter the start date in format [DD-MM-YYYY] ")
            start_date = datetime.strptime(start, format).date()
            if start_date < today:
                print(
                    "Invalid date. The selected date must be today or a future date. Please enter a valid date.")
            else:
                return start_date.strftime(format)

        except ValueError:
            print("Invalid date format! Please try again.")


def add_end_date(format, start_date):
    while True:
        try:
            end = input("Enter the end date in format [DD-MM-YYYY] ")
            end_date = datetime.strptime(end, format).date()
            start_date_obj = datetime.strptime(start_date, format).date()
            if end_date < start_date_obj:
                print(
                    "Invalid date. The end date must be after start date. Please enter a valid date.")
            else:
                return end_date
        except ValueError:
            print("Invalid date format! Please try again.")


def add_target():
    while True:
        target = input('Enter total target: ').strip().lower()
        if target.isdigit() and int(target) > 0:
            target = int(target)
            break
        else:
            print('Please enter valid target ')
    return target


def create_project():

    print("Welcome to the create project page!")

    title = input('Enter the project title : ').strip().lower()
    details = input('Enter the project details : ').strip().lower()
    target = add_target()
    start_date = add_start_date(format, today)
    end_date = add_end_date(format, start_date)

    projects.append({"title": title,
                     "details": details,
                     "target": target,
                     "start_date": start_date,
                     "end_date": end_date,
                     "created_by": logged_user})


def to_string(project):
    print(
        f"Project Title: {project['title']} \nProject Details: {project['details']} \nProject Total Target is : {project['target']} \nStarted At:{project['start_date']} \nEnds At :{project['end_date']}\n   ")
    print("*"*50)


def view_projects():
    print("Welcome to all projects Page !")
    for project in projects:
        to_string(project)
    while True:
        choice = input(
            "\nDo you want to go back to main menu ? [y] for Yes & [any key] for No :\n").lower()
        if choice == "y":
            os.system('clear')
            break


def view_my_projects():
    print("Your Projects Page")
    print("-"*25)
    for project in projects:
        if logged_user == project['created_by']:
            to_string(project)
        else:
            continue

    while True:
        choice = input(
            "\nDo you want to go back to main menu ? [y] for Yes & [any key] for No :\n").lower()
        if choice == "y":
            os.system('clear')
            break


def edit_project():
    print("Welcome in Edit page \n")
    print("*"*25)
    titles = [project['title']
              for project in projects if logged_user == project['created_by']]
    while True:
        print("Please enter the project number to edit it:")
        print("-"*50)
        for index, title in enumerate(titles):
            print(f"{index+1}. {title}")
        choice = input('\nEnter your choice: ').strip().lower()
        if not choice.isdigit() or int(choice) > len(titles):
            os.system('clear')
            print('**Please enter valid number***')
            continue
        else:
            os.system('clear')
            opened_project = projects[int(choice)-1]
            while True:
                print("\nEnter the number of field you want to change")
                print("-"*50)
                print('1. Project Title')
                print('2. Project Details')
                print('3. Project Target')
                print('4. Project Start Date')
                print('5. Project End Date')
                option = input('\nEnter your choice: ').strip().lower()
                os.system('clear')
                match option:
                    case '1':
                        opened_project['title'] = input(
                            "Enter the New title :")
                    case '2':
                        opened_project['details'] = input(
                            'Enter the New Details :')
                    case '3':
                        opened_project['target'] = add_target()
                    case '4':
                        opened_project['start_date'] = add_start_date(
                            format, today)
                    case '5':
                        opened_project['end_date'] = add_end_date(
                            format, opened_project['start_date'])

                flag = input(
                    '\nDo you want to Edit other field ? [y/Y] for Yes and [any key ] for No :') .strip().lower()
                if flag != "y":
                    break
            os.system('clear')
            break


def delete_project():
    print("Welcome in Delete project page \n")
    print("*"*25)
    titles = [project['title']
              for project in projects if logged_user == project['created_by']]
    while True:
        print("Please enter the project number you want to Delete :")
        print("-"*50)
        for index, title in enumerate(titles):
            print(f"{index+1}. {title}")
        choice = input('\nEnter your choice: ').strip().lower()
        if not choice.isdigit() or int(choice) > len(titles):
            os.system('clear')
            print('**Please enter valid number***')
            continue
        else:
            os.system('clear')
            projects.pop(int(choice)-1)
        break


def search_Project():
    print("Welcome in Search page ")
    print("-"*30)
    while True:
        try:
            search_input = input(
                "\nEnter a date in format [DD-MM-YYYY]: ").strip()
            print("\n")
            search_date = datetime.strptime(
                search_input, format).strftime(format)
            found = False

            for project in projects:
                if project['start_date'] == search_date or project['end_date'] == search_date:
                    to_string(project)
                    found = True

            if not found:
                print("No projects found with the given date.")

        except ValueError:
            print("Invalid date format! Please try again.")

        flag = input(
            '\nDo you want to Search for other field ? [y/Y] for Yes and [any key ] for No :') .strip().lower()
        if flag != "y":
            break


def project_form():
    while True:
        print("Please choose an option from the menu below:")
        print("-"*50)
        print('1. Create Project')
        print('2. View All Projects')
        print('3. View My Projects')
        print('4. Edit Project')
        print('5. Delete Project')
        print('6. Search Project')
        print('7. Logout')
        print('8. Exit')
        choice = input('\nEnter your choice: ').strip().lower()
        match choice:
            case '1':
                os.system('clear')
                create_project()
                os.system('clear')
            case '2':
                os.system('clear')
                view_projects()
            case '3':
                os.system('clear')
                view_my_projects()
            case '4':
                os.system('clear')
                edit_project()
            case '5':
                os.system('clear')
                delete_project()
            case '6':
                os.system('clear')
                search_Project()
            case '7':
                os.system('clear')
                logout()
                break
            case '8':
                os.system('clear')
                break
            case _:
                os.system('clear')
                print('***Invalid choice please choose from previous menu***\n')


while (True):
    print('\nCrowd-Funding console app')
    print('-'*25)
    print('1. Register')
    print('2. Login')
    print('3. Exit')

    choice = input('\nEnter your choice: ').strip().lower()

    match choice:
        case '1':
            os.system('clear')
            register()
            os.system('clear')
            print("You have successfully registered!")

        case '2':
            os.system('clear')
            user = login()
            if user:
                os.system('clear')
                project_form()
        case '3':
            os.system('clear')
            print("Thank you for using the crowd funding app!")
            break
        case _:
            os.system('clear')
            print('***Invalid choice please choose from previous menu***\n')
