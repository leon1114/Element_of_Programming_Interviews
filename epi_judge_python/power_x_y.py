from test_framework import generic_test

def power(x: float, y: int) -> float:
    if y < 0:
        x,y = 1.0/x, -y
    result, power = 1.0, y
    while power:
        if power & 1:
            result *= x
        x, power = x*x, power >> 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',power))
    # power(2,13)
