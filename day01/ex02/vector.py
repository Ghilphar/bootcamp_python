class Vector:
    def __init__(self, values):
        if isinstance(values[0], list) and all(isinstance(x[0], float) for x in values):
            self.values = values
            if len(values[0]) == 1:
                #column vector
                self.shape = (len(values), 1)
            else:
                # row vector
                self.shape = (1, len(values[0]))
        else:
            raise ValueError("Values must be a list of lists of floats")

    def __mul__(self, operand):
        if isinstance(operand, (int, float)):
            if self.shape[1] == 1: #column vector
                return Vector([[value[0]*operand] for value in self.values])
            else:
                return Vector([[value[column]*operand for column in range(self.shape[1])] for value in self.values])
        else:
            raise ValueError("We only can multiply floats or ints")

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ZeroDivisionError("division by zero")
            if self.shape[1] == 1:
                return Vector([[value[0]/divisor] for value in self.values])
            else:
                return Vector([[value[column]/divisor for column in range(self.shape[1])] for value in self.values])

    def __str__(self):
        return f"Vector(values={self.values})"


v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5

print(v2)


v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5

print(v2)

v2 = v1 / 2.0
print(v2)