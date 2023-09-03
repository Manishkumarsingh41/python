timetable = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": []
}

def add_subject(day, subject_name, time):
    timetable[day].append((subject_name, time))

def display_timetable():
    for day, subjects in timetable.items():
        print(day)
        for subject in subjects:
            subject_name, time = subject
            print(f"- {subject_name}: {time}")

def time_management():
    available_time = input("Enter your available time: ")
    

# Example usage
add_subject("Monday", "Math", "9:00 AM - 10:30 AM")
add_subject("Monday", "Science", "10:45 AM - 12:15 PM")
display_timetable()
time_management()
