import json
from datetime import datetime

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def save(self):
        with open(f"{self.last_name}.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Person saved to"f"{self.last_name}.json")

class Subject(Person):
    def __init__(self, fist_name, last_name, sex, birthdate):
        super().__init__(fist_name,last_name)
        self.sex = sex
        self.__birthdate = birthdate
        self.max_hr = self.estimate_max_hr()

    def estimate_max_hr(self):

        birthdate = datetime.strptime(self.__birthdate, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month,birthdate.day))

        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * age
            return max_hr_bpm
        else:
            max_hr_bpm = 226 - 1.0 * age
            return max_hr_bpm

class Supervisor(Person):
    def __init__(self,fist_name,last_name):
        super().__init__(fist_name,last_name)

class Experiment():
    
    def __init__(self,experiment_name,experiment_date,supervisor):

        self.experiment_name = experiment_name
        self.experiment_date = experiment_date
        self.supervisor = supervisor.__dict__
    
    def save(self):
        with open(f"{self.experiment_name}_experiment.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Experiment saved to"f"{self.experiment_name}.json")

                 

