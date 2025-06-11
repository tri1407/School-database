import json
class Student:
    def __init__(self, name, gender, birthdate, student_id):
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.student_id = student_id
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def get_average(self):
        if not self.grades:
            return 0
        return round(sum(self.grades) / len(self.grades), 1)
    def display_info(self):
        print(f"Tên: {self.name}")
        print(f"Giới tính: {self.gender}")
        print(f"Ngày sinh: {self.birthdate}")
        print(f"Mã số học sinh: {self.student_id}")
        print(f"Điểm trung bình: {self.get_average()}")
    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "birthdate": self.birthdate,
            "student_id": self.student_id,
            "grades": self.grades
        }
    @classmethod
    def from_dict(cls, data):
        student = cls(data['name'], data['gender'], data['birthdate'], data['student_id'])
        student.grades = data['grades']
        return student
class Classroom:
    def __init__(self, class_name, teacher):
        self.class_name = class_name
        self.students = []
        self.teacher = teacher
    def add_student(self, new_student):
        for student in self.students:
            if student.student_id.strip() == new_student.student_id.strip():
                print("Mã số học sinh này đã tồn tại!")
                return
        self.students.append(new_student)
        print(f"Đã thêm học sinh {new_student.name}.")
    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Đã xóa học sinh {student.name}")
                return
        print("Mã số học sinh này không tồn tại!")
    def get_class_average(self):
        if not self.students:
            return 0
        total_average = sum(student.get_average() for student in self.students)
        return round(total_average / len(self.students), 1)
    def find_student(self, name):
        for student in self.students:
            if student.name.lower().strip() == name.lower().strip():
                print(f"Đã tìm thấy học sinh {name}.")
                while True:
                    print(f"\n=== {student.name.upper()} ===")
                    print("1. Thêm điểm")
                    print("2. Xóa điểm")
                    print("3. Hiển thị danh sách điểm")
                    print("4. Hiển thị thông tin học sinh")
                    print("5. Thoát")
                    choice = input("Chọn chức năng: ")
                    if choice == "1":
                        try:
                            grade = float(input("Nhập số điểm: "))
                            student.add_grade(grade)
                            print(f"Đã thêm điểm {grade} vào danh sách điểm.")
                        except:
                            print("Số điểm không hợp lệ!")
                    elif choice == "2":
                        print("\n1. Xóa điểm gần nhất")
                        print("2. Xóa tất cả")
                        print("3. Thoát")
                        choice = input("Chọn chức năng: ")
                        if choice == "1":
                            self.grades.pop()
                        elif choice == "2":
                            self.grades.clear()
                        elif choice == "3":
                            pass
                        else:
                            print("Lựa chọn không hợp lệ!")
                    elif choice == "3":
                        print(f"Danh sách điểm: {student.grades}")
                    elif choice == "4":
                        student.display_info()
                    elif choice == "5":
                        break
                return
        print(f"Không tìm thấy học sinh {name}!")
    def get_students_list(self):
        if not self.students:
            print("Danh sách học sinh trống!")
            return
        print("Danh sách học sinh:")
        for student in self.students:
            print(student.name)
    def display_class_info(self):
        print(f"Tên lớp: {self.class_name}")
        print(f"Sĩ số: {len(self.students)}")
        print(f"Giáo viên: {self.teacher}")
        print(f"Điểm trung bình lớp: {self.get_class_average()}")
    def to_dict(self):
        return {
            "class_name": self.class_name,
            "teacher": self.teacher,
            "students": [student.to_dict() for student in self.students]
        }
    @classmethod
    def from_dict(cls, data):
        classroom = cls(data['class_name'], data['teacher'])
        classroom.students = [Student.from_dict(student) for student in data['students']]
        return classroom
class School:
    def __init__(self, school_name, headmaster):
        self.school_name = school_name
        self.headmaster = headmaster
        self.classrooms = []
    def add_classroom(self, classroom):
        for available_classroom in self.classrooms:
            if available_classroom.class_name.strip() == classroom.class_name.strip():
                print("Tên lớp đã tồn tại!")
                return
        self.classrooms.append(classroom)
        print(f"Đã thêm lớp {classroom.class_name}.")
    def remove_classroom(self, name):
        for classroom in self.classrooms:
            if classroom.class_name.strip() == name.strip():
                self.classrooms.remove(classroom)
                print(f"Đã xóa lớp {name}.")
                return
        print("Tên lớp không tồn tại!")
    def find_classroom(self, name):
        for classroom in self.classrooms:
            if classroom.class_name.strip() == name.strip():
                print(f"Đã tìm thấy lớp {classroom.class_name}.")
                while True:
                    print(f"\n=== {classroom.class_name.upper()} ===")
                    print("1. Thêm học sinh")
                    print("2. Xóa học sinh")
                    print("3. Tìm học sinh")
                    print("4. Hiển thị danh sách học sinh")
                    print("5. Hiển thị thông tin lớp")
                    print("6. Thoát")
                    choice = input("Chọn chức năng: ")
                    if choice == "1":
                        name = input("Nhập tên học sinh: ")
                        gender = input("Nhập giới tính học sinh: ")
                        birthdate = input("Nhập ngày sinh học sinh: ")
                        student_id = input("Nhập mã số học sinh: ")
                        classroom.add_student(Student(name, gender, birthdate, student_id))
                    elif choice == "2":
                        student_id = input("Nhập mã số học sinh: ")
                        classroom.remove_student(student_id)
                    elif choice == "3":
                        name = input("Nhập tên học sinh: ")
                        classroom.find_student(name)
                    elif choice == "4":
                        classroom.get_students_list()
                    elif choice == "5":
                        classroom.display_class_info()
                    elif choice == "6":
                        return
                    else:
                        print("Lựa chọn không hợp lệ!")
                return
        print("Tên lớp không tồn tại!")
    def get_classrooms_list(self):
        if not self.classrooms:
            print("Danh sách lớp trống!")
            return
        print("Danh sách lớp:")
        for classroom in self.classrooms:
            print(classroom.class_name)
    def to_dict(self):
        return {
            "school_name": self.school_name,
            "headmaster": self.headmaster,
            "classrooms": [classroom.to_dict() for classroom in self.classrooms]
        }
    @classmethod
    def from_dict(cls, data):
        school = cls(data['school_name'], data['headmaster'])
        school.classrooms = [Classroom.from_dict(classroom) for classroom in data['classrooms']]
        return school
class Area:
    def __init__(self):
        self.schools = []
    def add_school(self, name, headmaster):
        for school in self.schools:
            if school.school_name == name:
                print("Tên trường đã tồn tại!")
                return
        self.schools.append(School(name, headmaster))
        print(f"Đã thêm trường {name}.")
    def remove_school(self, name):
        for school in self.schools:
            if school.school_name == name:
                self.schools.remove(school)
                print(f"Đã xóa trường {name}.")
                return
        print("Tên trường không tồn tại!")
    def find_school(self, name):
        for school in self.schools:
            if school.school_name == name:
                while True:
                    print(f"\n=== {school.school_name.upper()} ===")
                    print("1. Thêm lớp")
                    print("2. Xóa lớp")
                    print("3. Tìm lớp")
                    print("4. Hiển thị danh sách các lớp")
                    print("5. Thoát")
                    choice = input("Chọn chức năng: ")
                    if choice == "1":
                        class_name = input("Nhập tên lớp: ")
                        teacher = input("Nhập tên giáo viên: ")
                        school.add_classroom(Classroom(class_name, teacher))
                    elif choice == "2":
                        name = input("Nhập tên lớp: ")
                        school.remove_classroom(name)
                    elif choice == "3":
                        name = input("Nhập tên lớp: ")
                        school.find_classroom(name)
                    elif choice == "4":
                        school.get_classrooms_list()
                    elif choice == "5":
                        break
                    else:
                        print("Lựa chọn không hợp lệ!")
                return
        print("Tên trường không tồn tại!")
    def get_schools_list(self):
        if not self.schools:
            print("Danh sách các trường trống!")
            return
        print("Danh sách trường:")
        for school in self.schools:
            print(school.school_name)
    def to_dict(self):
        return {
            "schools": [school.to_dict() for school in self.schools]
        }
    @classmethod
    def from_dict(cls, data):
        area = cls()
        area.schools = [School.from_dict(school) for school in data['schools']]
        return area
def save_data(area, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(area.to_dict(), f, ensure_ascii=False, indent=4)
def load_data(filename):
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            data = json.load(f)
            return Area.from_dict(data)
    except FileNotFoundError:
        print("File không tồn tại!")
        return Area()
    except json.JSONDecodeError:
        print("File JSON bị lỗi hoặc sai định dạng!")
        return Area()
area = load_data('school_data.json')
while True:
    print("\n=== QUẢN LÝ TRƯỜNG HỌC ===")
    print("1. Thêm trường")
    print("2. Xóa trường")
    print("3. Tìm trường")
    print("4. Hiển thị danh sách các trường")
    print("5. Thoát")
    choice = input("Nhập chức năng: ")
    if choice == "1":
        school_name = input("Nhập tên trường: ")
        headmaster = input("Nhập tên hiệu trưởng: ")
        area.add_school(school_name, headmaster)
        save_data(area, 'school_data.json')
    elif choice == "2":
        school_name = input("Nhập tên trường: ")
        area.remove_school(school_name)
        save_data(area, 'school_data.json')
    elif choice == "3":
        school_name = input("Nhập tên trường: ")
        area.find_school(school_name)
        save_data(area, 'school_data.json')
    elif choice == "4":
        area.get_schools_list()
    elif choice == "5":
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng thử lại.")