length = abs(int(input("Enter the size of the pattern: ")))
count=length
while count > 0:
    for _ in range(length):
        print("*", end="")
    print("\n")
    count -=1

