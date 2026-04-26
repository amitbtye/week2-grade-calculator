# Student Grade Calculator
# Name: Amit

def calculate_grade(avg):
    if avg >= 90:
        return 'A', 'Excellent! Keep it up!'
    elif avg >= 80:
        return 'B', 'Very Good!'
    elif avg >= 70:
        return 'C', 'Good effort!'
    elif avg >= 60:
        return 'D', 'Needs Improvement'
    else:
        return 'F', 'Failed! Study more.'

def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100!")
        except ValueError:
            print("Invalid input! Enter numbers only.")

def main():
    students = []

    print("="*50)
    print(" STUDENT GRADE CALCULATOR")
    print("="*50)

    # number of students
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("Enter positive number!")
        except:
            print("Invalid input!")

    # input data
    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        
        name = input("Enter name: ")
        while name.strip() == "":
            print("Name cannot be empty!")
            name = input("Enter name: ")

        math = get_valid_marks("Math")
        science = get_valid_marks("Science")
        english = get_valid_marks("English")

        avg = (math + science + english) / 3
        grade, comment = calculate_grade(avg)

        students.append({
            "name": name,
            "avg": avg,
            "grade": grade,
            "comment": comment
        })

    # display results
    print("\n" + "="*50)
    print(" RESULTS SUMMARY")
    print("="*50)
    print(f"{'Name':<20} {'Avg':<10} {'Grade':<10} Comment")
    print("-"*60)

    for s in students:
        print(f"{s['name']:<20} {s['avg']:<10.2f} {s['grade']:<10} {s['comment']}")

    # statistics
    averages = [s['avg'] for s in students]
    print("\n" + "="*50)
    print(" CLASS STATISTICS")
    print("="*50)

    print(f"Total Students: {len(students)}")
    print(f"Class Average: {sum(averages)/len(averages):.2f}")
    print(f"Highest: {max(averages):.2f}")
    print(f"Lowest: {min(averages):.2f}")

    # save to file
    with open("results_sample.txt", "w") as f:
        for s in students:
            f.write(f"{s['name']} - {s['avg']:.2f} - {s['grade']} - {s['comment']}\n")

    print("\nResults saved to results_sample.txt")
    print("\nThank you for using the Grade Calculator!")

main()
