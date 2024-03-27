def SubsetSum(A: list, T: int) -> bool:
    n = len(A)
    X = [[False for t in range(T + 1)] for i in range(n + 1)]

    for t in range(T + 1):
        X[n][t] = t == A[-1]

    for i in reversed(range(n)):
        for t in range(T + 1):
            X[i][t] = any([X[i + 1][t], X[i + 1][t - A[i]] if (t >= A[i]) else False])

    return X[0][T]


if __name__ == "__main__":
    A = [1, 3, 4, 12, 19, 21, 22]
    print("A: ", A)
    for T in [2, 6, 9, 10, 11, 47]:
        print(
            "T: {},\tSubsetSum(A, T)? {}".format(T, "YES" if SubsetSum(A, T) else "NO")
        )
