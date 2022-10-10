from dh_alg import demonstration as dh_demo
from shamir_alg import demonstration as sham_demo
from elgamal_alg import demonstration as elgamal_demo
from rsa_alg import demonstration as rsa_demo


MESSAGE: str = "Супер секретное сообщение"
MESSAGE_INT: int = 11111
P_CONST: int = 30803
G_CONST: int = 2


dh_demo(1000, 2000, P_CONST, G_CONST, MESSAGE)
sham_demo(501, 601, P_CONST, MESSAGE_INT)
elgamal_demo(600, 500, P_CONST, G_CONST, MESSAGE_INT)
rsa_demo(131, 227, 3, MESSAGE_INT)

