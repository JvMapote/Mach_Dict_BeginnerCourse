def HelloWorld():
    #Hello world
    print("Hello world")
    print("I love cakes")

def Variables():
    #Variables
    x = 7
    y = "cake"

    print(x)
    print(y)

    #String concatenation

    favorite_food = "pizza"
    friend_name = "tina"
    favorite_drink = "soda"

    print("I like " + favorite_food + ".")
    print("I like eating " + favorite_food + " with my friend, " + friend_name + ".")
    print("We like to drink " + favorite_drink + ".")

def syntax_error():
    #Syntax and error
    favorite_food = set ("pizza")
    if favorite_food == "pizza":
        print("I like pizza")

def challenges():
    #challenge 1
    string = "this is a string."
    print(string)

    #challenge 2
    print("I could use a cup of coffee.")

    #challenge 3
    favorite_book = "Slaughterhouse-Five"
    least_favorite_book = "Jane Eyre"

    print("I enjoyed reading " + least_favorite_book + ".")

    #challenge 4
    #how to make a comment

    #challenge 5
    #dude this is boring ill skip this task basta w at z

def functions():
    #creating functions

    def hello_function(name):
        print("Hello, " + name + "!")

    hello_function("jv")

def input_Function():
    #using input

    name = input("Enter your name: ")
    print("Hi " + name + "!")

    def addNum(num1, num2):
        total = num1 + num2
        return(total)

    num1 = int(input("Please enter your first number: "))
    num2 = int(input("Please enter your second number: "))
    print("Total: ", addNum(num1, num2))

def datatypes_conversion():
    variable = null
    print(int(variable))
    print(float(variable))
    print(str(variable))
    print(tuple(variable))
    print(list(variable))