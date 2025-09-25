# part 1 code and variables
student_name = "Shikel Percell"
current_gpa = 3.5  # My irl stats I think
study_hours = 25
social_points = 50
stress_level = 70

print("=== Welcome to the Acedemic game with your host: Shikel ===")
print(f"Student Name: {student_name}")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}/100")

# Part 2 code and variables
print("=== PArt 2: Courses ===")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    if current_gpa <= 2.5:
        study_hours += 2
        stress_level -= 5
        print("Light load chosen. Lower stress, more free time.")
    else:
        print("Light load chosen. Balanced semester ahead.")

elif choice == "B":
    if current_gpa >= 2.6 and current_gpa <= 3.4:
        study_hours += 3
        stress_level += 5
        print("Standard load chosen. Moderate challenge.")
    else:
        print("Standard load chosen. No major changes.")

elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 6
        stress_level += 15
        print("Heavy load chosen. High GPA allows tough challenge.")
    else:
        stress_level += 20
        print("Heavy load chosen without high GPA. Risk of burnout!")

else:
    print("Invalid input. No course load assigned.")

# part 3 code and variables
print("=== Step 3: Study Strategy Decision ===")

study_options = ["Programming", "Math", "English", "History"]
print("Choose a study focus area from the following options:")
print(study_options)

user_choice = input("Enter your choice: ")

if user_choice in study_options:
    print(f"You chose {user_choice} as your study focus.")

    if user_choice == "Programming" and study_hours > 20:
        current_gpa += 0.2
        social_points -= 5
        print("Extra programming boosted your GPA but cost social time.")

    elif user_choice == "Math" and stress_level < 50:
        current_gpa += 0.1
        print("Math focus raised GPA due to manageable stress.")

    elif user_choice == "English" or user_choice == "History":
        social_points += 5
        print("Studying English/History improved social points.")

    if not (user_choice == "Programming"):
        print("You did not choose Programming.")

else:
    print("Invalid choice! That subject is not in the study options.")

# part 4 variables and code
print("=== Step 4: Final Semester Assessment ===")

if current_gpa >= 3.5:
    if stress_level < 50:
        print("Excellent! You maintained high GPA and low stress. You have achieved the Nerd Ending!")
    else:
        print("Great GPA but stress was too high. You have achieved the Stressed Ending!")
elif current_gpa >= 2.5:
    if social_points > 60:
        print("Balanced outcome: Solid GPA and strong social life. You have achieved the Balanced Ending!")
    else:
        print("Decent GPA but social life suffered. Work on balance. You have achieved the Lonely Ending!")
else:
    if stress_level > 70:
        print("Struggling: Low GPA and high stress. You have achieved the Mediocore Ending!")
    else:
        print(
            "Your GPA dropped, but stress is manageable. Try again next semester. You have achieved the Failure Endning")

print("\n=== Final Statistics ===")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}/100")















