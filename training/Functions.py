# SOME NOTES FOR LOOPS IN PYTHON


# Creation
def function_name():
    print("This is a function")


# Calling a function
function_name()


# Function with parameters
def function_with_parameters(first_parameter):
    print("This a function with this parameter: " + first_parameter)


# Calling function with parameters
function_with_parameters("andres")


# Function with a default parameter value
def function_with_default_parameter_value(parameter=324):
    print("This is a function with a default parameter value: " + parameter)


# Calling a function with default parameter value
function_with_default_parameter_value()  # If you don't set a parameters, it takes the default value

function_with_default_parameter_value(124)  # If you set a parameter, it takes that one.


# Return value
def function_with_return_value(x):
    return x ** x  
