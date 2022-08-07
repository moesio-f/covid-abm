"""
Executa todos os algoritmos para calibração do ABM.
"""

import typing

from mealpy.swarm_based.PSO import BasePSO
from mealpy.evolutionary_based.DE import SHADE

from covid_abm.objective_function import quadratic_error


def pso(fn,
        pop_size: int,
        max_fe: int):

    epoch = 10000
    termination = _termination_from_max_fe(max_fe)
    problem = _fn_as_problem(fn)

    model = BasePSO(problem,
                    epoch=epoch,
                    pop_size=pop_size,
                    termination=termination,
                    mode="swarm")

    bs, bf = model.solve(mode="swarm")

    return model, bs, bf


def _termination_from_max_fe(max_fe: int) -> typing.Dict:
    return {
        "mode": "FE",
        "quantity": max_fe
    }


def _fn_as_problem(fn) -> typing.Dict:
    return {
        "fit_func": fn,
        "lb": [0.0] * 9,
        "ub": [20.0] + [50] * 3 + [1000] + [21.0] * 4,
        "minmax": "min",
        "n_dims": 9,
        "verbose": True,
        "save_population": False,
        "log_to": "console"
    }


if __name__ == '__main__':
    pso_model, pso_bs, pso_bf = pso(quadratic_error,
                                    10,
                                    30)
    print(pso_bs)
    print(pso_bf)
    pso_model.history.save_global_best_fitness_chart(
        filename="pso_best_fitness")
