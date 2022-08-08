"""
Executa todos os algoritmos para calibração do ABM.
"""

import argparse

from covid_abm import algorithms
from covid_abm import objective_function as fns

POP_SIZE = 10
GENERATIONS = 6

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='AEs para Calibração do OpenABM-COVID19.')
    parser.add_argument('-a', type=str,
                        required=True,
                        help='algoritmo (PSO, SHADE ou ACOR)',
                        dest='alg')
    parser.add_argument('-e', type=str, required=True,
                        help='função objetiva (RMSE ou MAE)',
                        dest='error')
    args = parser.parse_args()

    alg = str(args.alg).upper()
    error = args.error

    fn = fns.mae()

    if error == 'RMSE':
        fn = fns.rmse()

    if alg == 'PSO':
        algorithms.pso(fn, POP_SIZE, GENERATIONS)
    elif alg == 'ACOR':
        algorithms.acor(fn, POP_SIZE, GENERATIONS)
    else:
        algorithms.shade(fn, POP_SIZE, GENERATIONS)
