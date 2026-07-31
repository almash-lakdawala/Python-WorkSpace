# name = "almash"
# age = 25
# print("Hello " + name + " age is " + str(age))


#The f before the string = formatted string
#Anything inside {} gets replaced by the variable’s value
# print(f"Hello {name}, age is {age}")


#{} are placeholders
#.format(name, age) fills them in order
# print("Hello {}, age is {}".format(name, age))


#the following code is alow us to take input from user
# name = input("What is your name ? ")
# print("Hello "+ name)


#type checking or conversion
# birth_year = input("Enter your birth year: ")
# age = 2026 - int(birth_year)
# print(age)

# num1 = input("Enter value of num1: ")
# num2 = input("Enter value of num2: ")
# sum = num1 + num2
# print(f"The sum of num1 and num2 is: {sum} ")


course = "Python for Beginners"

print(course.upper())

stack = []

while True:

    print("\n1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        stack.append(value)

    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow")
        else:
            print("Deleted:", stack.pop())

    elif choice == 3:
        if len(stack) == 0:
            print("Stack Empty")
        else:
            print("Top =", stack[-1])

    elif choice == 4:
        print(stack)

    elif choice == 5:
        break

    else:
        print("Invalid Choice")