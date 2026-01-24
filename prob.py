def P(S, A):
    """
    Returns the probability as the ratio of the length of A to S if A is a subset of S, else 0.
    S: list or set
    A: list or set
    """
    if set(A).issubset(set(S)):
        return len(A) / len(S)
    else:
        return 0


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5]
    A1 = [2, 3]
    A2 = [6]
    A3 = [1, 2, 3, 4, 5]
    print(P(S, A1))  # Output: 0.4
    print(P(S, A2))  # Output: 0
    print(P(S, A3))  # Output: 1.0