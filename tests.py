import unittest

import common_algorithms
from dh_alg import DHalg
from shamir_alg import ShamirAlg
from elgamal_alg import ElgamalAlg
from rsa_alg import RSAAlg

MESSAGE = "Супер секретное сообщение"
INT_MESSAGE = 11111


class TestCommonAlgorithms(unittest.TestCase):

    def test_module_degree(self):
        self.assertEqual(common_algorithms.module_degree(5, 11, 23), 22)

    def test_module_inversion(self):
        self.assertEqual(common_algorithms.module_inversion(3, 11), 4)

    def test_evclid_extended(self):
        self.assertEqual(common_algorithms.evclid_extended(28, 19), (1, -2, 3))


class TestDeffiHellman(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = DHalg(1000, 30803, 2)
        self.user_2 = DHalg(2000, 30803, 2)
        self.user_1.create_full_key(self.user_2.open_key)
        self.user_2.create_full_key(self.user_1.open_key)

    def test_decrypt_str(self):
        encrypted_message = self.user_1.encrypt_message(MESSAGE)
        self.assertEqual(self.user_2.decrypt_message(encrypted_message),
                         MESSAGE)

    def test_decrypt_int(self):
        encrypted_message = self.user_2.encrypt_message(INT_MESSAGE)
        self.assertEqual(self.user_1.decrypt_message(encrypted_message),
                         str(INT_MESSAGE))


class TestShamir(unittest.TestCase):

    def setUp(self) -> None:
        self.p = 30803
        self.user_1 = ShamirAlg(501, self.p-1)
        self.user_2 = ShamirAlg(601, self.p-1)
        self.p2 = 23
        self.user_3 = ShamirAlg(7, self.p2 - 1)
        self.user_4 = ShamirAlg(5, self.p2 - 1)

    def test_shamir_decrypt_1(self):
        value = common_algorithms.module_degree(INT_MESSAGE, self.user_1.c, self.p)
        value = common_algorithms.module_degree(value, self.user_2.c, self.p)
        value = common_algorithms.module_degree(value, self.user_1.d, self.p)
        value = common_algorithms.module_degree(value, self.user_2.d, self.p)
        self.assertEqual(INT_MESSAGE, value)

    def test_shamir_decrypt_2(self):
        value = common_algorithms.module_degree(10, self.user_3.c, self.p2)
        value = common_algorithms.module_degree(value, self.user_4.c, self.p2)
        value = common_algorithms.module_degree(value, self.user_3.d, self.p2)
        value = common_algorithms.module_degree(value, self.user_4.d, self.p2)
        self.assertEqual(10, value)

class TestElgamal(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = ElgamalAlg(13, 7, 23, 5)
        self.user_2 = ElgamalAlg(500, 600, 30803, 2)

    def test_elgamal_decrypt_1(self):
        encrypted_message = self.user_1.encrypt_message(self.user_1.open_key, 15)
        self.assertEqual(15, self.user_1.decrypt_message(encrypted_message))

    def test_elgamal_decrypt_2(self):
        encrypted_message = self.user_2.encrypt_message(self.user_2.open_key, INT_MESSAGE)
        self.assertEqual(INT_MESSAGE, self.user_2.decrypt_message(encrypted_message))


class TestRSA(unittest.TestCase):

    def setUp(self) -> None:
        self.user_1 = RSAAlg(3, 11, 3)
        self.user_2 = RSAAlg(131, 227, 3)

    def test_decrypt_1(self):
        encrypted_message = self.user_1.encrypt_message(self.user_1.open_key, 15)
        self.assertEqual(self.user_1.decrypt_message(encrypted_message),
                         15)

    def test_decrypt_2(self):
        encrypted_message = self.user_2.encrypt_message(self.user_2.open_key, INT_MESSAGE)
        self.assertEqual(self.user_2.decrypt_message(encrypted_message),
                         INT_MESSAGE)


if __name__ == "__main__":
    unittest.main()
