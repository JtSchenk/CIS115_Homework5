# CIS115 - Homework5 (Student Grading)
# Jacob Schenkelberg

# this method take the student's name and id number
def input_student():
    student_name = input("\nWhat is your name?: ")
    student_id = input("\nWhat is your id number?: ")
    return student_name, student_id

# This method takes the score for each assignment
def input_assignments(student_dic, num_assignments):
    total_scores = []
    # iterate through the number of assignments and asks the user for the score.
    for i in range(num_assignments):
        score_assignment = int(input("Enter score for assignment {}: ".format(i+1)))
        total_scores.append(score_assignment)
        student_dic['Scores'] = total_scores

#This method takes the scores and creates an average for the student.
def grade_student(student_dic):
    average_student = sum(student_dic['Scores'])/len(student_dic['Scores'])
    student_dic['Average Score'] = average_student

# This method takes all inputs and prints the report for a student.
def print_report(student_dic):
    for id in student_dic:
        print("Name: {}, Scores: {}, Average Grade: {}".format(student_dic[id]["Student Name"], student_dic[id]["Scores"], student_dic[id]['Average Score']))

# This is the main loop that has extra functionality, but also calls each method within it.
def main():
    # setting the count to 0.
    count = 0  
    # create an empty dictionary.
    student_dic = {}
    # Have enter_student = 'Y' so it enters the while loop
    enter_student = 'Y'
    # This loop will ask the user if they want to add a student,
    # if added, it will add the student to the dictionary with their scores, id, and average score.
    while(enter_student != 'N' and enter_student != 'n'):
        count = count + 1
        student_name, student_id = input_student()
        student_dic[student_id] = {"Student Name": student_name, "Average Score": 0}
        enter_student = input("\nDo you want to enter another student? (y) (n): ")[0]
    number_assignments = int(input("Enter number of assignments: "))
    # iterate through the dictionary to find the name and number of assignments.
    for key in student_dic:
        print("\nEnter scores for {}".format(student_dic[key]["Student Name"]))
        input_assignments(student_dic[key], number_assignments)
        grade_student(student_dic[key])
    # this method prints the report.
    print_report(student_dic)
# Calls the main method
main()