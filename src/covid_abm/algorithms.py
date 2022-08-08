"""
Módulo dos algoritmos.
"""

import pathlib
import typing

from mealpy.evolutionary_based.DE import SHADE
from mealpy.swarm_based.ACOR import BaseACOR
from mealpy.swarm_based.PSO import BasePSO

from covid_abm import utils
from covid_abm.objective_function import ObjectiveFunction


def pso(fn: ObjectiveFunction,
        pop_size: int,
        generations: int):

    epoch = 10000
    termination = _termination_max_gen(generations)
    problem = _fn_as_problem(fn, "pso")

    model = BasePSO(problem,
                    epoch=epoch,
                    pop_size=pop_size,
                    termination=termination,
                    mode="swarm")

    bs, bf = model.solve(mode="swarm")
    model.history.save_global_best_fitness_chart(
        filename="pso_convergence.png")
    model.history.save_local_best_fitness_chart(
        filename="local_pso.png")

    return model, bs, bf


def shade(fn: ObjectiveFunction,
          pop_size: int,
          generations: int):

    epoch = 10000
    termination = _termination_max_gen(generations)
    problem = _fn_as_problem(fn, "shade")

    model = SHADE(problem,
                  epoch=epoch,
                  pop_size=pop_size,
                  termination=termination,
                  mode="swarm")

    bs, bf = model.solve(mode="swarm")
    model.history.save_global_best_fitness_chart(
        filename="shade_convergence.png")
    model.history.save_local_best_fitness_chart(
        filename="local_shade.png")

    return model, bs, bf


def acor(fn: ObjectiveFunction,
         pop_size: int,
         generations: int):

    epoch = 10000
    termination = _termination_max_gen(generations)
    problem = _fn_as_problem(fn, "acor")

    model = BaseACOR(problem,
                     epoch=epoch,
                     pop_size=pop_size,
                     sample_count=2,
                     termination=termination,
                     mode="swarm")

    bs, bf = model.solve(mode="swarm")
    model.history.save_global_best_fitness_chart(
        filename="acor_convergence.png")
    model.history.save_local_best_fitness_chart(
        filename="local_acor_convergence.png")

    return model, bs, bf


def _termination_max_gen(gens: int) -> typing.Dict:
    return {
        "mode": "MG",
        "quantity": gens
    }


def _fn_as_problem(fn: ObjectiveFunction, fname: str) -> typing.Dict:
    filename = f"{fname}-{fn.name}.log"
    log_path: pathlib.Path = utils._RESULTS_DIR.joinpath('logs')
    log_file: pathlib.Path = log_path.joinpath(filename)
    log_file.parent.mkdir(exist_ok=True, parents=True)
    log_file.write_text("")

    return {
        "fit_func": fn.fn,
        "lb": [0.0] * 9,
        "ub": [20.0] + [50] * 3 + [1000] + [21.0] * 4,
        "minmax": "min",
        "n_dims": 9,
        "verbose": True,
        "save_population": False,
        "log_to": "file",
        "log_file": log_file
    }
