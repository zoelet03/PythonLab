import sys
count = len(sys.argv)
x=count-1
total = 0
while count > 1:
    count -= 1
    total += int(sys.argv[count])
    print("count number: ", count)

    if x == 0:
        print("No arguments were provided")

avg = total/x

print(f"Total is, {total}")

print(f"Average is, {avg}")
