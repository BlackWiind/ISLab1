# Реализация шифра Эль-Гамаля, шифрует только целые числа
from common_algorithms import module_degree


class ElgamalAlg:

    def __init__(self, privat_key: int, k: int, p: int, g: int):
        self.privat_key = privat_key
        self.k = k
        self.p = p
        self.g = g
        self.open_key = module_degree(self.g, self.privat_key, self.p)

    def encrypt_message(self, open_key: int, message: int) -> tuple:
        # Шифровка сообщения, open_key от получателя
        encrypted_message = (
            module_degree(self.g, self.k, self.p),
            module_degree(open_key, self.k, self.p, message)
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message: tuple) -> int:
        # Расшифровка сообщения
        decrypted_message = module_degree(encrypted_message[0],
                                             self.p - 1 - self.privat_key,
                                             self.p, encrypted_message[1])
        return decrypted_message


def demonstration(c: int, k: int, p: int, g: int, message):
    user_1 = ElgamalAlg(c, k, p, g)
    encrypted_message = user_1.encrypt_message(user_1.open_key, message)
    decrypted_message = user_1.decrypt_message(encrypted_message)

    print(f"Алгоритм Диффи-Хелмана:\n"
          f"Входные данные p= {p}, g= {g}, k(a) = {k}, c(b) = {c}\n"
          f"Сообщение: {message}\n"
          f"Открытый ключ: {user_1.open_key}\n"
          f"Зашифрованное сообщение(r, e): {encrypted_message}\n"
          f"Расшифрованное сообщение: {decrypted_message}\n")