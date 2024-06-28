import os
import datetime
from statistics import mean

def assess_mood():
    moods = {"happy": 2, "relaxed": 1, "apathetic": 0, "sad": -1, "angry": -2}
    data_directory = "data"
    file_path = os.path.join(data_directory, "mood_diary.txt")
    date_today = datetime.date.today()
    date_today = str(date_today)

    if os.path.exists(file_path):
        file = open(file_path, 'r')
        attempted = [line for line in file if line.startswith(date_today)]
        
        if attempted:
            print("Sorry, you have already entered your mood today.")
            return

    current_mood = input("Enter your current mood: ").strip().lower()
    if current_mood not in moods:
        return

    mood_value = moods[current_mood]
    
    file = open(file_path, 'a')
    file.write(f"{date_today} {mood_value}\n")
    
    file = open(file_path, 'r')
    lines = file.readlines()
    
    if len(lines) < 7:
        return
    
    mood_values = [int(line.strip().split()[1]) for line in lines[-7:]]
    
    average_mood = round(mean(mood_values))

    if mood_values.count(2) >= 5:
        diagnosis = "Manic"
    elif mood_values.count(-1) >= 4:
        diagnosis = "Depressive"
    elif mood_values.count(0) >= 6:
        diagnosis = "Schizoid"
    else:
        if average_mood == 2:
            diagnosis = "Happy"
        elif average_mood == 1:
            diagnosis = "Relaxed"
        elif average_mood == 0:
            diagnosis = "Apathetic"
        elif average_mood == -1:
            diagnosis = "Sad"
        elif average_mood == -2:
            diagnosis = "Angry"

    print(f"Your diagnosis: {diagnosis.capitalize()}!")