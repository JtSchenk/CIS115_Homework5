def input_student():
    name_list = []
    id_list = []
    is_new_student = True
    while(is_new_student == True):
        student_name = input("What is your name?: ")
        name_list.append(student_name)
        student_id = input("\nWhat is your id number?: ")
        id_list.append(student_id)
        enter_student = input("Enter another student? (y)es or (n)o: ")
        if(enter_student == "Y" or enter_student == "y"):
            pass
        elif(enter_student == "N" or enter_student == "n"):
            break
        else:
            while(enter_student != "Y" or enter_student != "y" or enter_student != "N" or enter_student != "n"):
                print("\nEnter a valid response.\n")
                enter_student = input("Enter another student? (y)es or (n)o: ")
                if(enter_student == "Y" or enter_student == "y"):
                    break
                elif(enter_student == "n" or enter_student == "N"):
                    is_new_student = False
                    break
    return name_list, id_list


def input_assignments(student_dic, num_assignments):
    total_scores = []

    for i in range(num):
        score_assignment = int(input("Enter score for assignment: "))
        total_scores.append(score_assignment)
        student_dic['Scores'] = total_scores

def grade_student():
    pass

def print_report():
    pass

def main():
    pass

input_student()
input_assignments()