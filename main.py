import my_functions
import json
from datetime import datetime



if __name__ == "__main__":

   # Datum fixieren
    datum =  datetime.now().strftime("%d-%m-%Y")

    # Experimentenname
    name = input("Experimentenname:")
    
    # Erstelle einen Betreuer
    supervisor_info = my_functions.build_person("Georg", "sagmeister", "male", 20)

    # Erstelle einen Probanden
    print("Bitte Daten der Versuchsperson eingeben:")
    first_name = input("Vorname:")
    last_name = input("Nachname:")
    sex = input("Geschlecht (male or female):")
    age = int(input("Alter:"))

    subject_info = my_functions.build_person(first_name, last_name, sex, age)

    # Erstelle ein Experiment
    experiment_info = my_functions.build_experiment(name,datum, supervisor_info, subject_info)
    print(experiment_info)

    # Drucke das Experimenten-Dictionary
    print("Experiment Details:")
    for key, value in experiment_info.items():
        print(f"{key}: {value}")


    # Define student_details dictionary
    student_details ={ 
        "Experimentenname" : name, 
        "Experimentendatum": datum, 
        "Diagnostiker": supervisor_info,
        "Versuchsperson": subject_info
        } 

    # Convert and write JSON object to file
    with open("sample.json", "w") as outfile: 
        json.dump(student_details, outfile)