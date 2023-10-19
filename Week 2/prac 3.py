def calculate_groups(num_students, group_size):

    num_groups = num_students // group_size
    remaining_students = num_students % group_size


    if remaining_students == 1:
        return f"There will be {num_groups} groups with 1 student left over."
    else:
        return f"There will be {num_groups} groups with {remaining_students} students left over."


num_students = int(input("How many students? "))
group_size = int(input("Required group size? "))


result = calculate_groups(num_students, group_size)
print(result)
