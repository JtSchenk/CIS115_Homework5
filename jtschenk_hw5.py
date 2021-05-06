def input_student():
    name_list = []
    id_list = []
    is_new_student = True
    student_name = input("What is your name?: ")
    name_list.append(student_name)
    student_id = input("\nWhat is your id number?: ")
    id_list.append(student_id)
    return name_list, id_list


def input_assignments(student_dic, num_assignments):
    total_scores = []

    for i in range(num_assignments):
        score_assignment = int(input("Enter score for assignment {): ".format(i)))
        total_scores.append(score_assignment)
        student_dic['Scores: '] = total_scores

def grade_student(student_dic):
    average_student = sum(student_dic['Scores'])/len(student_dic['Scores'])
    student_dic['Average:'] = average_student

def print_report(student_dic):
    for id, student in student_dic.items():
        print("Name: {}, Scores: {}, Average Grade: {}".format(student["Student Name"], student["Scores"], student['Average Score']))

def main():
    
    student_dic = {}

#may be problem with different names and input methods.
    enter_student = 'Y'

    while(enter_student != 'N' or enter_student != 'n'):

        student_name, student_id = input_student()

        student_dic[student_id] = {"Student Name": student_name, "Average Score":0}

        enter_student = input("Do you want to enter another student?: ")[0]

    number_assignments = int(input("Enter number of assignments: "))

    input_assignments(student_dic[student_id], number_assignments)

    grade_student(student_dic[student_id])

    print_report(student_dic)

main()