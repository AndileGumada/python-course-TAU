def user_info(name, age =0, city="Taung"):
    '''This function prints name, age and city from an argument provided to the function. '''

    # Positional argument are read in the order they appear
    # keyword argument
    print("{} is {} years old, from {}".format(name,age, city))
#
user_info("Andile", 30, "Gauteng")
user_info("Thabile")
# *agrs allows a function to take any number of positional argumnets
# def add(*args):
# print(sum(agrs))
# **kwargs allows a function to take any number of keyword arguments pass passed to it
# all three types can be used in a single function, But they must be in order : formal positional arguments, *args, **kwargs

def application(fname, lname, email, company,*args, **kwargs):
    print("{} {} works at {}. His email is {}.".format(fname, lname,company,email))

application("Andile","Gumada", "mail@stellr.com","Stellr",70000, hire_date="Septermber 2020")
