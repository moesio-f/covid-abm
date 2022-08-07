"""
Módulo que define a função objetiva utilizada.
"""

import numpy as np
from COVID19 import model, simulation

from covid_abm import mapper_function as mapper

ACC_CASES = 4523


def quadratic_error(solution: np.array,
                    input_params: str = "./data/params.csv",
                    output_dir: str = "./data/output") -> float:
    params = model.Parameters(input_param_file=input_params,
                              param_line_number=1,
                              output_file_dir=output_dir)
    params.set_param("rng_seed", int(np.random.uniform(low=0, high=9999999)))
    end_time = params.get_param("end_time")
    params.set_param_dict(mapper.default_mapper(solution).dict())

    m = simulation.COVID19IBM(model=model.Model(params))
    s = simulation.Simulation(env=m, end_time=end_time)
    s.steps(end_time)

    return float((_extract_acc(s) - ACC_CASES)) ** 2


def _extract_acc(s: simulation.Simulation) -> int:
    return s.results.get('total_infected')[-1]
