class EquationSolver:
    def __init__(self, a, b, c):
        print('Equation Solver Initialized')
        self.a = a
        self.b = b
        self.c = c

    def monomial_solver(self):
        x = (self.c + self.b)/self.a
        return'Solution of x in {}x - {} = {} is x = {}'.format(self.a, self.b, self.c, x)

    def polynomial_solver(self):

        x = (pow(self.c, 2) - self.b)/self.a
        return 'Solution of x in √{}x + {} = {} is x = {}'.format(self.a, self.b, self.c, x)


a = int(input('Enter Value for a: '))
b = int(input('Enter Value for b: '))
c = int(input('Enter Value for c: '))

solution = EquationSolver(a, b, c)
print(solution.polynomial_solver())
print(solution.monomial_solver())

