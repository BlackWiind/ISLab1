# Реализация алгоритма шифрования Диффи-Хелмана
from common_algorithms import module_degree


class DHalg():

    def __init__(self, privat_key: int, p: int, g: int):
        self.private_key = privat_key
        self.p = p
        self.g = g
        self.full_key = None

    def create_open_key(self) -> int:
        # Создаёт открытый ключ
        return module_degree(self.g, self.private_key, self.p)

    def create_full_key(self, open_key: int) -> int:
        # Создаёт общий закрытый ключ для шифрования
        full_key = module_degree(open_key, self.private_key, self.p)
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message) -> str:
        # Шифровка сообщения
        encrypted_message = ""
        message = str(message)
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message) -> str:
        # Дешифровка сообщения
        encrypted_message = str(encrypted_message)
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message


def demonstration(x_a: int, x_b: int, p: int, g: int, message):
    user_1 = DHalg(x_a, p, g)
    user_2 = DHalg(x_b, p, g)
    user_1.create_full_key(user_2.create_open_key())
    user_2.create_full_key(user_1.create_open_key())
    encrypted_message = user_1.encrypt_message(message)
    decrypted_message = user_2.decrypt_message(encrypted_message)

    print(f"Алгоритм Диффи-Хелмана:\n"
          f"Входные данные p= 30803, g= 2, Xa= 1000, Xb= 2000\n"
          f"Открытый ключ пользователя А: {user_1.create_open_key()}\n"
          f"Открытый ключ пользователя Б: {user_2.create_open_key()}\n"
          f"Общий секретный ключ: {user_2.full_key}\n"
          f"Пользователь А шифрует сообщение: {encrypted_message}\n"
          f"Пользователь Б расшифровывает: {decrypted_message}\n")