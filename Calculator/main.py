def addition(numbers):
    return sum(numbers)

def subtraction(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiplication(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result *= num
    return result

def division(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num != 0:
            result /= num
        else:
            return "Invalid operation: Division by zero error!"
    return result

print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Select an operation (1/2/3/4): ")

num_count = int(input("Enter the number of values you want to operate on: "))
numbers = []
for i in range(num_count):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

if choice == '1':
    print("Result:", addition(numbers))
elif choice == '2':
    print("Result:", subtraction(numbers))
elif choice == '3':
    print("Result:", multiplication(numbers))
elif choice == '4':
    print("Result:", division(numbers))
else:
    print("Invalid operation choice!")