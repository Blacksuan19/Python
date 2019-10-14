# solve linear equation using gaussian elimination by blacksuan19
import numpy as np


def forward_elimination(coeff, b, n):
    """
    Calculates the forward part of Gaussian elimination.
    """
    for row in range(0, n - 1):
        for i in range(row + 1, n):
            factor = coeff[i, row] / coeff[row, row]
            for j in range(row, n):
                coeff[i, j] = coeff[i, j] - factor * coeff[row, j]

            b[i] = b[i] - factor * b[row]
        print('coeff = \n%s \nright_side = %s\n' % (coeff, b))
    return coeff, b


def back_substitution(a, b, n):
    """"
    Does back substitution, returns the Gauss result.
    """
    result = np.zeros((n, 1))
    result[n-1] = b[n-1] / a[n-1, n-1]
    for row in range(n-2, -1, -1):
        sums = b[row]
        for j in range(row+1, n):
            sums = sums - a[row, j] * result[j]
        result[row] = sums / a[row, row]
    return result


def gauss(coeff, b):
    """
    This function performs Gauss elimination without pivoting.
    """
    n = coeff.shape[0]

    # Check for zero diagonal elements
    if any(np.diag(coeff) == 0):
        raise ZeroDivisionError(('Division by zero will occur; '
                                 'pivoting currently not supported'))

    coeff, right_side = forward_elimination(coeff, b, n)
    return back_substitution(coeff, b, n)


# the coefficents array
coeff = np.array([[1, 5, 1],
                 [1, -2, -2],
                 [1, 4, -4]])

# the right side array
right_side = np.array([0, 4, 2])
result = gauss(coeff, right_side)

print('Gauss result is: \n')
print('X = ', str(result[0]).replace("[", "").replace("]", ""),
      '\nY = ', str(result[1]).replace("[", "").replace("]", ""),
      '\nZ = ', str(result[2]).replace("[", "").replace("]", ""))
