from numpy import sqrt
x = 2
y = 3

def pytagoras(a, b):
    return sqrt(a**2+b**2)

def test_pytagoras():
    tolerance = 1e-10

    computed = pytagoras(3,4)
    expected = 5
    success = abs(expected - computed[0]) < tol
    msg = "Something went wrong!"
    assert success, msg

test_pytagoras()
