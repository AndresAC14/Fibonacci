import argparse


def fibonacci(n: int) -> int:
    """
    Computes de n-th Fibonacci number.
    :param n: n-th Fibonacci number.
    :return: the n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("NOOOOOO")
    if n < 2:
        return n

    if n in cache:
        return cache[n]

    nth = fibonacci(n - 1) + fibonacci(n - 2)

    cache[n] = nth

    return nth


########################################################
'''
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("NOOOOOO")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    nth = 0
    for _ in range(n):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return nth
'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Fibonacci',
                                     description='Calculates the n-th Fibonacci number')
    parser.add_argument('n', type=int, help="N-th Fib number")
    args = parser.parse_args()

    cache = {}
    res = fibonacci(args.n)
    print(res)
