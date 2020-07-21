def input_interpreter(function_input_simple_additive):
    function_input.split("+")

import re
import math
def derivative_calculator_ln(derivative_order):

    #matcher = re.compile(".*1/.+") #regex expression to allow for pattern matching of (factor)*(1/x^(power))

    #template for ln derivatives of order > 1
    #ln_template = "1/{ln_divisor}"

    #calculate factor, negative for odd values and vice versa
    if derivative_order%2 == 0:
        factor_ln = math.factorial(derivative_order-1) * (-1)
    else:
        factor_ln = math.factorial(derivative_order-1)

    if derivative_order == 0:
        #derivative order 0
        return "ln(x)"

    if derivative_order == 1:
        #derivative order 1
        return "1/x"

    #derivative order > 1
    if derivative_order > 1:

        if derivative_order%2 == 0: #check for even magnitude
            return str(factor_ln) + "*" + "1/" + "x^" + str(derivative_order)


        if derivative_order%2 == 1: #check for odd magnitude
            return str(factor_ln) + "*" + "1/" + "x^" + str(derivative_order)

def derivative_calculator_expx():
    return "e^x"

def derivative_calculator_polynomial(input_function_polynomial, derivative_order):
    #input function of form (factor)*x^(power)
    #split * to obtain factor at index 0 of return list
    #split ^ to obtain power at index 1 of return list

    derived_power = int(input_function_polynomial.split('^')[1]) - 1
    derived_factor = int(input_function_polynomial.split('^')[1]) * int(input_function_polynomial.split('*')[0])
    
    return str(derived_factor) + "*x^" + str(derived_power)
