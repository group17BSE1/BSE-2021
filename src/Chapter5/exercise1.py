total = 0
count = 0
average = 0

while True: #this will iterate over the block of code provided the condition is true
    try: #this helps to check the cod block and if there ae no errors the code is executed
        inp = input("Enter a number: ")
        if inp == "done":
            break
            #break this will terminate the while loop and execute other codes outside the loop
        value = float(inp)
        total = value + total
        count = count + 1
        average = total / count
    except ValueError: #this helps to check the cod block and if there ae no errors the code is executed
        print("Invalid input.")
print(total, count, average)
