import unittest
from dh_alg import DHalg

message = "Супер секретное сообщение"


class TestDiffieHellman(unittest.TestCase):

    def setUp(self) -> None:
        p = 30803
        g = 2
        x_a = 1000
        x_b = 2000

        self.user_1 = DHalg(x_a, p, g)
        self.user_2 = DHalg(x_b, p, g)

    def test_create_open_key(self):
        self.assertEqual(self.user_1.create_open_key(), 11971)

    def test_create_full_keys(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())
        self.assertEqual(self.user_1.full_key, self.user_2.full_key, 6830)

    def test_encrypt(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())
        self.assertEqual(self.user_1.encrypt_message(message),
                         "ỏựửợỮᫎữợỨỮợỰừỬợᫎữỬỬởỷợừỦợ")

    def test_decrypt(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())

        self.assertEqual(self.user_2.decrypt_message("ỏựửợỮᫎữợỨỮợỰừỬợᫎữỬỬởỷợừỦợ"),
                         message)


if __name__ == "__main__":
  unittest.main()