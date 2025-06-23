
student_name = input("Enter student name: ")
class_no = input("Enter class: ")


print("Enter marks for the following subjects:")
subjects = ["Hindi", "Maths", "English", "CPP", "DSA"]
marks = []

for subject in subjects:
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


total_marks = sum(marks)
percentage = (total_marks / 500) * 100


print("\n--- Student Result ---")
print(f"Name",f" {student_name.strip()}",sep="     : ")
print(f"Class    : {class_no}")
if percentage<33:
    print("FAil")
print(f"Percentage: {percentage:.3f}%")
