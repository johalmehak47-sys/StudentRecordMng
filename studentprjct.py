class Student:
    def __init__(self):
        self.rolln=0
        self.name=""
        self.age=0
        self.course=""
        self.cgpa=0.0

    def set_details(self):
        self.rolln = int(input("enter roll number of student : "))
        self.name = str(input("enter name of the student : "))
        self.age = int(input("enter age of the student : "))
        self.course = str(input("enter the course name : "))
        self.cgpa = float(input("enter the cgpa : "))
        print("details input sucessfull.")



students=[] #global list for students whose details were fetched 

def load_students():
    try:
        with open("students.txt","r") as f:
            for line in f :
                data = line.strip().split("|")
                st = Student()
                st.rolln = int(data[0])
                st.name=str(data[1])
                st.age=int(data[2])
                st.course=str(data[3])
                st.cgpa=float(data[4])
                students.append(st)
        print("fetching successfull.")
    except FileNotFoundError :
        print("File does not exists ! ")


def save_students():
    with open("students.txt","w") as f:
        for st in students:
            line=f"{st.rolln}|{st.name}|{st.age}|{st.course}|{st.cgpa}\n"
            f.write(line)


def add_student():
    roll = int(input("enter roll number of the new student : "))
    for st in students :
        if st.rolln == roll :
            print("student with this roll number already exists ! ")
            return
    st = Student()
    st.rolln = roll
    st.name = str(input("enter name of the student : "))
    st.age = int(input("enter age of the student : "))
    st.course = str(input("enter the course name : "))
    st.cgpa = float(input("enter the cgpa : "))
    students.append(st)
    save_students()
    print("details input sucessfull.")

def viewall():
    if(len(students)==0):
        print("record is empty.")
        return
    
    for st in students:
        print(f"Roll no = {st.rolln}, Name = {st.name}, Age = {st.age}, Course = {st.course}, Cgpa = {st.cgpa}" )


def search_by_roll():
    roll = int(input("enter roll number of the student to search : "))
    for st in students:
        if st.rolln == roll :
            print("student found ! ")
            print("details are as follows : ")
            print(f"Roll no = {st.rolln}, Name = {st.name}, Age = {st.age}, Course = {st.course}, CGPA = {st.cgpa}" )
            return
        
    print("Not found !")

def delete_student():
    if len(students)==0:
        print("record is empty ! ")
        return

    roll = int(input("Enter roll number to delete : "))
    for st in students:
        if st.rolln == roll:
            students.remove(st)
            save_students()
            print("deletion sucessfully.")
            return
    
    print("Not found.")

def update_details():
    if len(students)==0:
        print("record empty !")

    roll=int(input("enter roll number whose details are to be modified : "))
    for st in students:
        if st.rolln == roll:
            print("select the data which is to be modified - ")
            print("1. roll number ")
            print("2. name ")
            print("3. age ")
            print("4. course ")
            print("5. cgpa ")
            choice = int(input("enter choice : "))
            if(choice==1):
                newr = int(input("enter new roll number : "))
                st.rolln = newr
                save_students()
                return

            elif(choice==2):
                newn = str(input("enter new name : "))
                st.name = newn
                save_students()
                return
            elif(choice==3):
                nage = int(input("enter new age : "))
                st.age = nage
                save_students()
                return

            elif(choice==4):
                ncourse = str(input("enter new course name : "))
                st.course = ncourse
                save_students()
                return
            elif(choice ==5):
                ncg = float(input("enter new cgpa : "))
                st.cgpa = ncg
                save_students()
                return
    print("invalid choice ! ")

def sort_by_cg():
    if len(students)==0:
        print("record empty.")
        return
    
    students_sorted = sorted(students,key=lambda st: st.cgpa, reverse=True)
    print("sorted students by cgpa (high to low )")
    for st in students_sorted:
        print(f"Roll number= {st.rolln}, Name= {st.name}, Age= {st.age}, Course = {st.course}, CGPA= {st.cgpa}")


def countstudents():
    if len(students)==0:
        print("record empty ! ")
        return
    print("Total students = ",len(students))

def menu():
    print("1. Add student.")
    print("2. View all students.")
    print("3. Search student by roll number.")
    print("4. Update student details.")
    print("5. Delete Student.")
    print("6. Sort students by CGPA.")
    print("7. Count total students.")
    print("8. Exit.")

def main():
    load_students()
    while True:
        menu()

        try :
            inp = int(input("Enter choice : "))
            if inp==1:
                add_student()
            elif inp==2:
                viewall()
            elif inp==3:
                search_by_roll()
            elif inp==4:
                update_details()
            elif inp==5:
                delete_student()
            elif inp==6:
                sort_by_cg()
            elif inp==7:
                countstudents()
            elif inp==8:
                print("exiting ")
            else :
                print("enter valid number ! ")

        except ValueError:
            print("Invalid choice ! ")

        except Exception as e:
            print("An error occured : {e}")


if __name__ == "__main__":
    main()




