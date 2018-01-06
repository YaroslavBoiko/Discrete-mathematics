import random
import numpy as np

def generate_matrix(n):

    """
    (number) -> list

    Return random matrix

     >>> generate_matrix(3)
        [[1, 1, 1], [1, 1, 1], [1, 1, 0]]
    """

    return [[random.getrandbits(1)
	   for i in range(n)]
			for j in range(n)]


def All(n):

    """
    (number) -> list

    This function return a list of all possible matrices

    >>> All(2)
        [[[1, 1], [1, 1]], [[1, 0], [1, 0]], [[0, 0], [1, 1]], [[0, 1], [1, 1]], [[1, 0], [0, 0]], [[0, 0], [0, 0]], [[0, 0], [1, 0]], [[1, 1
], [1, 0]], [[1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 1], [0, 0]], [[1, 0], [1, 1]], [[0, 0], [0, 1]], [[1, 1], [0, 1]], [[0, 1], [0,
1]], [[0, 1], [0, 0]]]
    """

    k = n * n
    a = pow(2,k)
    f = 0
    Home = []
    while a > f:
        A = generate_matrix(n)
        if A in Home:
            continue
        else:
            Home = Home + [A]
            f = f + 1
    return Home


def is_transitive(matrix):
# This function checks if the matrix is transitive
# Returns True if the  matrix is transitive and returns False if the matrix is not transitive
	n = len(matrix)
	for i in range(n):
		for j in range(n):
			if matrix[i, j] == 1:
				for k in range(n):
					if (matrix[j, k] == 1) and (matrix[i, k] == 0):
						return False
	return True


def fin(n):

    """
    (number) -> number

    This function returns the number of transitive matrices

    >>>fin(3)
        171
    """

    Home = All(n)
    V = 0
    for i in Home:
        rows = i
        A = np.array(rows)
        B = is_transitive(A)
        if B is False:
            continue
        else:
            V = V + 1
    return V

n = int(input("Enter matrix size : 3 or 4 "))
print("There are")
print(fin(n))
print("transitive matrices")
