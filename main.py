import json
from datetime import datetime
from my_classes import Person, Experiment 

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

#subject:
print("Enter the following information about the subject")
print()
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
age = int(input("Enter the age: "))
sex = input("Sex of the subject (male/female): ")

#Expermient
experiment_name = input("Enter the experiment name: ")
supervisor = input("Enter the supervisor's name: "),

subject = Person(first_name,last_name,sex,age)
experiment = Experiment(experiment_name,experiment_date,supervisor)
        
subject.save()
experiment.save()


