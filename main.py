import my_functions

if __name__ == "__main__":
    # Erstelle einen Betreuer
    supervisor_info = my_functions.build_person("John", "Doe", "male", 40)

    # Erstelle einen Probanden
    subject_info = my_functions.build_person("Jane", "Doe", "female", 35)

    # Erstelle ein Experiment
    experiment_info = my_functions.build_experiment("Heart Rate Study", "2024-03-19", supervisor_info, subject_info)

    # Drucke das Experimenten-Dictionary
    print("Experiment Details:")
    for key, value in experiment_info.items():
        print(f"{key}: {value}")
