
def fibonacci(n): # A função retornará True se o numero for da sequencia de Fibonacci e falso caso não seja
    a = 0
    b = 1
    while b < n:
        c = a
        a = b
        b = c + b
    return n == b

print(fibonacci(21))