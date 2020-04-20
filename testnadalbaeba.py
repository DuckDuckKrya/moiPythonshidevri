import time
from random import randint

print("segodnya mi uznaem na skolko ti dalbaeb")
time.sleep(1)
print("i tak pristupim")
time.sleep(1)
print("vischislyau na skolko ti dalbaeb")
time.sleep(1)
print("taaaaak echo chut chut")
print("zavershaem")
time.sleep(1)
k = randint(0, 100)
print("vi dalbaeb na", k, '%')
if k == 0:
    print("ebat da ti voobche ne dalbaeb")
else:
    if k > 50 and k != 1:
        print("ebat vi dalbaeb")
    else:
        print("pozdravlyaem vi chut chut dalabeb ne sovsem koroche")
