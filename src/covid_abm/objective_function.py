"""
Módulo que define a função objetiva utilizada.
"""

import typing
from dataclasses import dataclass

import numpy as np
from COVID19 import model, simulation

from covid_abm import mapper_function as mapper
from covid_abm import utils

_ACC_CASES = [679, 1667, 2035, 2380, 2919, 3544, 4319]


@dataclass
class ObjectiveFunction:
    fn: typing.Callable[[typing.Any], float]
    name: str


def rmse() -> ObjectiveFunction:
    def _rmse(solution: typing.Any) -> float:
        # Executar simulação
        sim_acc = _run_simulation(solution)
        n = len(sim_acc)

        # Calcular erro
        error = np.array(sim_acc) - np.array(_ACC_CASES)
        squared = error ** 2
        sum_ = np.sum(squared)
        mean = sum_ / n

        return np.sqrt(mean)

    return ObjectiveFunction(_rmse, "RMSE")


def mae() -> ObjectiveFunction:
    def _mae(solution: typing.Any) -> float:
        # Executar simulação
        sim_acc = _run_simulation(solution)
        n = len(sim_acc)

        # Calcular erro
        error = np.array(sim_acc) - np.array(_ACC_CASES)
        absolute = np.abs(error)
        sum_ = np.sum(squared)
        mean = sum_ / n

        return mean

    return ObjectiveFunction(_mae, "MAE")


def _run_simulation(solution,
                    input_params: str = str(utils._PARAMS)) -> typing.List[int]:
    params = model.Parameters(input_param_file=input_params,
                              param_line_number=1)
    params.set_param("rng_seed", 1)
    end_time = params.get_param("end_time")
    params.set_param_dict(mapper.default_mapper(solution).dict())

    m = simulation.COVID19IBM(model=model.Model(params))
    s = simulation.Simulation(env=m, end_time=end_time)
    s.steps(end_time)

    acc = s.results.get('total_infected')

    print('solution:', solution)
    print('acc:', acc)
    return acc
