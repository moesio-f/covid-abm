"""
Módulo de utilidades.
"""

import os
import pathlib
from dataclasses import dataclass, fields

_FPATH: pathlib.Path = pathlib.Path(__file__).parent.resolve()
_SRC_PATH: pathlib.Path = _FPATH.parent.resolve()
_ROOT: pathlib.Path = _SRC_PATH.parent.resolve()
_DATA_PATH: pathlib.Path = _ROOT.joinpath('data/')
_PARAMS: pathlib.Path = _DATA_PATH.joinpath('params.csv')
_RESULTS_DIR = _ROOT.joinpath('results/')


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

    def dict(self):
        return {field.name: getattr(self, field.name)
                for field in fields(self)}
