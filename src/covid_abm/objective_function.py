"""
Módulo que define a função objetiva utilizada.
"""

import numpy as np
from COVID19 import model, simulation

from covid_abm.utils import Parameters

ACC_CASES = 4523


def quadratic_error(solution: np.array):
    params = model.Parameters(input_param_file="./data/params.csv",
                              param_line_number=1,
                              output_file_dir="./data_test",)
    params.set_param("n_total", 10000)
    params.set_param("end_time", 20)
    m = simulation.COVID19IBM(model=model.Model(params))
    s = simulation.Simulation(m)
    s.start_simulation()
    print(s.results)
