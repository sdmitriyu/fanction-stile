def isprime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print("Составное")
        else:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    return
            print("Простое")
        return result
    return wrapper

@isprime
def sumthree(a, b, c):
    return a + b + c

result = sumthree(2, 3, 6)
print(result)
