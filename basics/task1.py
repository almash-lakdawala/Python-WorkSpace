name = "almash"
age = 25

print("Hello " + name + " age is " + str(age))


#The f before the string = formatted string
#Anything inside {} gets replaced by the variable’s value
print(f"Hello {name}, age is {age}")


#{} are placeholders
#.format(name, age) fills them in order
print("Hello {}, age is {}".format(name, age))


#the following code is alow us to take input from user
name = input("what is your name ? ")
print("Hello "+ name)



