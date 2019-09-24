# Equation Solver Class takes in the values of a, b and c from the user and calculates the solution of x in the
# monomial and binomial equations.


class EquationSolver:

    # initializes EquationSolver Class and assigns the parameters of the class to the attributes.
    def __init__(self, a, b, c):
        print('Equation Solver Initialized')
        self.a = a
        self.b = b
        self.c = c

    # monomial_solver method solves for the value of x in the equation ax + b = c.
    def monomial_solver(self):
        x = (self.c + self.b)/self.a
        return'Solution for x in {}x - {} = {} is x = {}'.format(self.a, self.b, self.c, x)

    # polynomial_solver method solves for the value of x in the equation √(ax + b) = c.
    def polynomial_solver(self):

        x = (pow(self.c, 2) - self.b)/self.a
        return 'Solution for x in √{}x + {} = {} is x = {}'.format(self.a, self.b, self.c, x)


# variables a,b and c take the values for a, b & c from the user.
a = int(input('Enter Value for a: '))
b = int(input('Enter Value for b: '))
c = int(input('Enter Value for c: '))


# solution variable is assigned EquationSolver with a constructor for a, b and c.
solution = EquationSolver(a, b, c)
print(solution.polynomial_solver())
print(solution.monomial_solver())

