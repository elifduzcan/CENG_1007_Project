course_codes = []
none_empty_courses = []
course_list = []
all_courses = []
while True:  # menu will work until admin enters "0"!
    print("#0 Exit from the menu. \n"
          "#1 List all courses. \n"
          "#2 List all the course that have at least one student registered. \n"
          "#3 Add a new course. \n"
          "#4 Search a course by course code. \n"
          "#5 Search a course by name. \n"
          "#6 Register a student to a course. \n"
          "#7 List all the students their registered courses. \n"
          "   (A student will be listed with a blank list even s/he has not registered for any courses.) \n"
          "#8 List top 3 most crowded courses. \n"
          "#9 List top 3 students with the most course registrations. \n")
    choice = input()

    if choice == "0":
        break

    elif choice == "1":  # lists all the courses
        with open('course.txt', 'r') as f:
            course_list1 = []
            for line in f:
                line = line.rstrip("\n")
                line_words = line.split(";")
                course_list1.append(line_words[1])
            print("The list of all courses:", course_list1)

    elif choice == "2":  # list the courses which has at least 1 student
        print("Courses that have at least one student registered:")
        with open('course.txt', 'r') as file2:
            course_list2 = []
            for line in file2:
                line = line.rstrip("\n")
                line_words = line.split(";")
                course_list2.append(line_words)
            for i in range(len(course_list2)):
                if course_list2[i][3] != "0":
                    print("- ", course_list2[i][1])

    elif choice == "3":  # adding a new course
        stop = 0
        while stop == 0:
            course_code = input("Enter course code:")
            course_name = input("Enter course name:")
            instructor = input("Enter the instructor:")

            with open("course.txt", "a") as file1:
                file1.write(course_code + ";" + course_name + ";" + instructor + ";" + "0" + "\n")
                stop = input("Enter 0 if you want to stop adding a new courses:")

    elif choice == "4":  # finds the courses by their codes
        course_code = input("Enter the code of the course you want to find:")
        with open("course.txt", "r") as file3:
            course_list3 = []
            for line in file3:
                line = line.rstrip("\n")
                line_words = line.split(";")
                course_list3.append(line_words)
            for i in range(len(course_list3)):
                if course_code in course_list3[i]:
                    print("The lesson you want to find:", course_list3[i][1])

    elif choice == "5":  # finds the courses by their name
        course_name = input("Enter the name of the course you want to find:")
        print("Courses that include the word/letter" + " ' " + course_name + " ' :")
        with open("course.txt", "r") as file4:
            course_list4 = []
            for line in file4:
                line = line.rstrip("\n")
                line_words = line.split(";")
                course_list4.append(line_words)
            for i in range(len(course_list4)):
                if course_name in course_list4[i][1]:
                    print("- ", course_list4[i][1])

    elif choice == "6":  # registering a student into a new course
        sign = 0
        while sign == 0:
            student_id = input("Enter student ID:")
            code = input("Enter the course code you want to register:")
            with open("student.txt", "r") as file6:
                course_list6 = []
                for line in file6:
                    line = line.rstrip("\n")
                    line_words = line.split(";")
                    course_list6.append(line_words)
                for i in range(len(course_list6)):
                    if student_id == course_list6[i][0]:
                        course_list6[i].append(code)  # registering a student that already exist
                    else:
                        student_name = input("Enter student name and surname:")
                        course_list6[0].append(student_id + ";" + student_name + ";" + code)
                        break

    elif choice == "7":  # list all the student's courses
        with open('student.txt', 'r') as file5:
            course_list5 = []
            for line in file5:
                line = line.rstrip("\n")
                line_words = line.split(";")
                course_list5.append(line_words)
            for i in range(len(course_list5)):
                print(course_list5[i][1], "'s courses:", course_list5[i][2])

    elif choice == "8":  # List top 3 most crowded courses.

        with open("course.txt", 'r') as file:
            list = []
            for line in file:
                line = line.rstrip("\n")
                line_words = line.split(";")
                list.append(line_words)

            for j in range(len(list) - 1):
                for i in range(len(list) - j - 1):
                    if list[i][3] < list[i + 1][3]:
                        temp = list[i]
                        list[i] = list[i + 1]
                        list[i + 1] = temp

            print("Top 3 most crowded courses: \n" + "1. " + list[0][1] + "\n" + "2. " + list[1][1] + "\n" + "3. " +
                  list[2][1])

    elif choice == "9":  # List top 3 students with the most course registrations.
        with open("student.txt", 'r') as file4:
            list2 = []
            for line in file4:
                line = line.rstrip("\n")
                line_words = line.split(";")
                list2.append(line_words)

            for j in range(len(list2) - 1):
                for i in range(len(list2) - j - 1):
                    if list2[i][2] < list2[i + 1][2]:
                        temp = list2[i]
                        list2[i] = list2[i + 1]
                        list2[i + 1] = temp
            print(
                "Top 3 students with the most course registrations: \n" + "1. " + list2[0][1] + "\n" + "2. " + list2[1][
                    1] + "\n" + "3. " +
                list2[2][1])
