def triangle(n=5):
    if n > 0:
        for line in range(1, n + 1):
            print("#" * line)
    else:
        n *= -1
        for line in range(n, 0, -1):
            print("#" * line)
