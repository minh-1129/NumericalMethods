def f(x:float):
    pass


def diff(f, x: float,  tol: float) -> float:
    """
    Tra ve uoc luong dao ham f tai x
    """
    return (f(x + tol) - f(tol)) / tol
    #return (f(x+tol) - f(x-tol)/2tol)


def partial_diff(f, x: list, id: int, tol: float) -> float:
    """
    Tra ve uoc luong dao ham ham nhieu bien f tai x[id]
    """
    f0 = f
    for i in range(len(x)):
        f = f(x[i])
        if i == id:
            f0 = f0(x[i] + tol)
        else:
            f0 = f0(x[i])
    return (f0 - f) / tol



def cumulative_error_direct_solver(f, x, x_abs_err, tol: float) -> float:
    """
    Giai bai toan thuan:
    Tim sai so tuyet doi cua y = f(x), biet x va sai so tuyet doi cua x
    f: ham mot bien hoac da bien
    x: mot so hoac day cac so neu f la ham da bien
    x_abs_err: sai so tuyet doi cua bien hoac cac bien
    tol: tolerance
    """
    if (type(x) == float):
        x = [x]
        x_abs_err = [x_abs_err]

    res = 0
    for i in range(len(x)):
        res += abs(diff(f, x[i], tol)) * x_abs_err[i]
    return res


def cumulative_error_inverse_solver(f, x, y_abs_err, tol: float):
    """
    Giai bai toan nguoc
    Tim can tren cua sai so tuyet doi cua x, biet x va sai so tuyet doi cua y = f(x)
    f: ham mot bien hoac da bien
    x: mot so hoac day cac so neu f la ham da bien
    y_abs_err: sai so tuyet doi cua y = f(x)
    tol: tolerance

    neu f la ham da bien, tra ve day cac sai so tuong ung cac bien
    """
    if (type(x) == float):
        return y_abs_err / diff(f, x, tol)

    res = list()
    n = len(x)
    for i in range(len(x)):
        res.append(y_abs_err / (n * partial_diff(f, x, i, tol)))
    return res

