# Реализация шифра Эль-Гамаля
from common_algorithms import module_degree


class ElgamalAlg():

    def __init__(self, privat_key: int, k: int, p: int, g: int):
        self.privat_key = privat_key
        self.k = k
        self.p = p
        self.g = g
        self.open_key = None

    def create_open_key(self) -> int:
        # Вычисляем открытый ключ
        value = module_degree(self.g, self.privat_key, self.p)
        self.open_key = value
        return value

    def encrypt_message(self, open_key: int, message: int) -> tuple:
        # Шифровка сообщения, open_key от получателя
        encrypted_message = (
            module_degree(self.g, self.k, self.p),
            module_degree(open_key, self.k, self.p, message)
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message: tuple) -> int:
        decrypted_message = module_degree(encrypted_message[0],
                                             self.p - 1 - self.privat_key,
                                             self.p, encrypted_message[1])
        return decrypted_message


def demonstration(c: int, k: int, p: int, g: int, message):
    user_1 = ElgamalAlg(c, k, p, g)
    user_2 = ElgamalAlg(c, k, p, g)
    user_2.create_open_key()
    encrypted_message = user_1.encrypt_message(user_2.open_key, message)
    decrypted_message = user_2.decrypt_message(encrypted_message)

    print(f"Алгоритм Диффи-Хелмана:\n"
          f"Входные данные p= {p}, g= {g}, k(a) = {k}, c(b) = {c}\n"
          f"Сообщение: {message}\n"
          f"Открытый ключ пользователя Б: {user_2.open_key}\n"
          f"Пользователю А открытый ключ в данном примере не нужен\n"
          f"Используя открытый ключ пользователя Б ползователь А "
          f"получает (e,r): {encrypted_message}\n"
          f"Пользователь Б расшифровывает: {decrypted_message}\n")