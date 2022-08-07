"""
Módulo que define a função de mapeamento entre
soluções e parâmetros do modelo.
"""

import typing

import numpy as np

from covid_abm import utils


def default_mapper(solution) -> utils.Parameters:
    solution = _solution_to_list(solution)
    int_sol = list(map(round, solution))
    assert len(solution) == 13

    return utils.Parameters(infectious_rate=solution[0],
                            mean_work_interactions_child=int_sol[1],
                            mean_work_interactions_adult=int_sol[2],
                            mean_work_interactions_elderly=int_sol[3],
                            n_seed_infection=int_sol[4],
                            quarantine_length_self=int_sol[5],
                            quarantine_length_traced_symptoms=int_sol[6],
                            quarantine_length_traced_positive=int_sol[7],
                            quarantine_length_positive=int_sol[8],
                            lockdown_time_on=int_sol[9],
                            lockdown_elderly_time_on=int_sol[10],
                            lockdown_time_off=int_sol[11],
                            lockdown_elderly_time_off=int_sol[12])


def _solution_to_list(solution):
    if isinstance(solution, list):
        return solution
    elif isinstance(solution, np.ndarray):
        return solution.tolist()

    return list(solution)
