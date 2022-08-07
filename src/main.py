
from covid_abm.objective_function import quadratic_error

if __name__ == '__main__':
    print(quadratic_error([0.1, 0.2, 0.3, 0.4, 500] + [100] * (13 - 5)))
