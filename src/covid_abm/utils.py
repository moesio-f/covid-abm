"""
Módulo de utilidades.
"""

from dataclasses import dataclass, fields


@dataclass(frozen=True)
class Parameters:
    """
    Essa classe representa os parâmetros passados
    ao ABM.
    """
    infectious_rate: float
    n_seed_infection: int
    mean_work_interactions_child: float
    mean_work_interactions_adult: float
    mean_work_interactions_elderly: float
    quarantine_length_self: int
    quarantine_length_traced_symptoms: int
    quarantine_length_traced_positive: int
    quarantine_length_positive: int
    lockdown_time_on: int
    lockdown_elderly_time_on: int
    lockdown_time_off: int
    lockdown_elderly_time_off: int

    def dict(self):
        return {field.name: getattr(self, field.name)
                for field in fields(self)}
