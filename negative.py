gradeNumList = []
total = 0

while True:
    user_input = input("Enter a negative number (or 'X' to exit): ")

    if user_input == 'X':
        break

    try:
        num = int(user_input)
        if num < 0:
            gradeNumList.append(num)
            total += num
        else:
            print("Not a negative number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number or 'X' to exit.")

print("Negative Numbers:", gradeNumList)
print("Sum of Entered Numbers:", total)
