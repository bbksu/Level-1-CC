def detect_three(num_a=2, num_b=1):
    digit = str(3)
    add = num_a + num_b
    add = str(add)

    if digit in add and (num_b == 3 or num_a == 3):
        return True
    else:
        return False
