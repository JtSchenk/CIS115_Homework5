# this method take the student's name and id number
def input_student():
    student_name = input("\nWhat is your name?: ")
    student_id = input("\nWhat is your id number?: ")
    return student_name, student_id


def input_assignments(student_dic, num_assignments):
    total_scores = []
    for i in range(num_assignments):
        score_assignment = int(input("Enter score for assignment {}: ".format(i+1)))
        total_scores.append(score_assignment)
        student_dic['Scores'] = total_scores

def grade_student(student_dic):
    average_student = sum(student_dic['Scores'])/len(student_dic['Scores'])
    student_dic['Average Score'] = average_student

def print_report(student_dic):
    for id in student_dic:
        print("Name: {}, Scores: {}, Average Grade: {}".format(student_dic[id]["Student Name"], student_dic[id]["Scores"], student_dic[id]['Average Score']))

def main():

    count = 0
    
    student_dic = {}

    enter_student = 'Y'

    while(enter_student != 'N' and enter_student != 'n'):

        count = count + 1

        student_name, student_id = input_student()

        student_dic[student_id] = {"Student Name": student_name, "Average Score": 0}

        enter_student = input("\nDo you want to enter another student? (y) (n): ")[0]

    number_assignments = int(input("Enter number of assignments: "))

    for key in student_dic:

        print("\nEnter scores for {}".format(student_dic[key]["Student Name"]))

        input_assignments(student_dic[key], number_assignments)

        grade_student(student_dic[key])

    print_report(student_dic)

main()