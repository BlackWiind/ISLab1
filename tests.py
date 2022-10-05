import unittest
from dh_alg import DHalg
from shamir_alg import ShamirAlg

message = "Супер секретное сообщение"
int_message = 1111111


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

    def test_encrypt_str(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())
        self.assertEqual(self.user_1.encrypt_message(message),
                         "ỏựửợỮᫎữợỨỮợỰừỬợᫎữỬỬởỷợừỦợ")

    def test_encrypt_int(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())
        self.assertEqual(self.user_1.encrypt_message(int_message),
                         "᫟᫟᫟᫟᫟᫟᫟")

    def test_decrypt_str(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())

        self.assertEqual(self.user_2.decrypt_message("ỏựửợỮᫎữợỨỮợỰừỬợᫎữỬỬởỷợừỦợ"),
                         message)

    def test_decrypt_int(self):
        self.user_1.create_full_key(self.user_2.create_open_key())
        self.user_2.create_full_key(self.user_1.create_open_key())

        self.assertEqual(self.user_2.decrypt_message("᫟᫟᫟᫟᫟᫟᫟"),
                         str(int_message))

    def tearDown(self) -> None:
        pass


class TestShamir(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = ShamirAlg(7, 11)
        self.user_2 = ShamirAlg(7, 11)

    def test_find_d(self):
        self.assertEqual(self.user_1.find_d(), 8)


if __name__ == "__main__":
  unittest.main()