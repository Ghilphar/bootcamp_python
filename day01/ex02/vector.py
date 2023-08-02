class Vector:
    def __init__(self, values):
        if isinstance(values, int):
            self.values = [[float(i)] for i in range(values)]
            self.shape = (values, 1)
        elif isinstance(values, tuple) and len(values) == 2:
            if values[0] > values[1]:
                raise ValueError("The start fo the range cannot be greater than the end.")
            self.values = [[float(i)] for i in range(values[0],values[1])]
            self.shape = (values[1] - values[0], 1)
        elif isinstance(values[0], list) and all(isinstance(x[0], float) for x in values):
            self.values = values
            if len(values[0]) == 1:
                #column vector
                self.shape = (len(values), 1)
            else:
                # row vector
                self.shape = (1, len(values[0]))
        else:
            raise ValueError("Values must be a list of lists of floats")

    def dot(self, otherVector):
        if not isinstance(otherVector, Vector):
            raise TypeError("The paramater must be a Vector.")

        self_dim = self.shape[0] * self.shape[1]
        other_dim = otherVector.shape[0] * otherVector.shape[1]

        if self_dim != other_dim:
            raise ValueError("Vectors must be of the same dimension for a dot product.")

        #Row Row
        if self.shape[0] == 1 and otherVector.shape[0] == 1:
            dotProduct = sum(self.values[0][i] * otherVector.values[0][i] for i in range(len(self.values[0])))
        #Row Column
        elif self.shape[0] == 1 and otherVector.shape[1] == 1:
            dotProduct = sum(self.values[0][i] * otherVector.values[i][0] for i in range(len(self.values[0])))
        #Column Row
        elif self.shape[1] == 1 and otherVector.shape[0] == 1:
            dotProduct = sum(self.values[i][0] * otherVector.values[0][i] for i in range(len(self.values)))
        #Column column
        elif self.shape[1] == 1 and otherVector.shape[1] == 1:
            dotProduct = sum(self.values[i][0] * otherVector.values[i][0] for i in range(len(self.values)))

        return dotProduct
    
    def T(self):
        if self.shape[0] == 1:  # row vector
            return Vector([[x] for x in self.values[0]])
        else:  # column vector
            return Vector([[self.values[i][0] for i in range(self.shape[0])]])

    def __add__(self, otherVector):
        if self.shape != otherVector.shape:
            raise ValueError("Vectors must be of the same shape.")
        if self.shape[0] == 1:  # row vector
            return Vector([[(self.values[0][i] + otherVector.values[0][i]) for i in range(self.shape[1])]])
        else:  # column vector
            return Vector([[(self.values[i][0] + otherVector.values[i][0])] for i in range(self.shape[0])])

    def __radd__(self, otherVector):
        return self.__add__(otherVector)

    def __sub__(self, otherVector):
        if self.shape != otherVector.shape:
            raise ValueError("Vectors must be of the same shape.")
        # row vector
        if self.shape[0] == 1:
            return Vector([[(self.values[0][i] - otherVector.values[0][i]) for i in range(self.shape[1])]])
        # column vector
        else:
            return Vector([[(self.values[i][0] - otherVector.values[i][0])] for i in range(self.shape[0])])

    def __rsub__(self, otherVector):
        return otherVector.__sub__(self)

    def __mul__(self, operand):
        if isinstance(operand, (int, float)):
            #column vector
            if self.shape[1] == 1:
                return Vector([[value[0]*operand] for value in self.values])
            #row vector
            else:
                return Vector([[value[column]*operand for column in range(self.shape[1])] for value in self.values])
        else:
            raise TypeError("We only can multiply Vectors by Scalars. (int, float)")

    def __rmul__(self, operand):
        return self.__mul__(operand)

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ZeroDivisionError("division by zero")
            #column vector
            if self.shape[1] == 1:
                return Vector([[value[0]/divisor] for value in self.values])
            #row vector
            else:
                return Vector([[value[column]/divisor for column in range(self.shape[1])] for value in self.values])
        else:
            raise TypeError("We only can divide Vectors by Scalars.  (int, float)")

    def __rtruediv__(self, divisor):
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __str__(self):
        return f"{self.values}"
    
    def __repr__(self):
        return self.__str__()
