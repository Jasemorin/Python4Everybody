num = 0
tot = 0.0

while True:
    sval = input("Enter a number: ")
    if sval == "done":
        break
    try:
        fval = float(sval)
    except ValueError:
        print("Invalid input")
        continue
    num += 1
    tot += float(sval)

print("ALL DONE")
print("Count:", num)
print("Sum:", tot)
print("Average:", tot / num)
