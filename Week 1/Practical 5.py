def calculate_lab_groups(num_students, group_size):
    full_groups = num_students // group_size
    leftover_students = num_students % group_size
    return full_groups, leftover_students

def display_results(num_students, group_size):
    full_groups, leftover_students = calculate_lab_groups(num_students, group_size)
    print(f'Number of students: {num_students}')
    print(f'Lab group size: {group_size}')
    print(f'Number of full groups: {full_groups}')
    print(f'Number of students in the leftover group: {leftover_students}\n')

# List of number of students
students_list = [113, 175, 12]

# Lab group size
group_size = 24

for num_students in students_list:
    display_results(num_students, group_size)
