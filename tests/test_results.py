import math
import pathlib
import random
import sys
import unittest.mock

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


import main


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
        yield (generate_lin_case(found))


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


def generate_lin_case(found:bool):
    '''
    To understand epsilon used correctly
    '''
    a = random.random() * 5.0 + 5.0
    b = random.random() * 0.5 + (-1.0)

    x_root = ((-b)/a)

    delta_x = get_delta_x()

    d_exp = {
            'found': found,
            'x': x_root,
            'xp': x_root - delta_x,
            'delta_x': delta_x,
            'epsilon': get_epsilon(),
        }

    if found:
        d_exp['f'] = lambda x: a * x + b
    else:
        d_exp['f'] = lambda x: a * x + (b + d_exp['epsilon'] * 1.2)

    return d_exp


@pytest.fixture
def result_expected(request) -> Tuple[RESULT]:
    d = request.param
    d_result = main.wk04(
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

    assert result.keys() == expected.keys() and len(result) == len(expected) and \
           math.isclose(result['x'], expected['x']) and (result['found'] == expected['found']), (
            f"Incorrect return value:\n"
            f"  Expected keys: {expected.keys()}\n"
            f"  Actual keys: {result.keys()}\n"
            f"  Expected size: {len(expected)}\n"
            f"  Actual size: {len(result)}\n"
            f"  Expected x: {expected['x']}\n"
            f"  Actual x: {result['x']}\n"
            f"  Expected found: {expected['found']}\n"
            f"  Actual found: {result['found']}"
        )

    assert math.isclose(
        result['x'], expected['x']
    ), f"expected x = {expected['x']}, result x = {result['x']}"
    assert (result['found'] == expected['found']), (
        f"expected found = {expected['found']}, result found = {result['found']}"
    )


@pytest.mark.parametrize(
    "epsilon, expected_calls",
    [
        (1e-2, 1),  # Large epsilon
        (1e-8, 1),  # Smaller epsilon
    ]
)
def test_single_iteration(epsilon, expected_calls):
    mock_f = unittest.mock.MagicMock(return_value=0.5)

    _ = main.wk04(mock_f, 1.0, 0.5, epsilon)  # Use arbitrary xp, delta_x

    assert mock_f.call_count == expected_calls, (
        f"Expected {expected_calls} calls to f with epsilon={epsilon}, but got {mock_f.call_count}.\n"
        f"예상 f 호출 횟수는 {expected_calls}번이지만, 실제노는 {mock_f.call_count}회 호출됨, 주어진 epsilon={epsilon}.\n"
    )


if "__main__" == __name__:
    pytest.main([__file__])
