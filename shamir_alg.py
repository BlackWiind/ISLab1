# Реализация шифра Шамира
from common_algorithms import module_degree, evclid_extended


class ShamirAlg():

    def __init__(self, c: int, p: int):
        self.c = c
        self.p = p
        self.d = None

    def find_d(self) -> int:
        # Находим число d, необходимое для шифра
        value = evclid_extended(self.p, self.c)
        value = value[2] if value[2] > 0 else value[2] + self.p
        self.d = value
        return value


def demonstration(c_a: int, c_b: int, p: int, message: int):
    user_1 = ShamirAlg(c_a, p-1)
    user_2 = ShamirAlg(c_b, p-1)
    user_1.find_d()
    user_2.find_d()
    x1 = module_degree(message, c_a, p)
    x2 = module_degree(x1, c_b, p)
    x3 = module_degree(x2, user_1.d, p)
    x4 = module_degree(x3, user_2.d, p)

    print(f"Шифр Шамира:\n"
          f"Входные данные p= {p}, Сa= {c_a}, Сb= {c_b}\n"
          f"Значение d пользователя А: {user_1.d}\n"
          f"Значение d пользователя Б: {user_2.d}\n"
          f"Сообщение: {message}\n"
          f"X1 = {x1}\n"
          f"X2 = {x2}\n"
          f"X3 = {x3}\n"
          f"X4 = {x4}\n")
