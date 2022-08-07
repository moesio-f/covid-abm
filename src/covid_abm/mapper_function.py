"""
Módulo que define a função de mapeamento entre
soluções e parâmetros do modelo.
"""

import numpy as np

from covid_abm import utils


def default_mapper(solution) -> utils.Parameters:
    return utils.Parameters(infectious_rate=1,
                            n_seed_infection=1,
                            mean_work_interactions_child=1,
                            mean_work_interactions_adult=1,
                            mean_work_interactions_elderly=1,
                            quarantine_length_self=1,
                            quarantine_length_traced_symptoms=1,
                            quarantine_length_traced_positive=1,
                            quarantine_length_positive=1,
                            lockdown_time_on=1,
                            lockdown_elderly_time_on=1,
                            lockdown_time_off=1,
                            lockdown_elderly_time_off=1,
                            successive_lockdown_duration=1,
                            successive_lockdown_gap=1,
                            successive_lockdown_time_on=1)
