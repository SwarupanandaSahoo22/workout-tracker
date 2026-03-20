# Grade Tracker
def add_student(students, school):
    name = input("Enter your name: ")
    marks = int(input("Enter your marks: "))
    sub = input("Enter subject: ")

    student = {
        "name" : name,
        "school" : school,
        "marks" : marks,
        "subject" : sub
    }

    students.append(student)
    print("Student added successfully!")

def find_highest(subjects):
    if not subjects:
        return None
    
    highest = subjects[0]
    
    for sub in subjects:
        if sub["marks"] > highest["marks"]:
            highest = sub
    
    return highest



def main():
    name = input("Enter student name: ").capitalize()
    school = input("Enter school name: ").capitalize()
    student = {
        "name" : name,
        "school" : school,
        "subjects" : []    
    }
    is_running = True

    while is_running:
        print("--------------------")
        print("Your Grade Tracker")
        print("--------------------")
        print("1. Add subject")
        print("2. Show subjects")
        print("3. Show total marks")
        print("4. Show highest mark")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            subject = input("Enter subject name: ")
            marks = int(input("Enter marks: "))
            
            student["subjects"].append({
                "subject" : subject,
                "marks" : marks
            })

            print("Subject added successfully!")

        elif choice == "2":
            if not student["subjects"]:
                print("No subjects added yet.")
            else:
                print("\n" + "-" * 35)
                print(f"STUDENT: {student['name']}")
                print(f"SCHOOL : {student['school']}")
                print("-" * 35)
                print(f"{'Subject':<15} | {'Marks':>5}")
                print("-" * 35)

                for sub in student["subjects"]:
                    print(f"{sub['subject']:<15} | {sub['marks']:>5}")

                print("-" * 35)

        elif choice == "3":
            if not student["subjects"]:
                print("No subjects added yet.")
            else:
                total = 0

                for sub in student["subjects"]:
                    total += sub["marks"]

                number_of_subjects = len(student["subjects"])
                percentage = (total / (number_of_subjects * 100)) * 100


                print("--------------- TOTAL MARKS ---------------")
                print("Total marks: 500")
                print(f"Marks secured: {total}")
                print(f"Percentage: {percentage:.2f}%")
                print("--------------------------------------------")

        elif choice == "4":
            highest = find_highest(student["subjects"])
            if highest:
                print(f"Highest: {highest["subject"]} - {highest["marks"]}")
            else:
                print("No subjects added yet.")

        elif choice == "5":
            is_running = False

        else:
            print("Invalid choice")
        
    print("Have a nice day!")


if __name__ == "__main__":
    main()