import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {}
for i in range(100):
    sock = random.choice(sock_types)
    
    socks[sock] = socks.get(sock, 0) + 1

print(socks)

for sock in sock_types:
    pairs = socks[sock] // 2
    loners = socks[sock] % 2
print(f'{pairs} pairs and {loners} loners.')