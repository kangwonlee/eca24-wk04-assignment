import math
import pathlib
import random
import sys

from typing import Callable, Generator, Dict, Tuple


import pytest


RESULT = Dict[str, (float | bool)]

file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import wk04


random.seed()


def one_poly_root() -> float:
    return ((0.5 + (random.random()*0.5)) * random.choice((-1, 1)))


def poly_roots() -> Tuple[float]:
    result = [one_poly_root(), one_poly_root()]

    result.sort()

    return tuple(result)


def exp_coef() -> float:
    return (random.random() * 8.0) + 2.0


def get_poly_2(poly_roots:Tuple[float]) -> Callable[[float], float]:
    def poly_2(x:float) -> float:
        return ((x - poly_roots[0]) * (x - poly_roots[1]))
    return poly_2


def get_exp(exp_a:float, exp_b:float) -> Callable[[float], float]:
    def exp(x:float) -> float:
        return exp_a * math.exp(x) + (exp_b * (-1.0))
    return exp


def get_delta_x() -> float:
    return ((random.random() * 0.5) + 0.5)


def get_epsilon() -> float:
    exp = random.randint(6, 8)
    sig = random.randint(1, 9)

    return ((0.1 ** exp) * sig)


def generate_test_cases() -> Generator[RESULT, None, None]:

    for found in (True, False):
        yield (generate_poly_case(found))
        yield (generate_exp_case(found))


def generate_poly_case(found:bool):
    p_roots = poly_roots()

    delta_x = get_delta_x()

    d_poly = {
            'found': found,
            'x': p_roots[0],
            'delta_x': delta_x,
            'f': get_poly_2(p_roots),
            'epsilon': get_epsilon(),
        }

    if not found:
        d_poly['x'] += ((-10.0) * delta_x)

    d_poly['xp'] = (d_poly['x'] - d_poly['delta_x'])
    return d_poly


def generate_exp_case(found:bool):
    exp_a = exp_coef()
    exp_b = exp_a * exp_coef()

    exp_root = math.log(exp_b / exp_a)

    delta_x = get_delta_x()

    d_exp = {
            'found': found,
            'x': exp_root,
            'delta_x': delta_x,
            'f': get_exp(exp_a, exp_b),
            'epsilon': get_epsilon(),
        }

    if not found:
        d_exp['x'] += ((-10.0) * delta_x)

    d_exp['xp'] = (d_exp['x'] - d_exp['delta_x'])
    return d_exp


@pytest.fixture
def result_expected(request) -> Tuple[RESULT]:
    d = request.param
    d_result = wk04.wk04(
        d['f'],
        d['xp'],
        d['delta_x'],
        d['epsilon'],
    )
    d_expected = {
        'x':d['x'],
        'found':d['found'],
    }

    return (d_result, d_expected)


@pytest.mark.parametrize("result_expected", generate_test_cases(), indirect=True)
def test_check_values(result_expected:Tuple[RESULT]):
    result, expected = result_expected

    assert (result is not None), f"return value is None"

    assert (len(result) == len(expected)), (
        f"return value size={len(result)}, expected size = {len(expected)}"
    )

    assert (result.keys() == expected.keys()), (
        f"return value keys={result.keys()}, expected keys = {expected.keys()}"
    )

    assert math.isclose(
        result['x'], expected['x']
    ), f"expected x = {expected['x']}, result x = {result['x']}"
    assert (result['found'] == expected['found']), (
        f"expected found = {expected['found']}, result found = {result['found']}"
    )


if "__main__" == __name__:
    pytest.main([__file__])
