def min_movimentos(X1, Y1, X2, Y2):
    if (X1, Y1) == (X2, Y2):
        return 0
    elif X1 == X2 or Y1 == Y2 or abs(X2 - X1) == abs(Y2 - Y1):
        return 1
    else:
        return max(abs(X2 - X1), abs(Y2 - Y1))

X1, Y1, X2, Y2 = map(int, input().split())
print(min_movimentos(X1, Y1, X2, Y2))
