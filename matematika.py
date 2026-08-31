def prima(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def akar(n):
    return n ** 0.5

def ganjil_genap(n):
    return n % 2 == 0