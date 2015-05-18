class CalculatorLibrary(object):
    """Custom test library for testing Calculator functions.
    """

    def __init__(self):
        #Initilize new calculator value
        self._result = 0

    def add_numbers(self, num1, num2):
        #Convert to ints before adding
        inum1 = int(num1)
        inum2 = int(num2)
        self._result = inum1 + inum2

    def multiply_numbers(self, num1, num2):
        #Convert to ints before multiplying 
        inum1 = int(num1)
        inum2 = int(num2)
        self._result = inum1 * inum2

    def clear_num(self):
        #Same as C. Resets calculator to 0
        self._result = 0

    def result_should_be(self, expected):
        #Verifies that the current result is `expected`.
        iexpected = int(expected)
        if self._result != iexpected:
            raise AssertionError('{0} != {1}'.format(self._result, iexpected))
