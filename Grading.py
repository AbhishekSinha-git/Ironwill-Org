class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.total = sum(marks)
        self.percentage = self.total / len(marks)
        self.grade = self.assign_grade()

    def assign_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B'
        elif self.percentage >= 60:
            return 'C'
        elif self.percentage >= 50:
            return 'D'
        else:
            return 'F'

    def display_result(self):
        print(f"Student: {self.name}")
        print(f"Total Marks: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")
        print("-" * 30)


def main():
    num_students = int(input("Enter number of students: "))
    students = []
    
    for _ in range(num_students):
        name = input("Enter student name: ")
        marks = list(map(int, input("Enter marks for subjects (comma-separated): ").split(',')))
        students.append(Student(name, marks))
    
    print("\nStudent Results:\n" + "=" * 30)
    for student in students:
        student.display_result()


if __name__ == "__main__":
    main()
