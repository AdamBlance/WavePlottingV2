import sympy as sy
from functions import all_functions
from re import split
# Doing this to avoid Python limitation. It cannot be made a static variable because I'm using list comprehension.


class Function:

    def __init__(self, function, limits):

        print(function)

        self.unformatted_function = self.unformatted_function.replace(' ', '').replace('^', '**')

        modified = False
        for function_tuple in all_functions:
            for function in function_tuple:
                function_index = self.unformatted_function.find(function)
                if function_index != -1:
                    modified = True
                    self.formatted_function = self.unformatted_function.replace(function, function_tuple[function])
