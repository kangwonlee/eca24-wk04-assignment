import pathlib
import random
import sys

from typing import List, Tuple


import numpy as np
import numpy.random as nr
import pandas as pd
import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import wk03


random.seed()


@pytest.fixture
def n() -> int:
    return random.randint(5, 8)


@pytest.fixture
def a() -> float:
    return (random.random() - 0.5) * 4


@pytest.fixture
def expected(n) -> np.ndarray:
    return (nr.randint(-32, 31, (n,)) * 1.0)


@pytest.fixture
def x(expected:np.ndarray, a:float) -> Tuple[float]:
    return tuple((expected / a).tolist())


@pytest.fixture
def result(a:float, x:Tuple[float]) -> List[float]:
    return wk03.wk03(a, x)


def test_wk03(result:int, a:Tuple[int], x:Tuple[int], expected:int):
    df = pd.DataFrame(
        data={'result': result, 'expected': expected},
        columns=['result', 'expected']
    )
    df['is close'] = np.isclose(df['result'], df['expected'])
    message = (
        f"a={a}, x={x}\n"
        f"{df}\n"
    )

    assert all(df['is close']), message
