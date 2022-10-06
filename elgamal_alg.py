# Реализация шифра Эль-Гамаля
from common_algorithms import module_degree


class ElgamalAlg():

    def __init__(self, privat_key: int, k: int, p: int, g: int):
        self.privat_key = privat_key
        self.k = k
        self.p = p
        self.g = g
        self.open_key = None

    def find_open_key(self) -> int:
        # Находим число открытый ключ
        value = module_degree(self.g, self.privat_key, self.p)
        self.open_key = value
        return value

    def encrypt_message(self, open_key: int, message: int) -> tuple:
        # Шифровка сообщения, open_key от получателя
        encrypted_message = (
            module_degree(self.g, self.k, self.p),
            module_degree(message * open_key, self.k, self.p)
        )
        return encrypted_message

    def decrypt_message(self, encrypted_message: tuple) -> int:
        decrypted_message = module_degree(encrypted_message[1] * encrypted_message[0],
                                             self.p - 1 - self.privat_key,
                                             self.p)
        return decrypted_message
