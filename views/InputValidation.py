from views.InputException import InputException


class InputValidation:
    @staticmethod
    def validate(equation_input, method, start, end):
        if InputValidation.missing_input_equation(equation_input):
            raise InputException("Input Equation is missing")
        elif InputValidation.full_interval_needed(method, start, end):
            raise InputException("Both Intervals ends are needed")
        elif InputValidation.partial_interval_needed(method, end):
            raise InputException("A starting point is needed")


    @staticmethod
    def missing_input_equation(equation_input):
        return equation_input == ""

    @staticmethod
    def full_interval_needed(method, start, end):
        return (method == "Bisection" or method == "False-Position" or method == "Secant") and (
                start == "" or end == "")

    @staticmethod
    def partial_interval_needed(method, end):
        return (method == "Newton" or method == "Fixed Point" or method == "Bierge Vieta") and (
                end == "")
