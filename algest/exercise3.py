cont = 1
number = int(input("Enter a number: "))
print(f"Multiplication table of {number}")
print("=" * 13)
while cont <= 12:
    print(f"{cont} * {number} = {cont * number}")
    cont += 1
print("=" * 13)