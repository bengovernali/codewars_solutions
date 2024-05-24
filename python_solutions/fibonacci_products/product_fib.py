def product_fib(_prod):
    fibs = [0, 1]
    n = 2
    while fibs[-1] * fibs[-2] < _prod:
        fibs.append(fibs[n-1] + fibs[n-2])
        n += 1
    if fibs[-1] * fibs[-2] == _prod:
        return [fibs[-2], fibs[-1], True]
    else:
        return [fibs[-2], fibs[-1], False]