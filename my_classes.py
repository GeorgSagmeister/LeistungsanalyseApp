import json
import requests
from datetime import datetime

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        with open(f"{self.last_name}.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Person saved to "f"{self.last_name}.json")

    def put(self):
        url = "http://127.0.0.1:5000/person/"
        data = {
            "name": self.first_name
        }
        data_json = json.dumps(data)
        response = requests.post(url, data=data_json)
        print(response.text)

class Subject(Person):
    def __init__(self, fist_name, last_name, sex, birthdate):
        super().__init__(fist_name, last_name)
        self.sex = sex
        self.__birthdate = birthdate
        self.age = self.get_age()
        self.max_hr = self.estimate_max_hr()


    def get_age(self):
        birthdate = datetime.strptime(self.__birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = int(today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day)))
        return age

    def estimate_max_hr(self):

        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
            return max_hr_bpm
        else:
            max_hr_bpm = 226 - 1.0 * self.age
            return max_hr_bpm

    def update_email(self):

        email = str(input("Bitte email eingeben:"))
        url = "http://127.0.0.1:5000/person/Testname2"
        data = {
            "name": self.first_name,
            "email": email,
            "age": self.age
            }
        data_json = json.dumps(data)
        response = requests.put(url, data=data_json)
        print(response.text)

class Supervisor(Person):
    def __init__(self,fist_name, last_name):
        super().__init__(fist_name, last_name)

class Experiment():
    
    def __init__(self, experiment_name, experiment_date, supervisor, subject):

        self.experiment_name = experiment_name
        self.experiment_date = experiment_date
        self.supervisor = supervisor.__dict__
        self.subject = subject.__dict__
    
    def save(self):
        with open(f"{self.experiment_name}_experiment.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Experiment saved to"f"{self.experiment_name}.json")


                 

