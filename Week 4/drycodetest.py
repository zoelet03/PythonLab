PASS_MARK = 40
passes = 2

mark_1 = input("Please enter mark 1: ")
mark_2 = input("Please enter mark 2: ")
mark_3 = input("Please enter mark 3: ")
mark_4 = input("Please enter mark 4: ")

if mark_1 >= PASS_MARK:
    passes += 1
if mark_2 >= PASS_MARK:
    passes += 1
if mark_3 >= PASS_MARK:
    passes += 1
if mark_4 >= PASS_MARK:
    passes += 1
