def check_if_in_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

num = int(input())
print(check_if_in_fibonacci(num))