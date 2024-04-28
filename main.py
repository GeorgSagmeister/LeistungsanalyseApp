
from datetime import datetime
from my_classes import Subject, Experiment, Supervisor

print()
print("Welcome to the experiment builder!")
print("Please enter the following information about the experiment")
print()
check = input("Do you want to use the current date? (y/n): ")
if check == "y":
    experiment_date = datetime.now().strftime("%d-%m-%Y")
elif check == "n":
    experiment_date = input("Enter the date(dd-mm-yyyy): ")
else:
    print("Please enter a valid input!")


#Subject
print("Enter the following information about the subject")
print()
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
birthdate = input("Enter the birthdate (%Y-%m-%d): ")
sex = input("Sex of the subject (male/female): ")

#Expermient
experiment_name = input("Enter the experiment name: ")
supervisor_first = input("Enter the supervisor's first name: ")
supervisor_last = input("Enter the supervisor's last name: ")

subject = Subject(first_name, last_name, sex, birthdate)
supervisor = Supervisor(supervisor_first, supervisor_last)
experiment = Experiment(experiment_name, experiment_date, supervisor, subject)
        
subject.save()
experiment.save()
