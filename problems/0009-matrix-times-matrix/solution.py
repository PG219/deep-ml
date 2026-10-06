def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]]:
    if not a or not b or len(a[0]) != len(b):
        return -1

    rows_a = len(a)
    cols_a = len(a[0]) 
    cols_b = len(b[0])

    result = []
    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            dot_product = sum(a[i][k] * b[k][j] for k in range(cols_a))
            row_result.append(dot_product)
        result.append(row_result)

    return result