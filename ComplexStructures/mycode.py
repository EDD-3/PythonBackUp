msg = 'Hello World'
#All functions are objects
def add_five(num):
    print( num + 5)

#print(add_five)
#This will not throw an error

#Function within function
def add_five(num):
    def add_two(num):
        return num + 2
    num_plus_two = add_two(num)
    print(num_plus_two + 3) 

#Functions that returns a function
def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2
    if  operation == '+':
        return add
    elif operation == '-':
        return sub
add_function = get_math_function('+')
sub_function = get_math_function('-')

#Decorating a function
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor:")
        print_name_function(*args, **kwargs)
    return wrapper


@title_decorator    #Decorators
def print_my_name():
    print("Eduardo")

@title_decorator    #Decorators
def print_joes_name():
    print('Joes')

#print_joes_name()

#Decorators with Parameters
@title_decorator
def print_my_name(name, age):
    print(name + "you are" + str(age))

