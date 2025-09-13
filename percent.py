user_input = input("Fraction: ")
x,y = user_input.split("/")

x = int(x)
y = int(y)
result = x / y

percent = round(result * 100)

print(f"percent:{percent}%")