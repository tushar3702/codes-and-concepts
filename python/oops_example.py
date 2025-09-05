# Python OOP Example
class Student:
    # Class variable (shared by all instances)
    school_name = "ABC High School"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance variables (unique to each object)
        self.name = name
        self.age = age
        # Object counter
        Student.student_count += 1

    # Static variable (counter for students)
    student_count = 0

    # Instance method
    def display_info(self):
        print(f"Student Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

    # Class method
    @classmethod
    def get_student_count(cls):
        print(f"Total Students: {cls.student_count}")

    # Static method
    @staticmethod
    def school_announcement():
        print("Welcome to ABC High School!")


# Create objects
student1 = Student("Alice", 15)
student2 = Student("Bob", 16)

# Access instance method
student1.display_info()
student2.display_info()

# Access class method
Student.get_student_count()

# Access static method
Student.school_announcement()

# Access class variable
print(f"School Name (from object): {student1.school_name}")
