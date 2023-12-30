
negativeNumList = []
total = 0
i = 1
print("Enter negative numbers otherwise 'X' to quit")

while True:
    userInput = input(f"Enter NEGATIVE number ({i}): ")

    if userInput == 'X':
        break

    num = float(userInput)
    if num < 0:
        negativeNumList.append(num)
        total += num
        i += 1
    else:
        print("*** Not a negative number, try again.")

print("\b")
print("negativeNumList", negativeNumList)
print("Sum :", total)
