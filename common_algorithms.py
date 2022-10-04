def module_degree(a, n, m: int) -> int:
    # Возведение в степень по модулю
    return (a ** n) % m


def module_inversion(a, c: int) -> int:
    # Обратная инверсия по модулю
    for i in range(c):
        if (a * i) % c == 1:
            answer = i
    if answer:
        return answer


def evclid_extended(num1, num2: int) -> int:
    # Обобщенный алгоритм Евклида
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = evclid_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)
