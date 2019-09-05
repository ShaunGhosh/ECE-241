class EquationSolver:
    def __init__(self):
        print('Equation Solver Initialized')

    def monomial_solver(self):
        a = int(input('Enter Value of a: '))
        b = int(input('Enter Value of b: '))
        c = int(input('Enter Value of c: '))

        x = (c + b)/a
        print('Solution of x in {}x - {} = {} is x = {}'.format(a, b, c, x))

    def polynomial_solver(self):
        a = int(input('Enter Value of a: '))
        b = int(input('Enter Value of b: '))
        c = int(input('Enter Value of c: '))

        x = ((c ** 2) - b)/a
        print('Solution of x in √{}x + {} = {} is x = {}'.format(a, b, c, x))


solution = EquationSolver()
solution.polynomial_solver()


