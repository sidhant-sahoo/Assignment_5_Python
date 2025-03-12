# Task 1: Create a Dictionary of Student Marks

student_dictionary = {'Srikant': 56,'Sahil': 85,'Robin': 60,'Akhil': 33,'Atul': 52,'Alice': 96}
student_name =input("Enter the student's name: ").capitalize()
if student_name in student_dictionary:
    print("{}'s marks:".format(student_name),student_dictionary[student_name])
else:
    print(f"Student name '{student_name}' not found.")