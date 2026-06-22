# Removing Duplicates from a list

def remove_duplicates(input_list):
    unique_list = []

    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list

list = [1,2,3,4,1,2,6,8]
print(remove_duplicates(list))

#student marks dictionary

student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

def calculate_average(marks_dict):
    total_marks = sum(marks_dict.values())
    n = len(marks_dict)
    if n == 0:
        return 0
    average = total_marks/n
    return average

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F" 
    
print("Average Marks:", calculate_average(student_marks))
print("Grade of whole class:", calculate_grade(calculate_average(student_marks)))