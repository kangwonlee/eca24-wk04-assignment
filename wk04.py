# 이 파일을 수정하여 제출하시오.
def wk04(


def sequential(f, x_start, x_end, delta_x, epsilon=1e-6,):
    xp = x_start

    while True:
        d = f(f, xp, delta_x, epsilon)

        if d['found']:
            break
        elif d['xi'] > x_end:
            d['xi'] = 'not found'
            break
        else:
            xp = d['xi']

    return d['xi']


def poly(x):
    return x * x - 20


def main():
    x = sequential(poly, 4, 5, 1e-6)
    print(f"f({x:f}) = {f(x):f} is close to zero.")


if "__main__" == __name__:
    main()
