from dh_alg import demonstration as dh_demo
from shamir_alg import demonstration as sham_demo


message: str = "Супер секретное сообщение"
message_int: int = 11111


dh_demo(1000, 2000, 30803, 2, message)
sham_demo(501, 601, 30803, message_int)




