import json

class Person():

    def __init__(self,first_name,last_name,sex,age):

        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = self.estimate_max_hr()
        
    
    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
            return max_hr_bpm
        else:
            max_hr_bpm = 226 - 1.0 *  self.age
            return max_hr_bpm

    def save(self):
        with open(f"{self.last_name}.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Experiment saved to"f"{self.last_name}.json")

class Experiment():
    
    def __init__(self,experiment_name,experiment_date,supervisor):

        self.experiment_name = experiment_name
        self.experiment_date = experiment_date
        self.supervisor = supervisor
    
    def save(self):
        with open(f"{self.experiment_name}_experiment.json","w") as outfile:
            json.dump(self.__dict__, outfile, indent=4)
            print("Experiment saved to"f"{self.experiment_name}.json")


person1 = Person("Alexander", "Kometer", "male", 27)
experiment1 = Experiment("Experiment1", "12-12-2020", "Wampe")

person1.save()
experiment1.save()
                 

