from dh_alg import demonstration as dh_demo
from shamir_alg import demonstration as sham_demo
from elgamal_alg import ElgamalAlg


message: str = "Супер секретное сообщение"
message_int: int = 11111


dh_demo(1000, 2000, 30803, 2, message)
sham_demo(501, 601, 30803, message_int)

test = ElgamalAlg(1, 7, 23, 5)
test2 = ElgamalAlg(13, 7, 23, 5)

test2.find_open_key()
print(test2.open_key)
m = test.encrypt_message(test2.open_key, 15)
print(m)
print(test2.decrypt_message(m))

