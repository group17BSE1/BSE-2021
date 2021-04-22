total = 0
count = 0
average = 0

while True:
    try:
        inp = input("Enter a number: ")
        if inp == "done":
            break
        value = float(inp)
        total = value + total
        count = count + 1
        average = total / count
    except ValueError:
        print("Invalid input.")
print(total, count, average)
