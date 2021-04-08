"""
Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi,
non-scalar verilerden de oluşabilir. Örnek olarak:

input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""
from time import time
import sys

# Problemin çözümünde yazdığım fonksiyonların ne kadar sürede çalıştığını ölçmek için
# iç içe çok fazla liste koymam gerekti. Bu durumda da recursion limit hatası aldım.
# Çözmek için sys kütüphanesinden bu limiti biraz daha yükselttim.
sys.setrecursionlimit(10 ** 7)


def flatten(l):
    # Nispeten daha yavaş çalışan versiyonu
    r = []
    for i in l:
        if not isinstance(i, list):
            r.append(i)
        else:
            for j in i:
                r.append(j)

    for i in r:
        if isinstance(i, list):
            return flatten(r)
    return r


def flatten2(l):
    # Daha hızlı çalışan versiyonu
    def f(l, r=[]):
        # r isimli parametrenin her zaman boş bir liste olması için
        # kullanıcı tarafından verilmemesi gerekiyor. Bu yüzden local bir
        # fonksiyonda bütün işlemleri yapıp, asıl fonksiyonu konteynır olarak
        # kullanıyoruz.
        if not isinstance(l, list):
            r.append(l)
        else:
            for i in l:
                f(i, r)
        return r

    return f(l)


l = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten(l))
print(flatten2(l))

# Süre testi 1
for _ in range(10000):
    l = [l]
start = time()
flatten(l)
end = time()
print("Flatten1:", end - start)  # Flatten1: 0.020244121551513672

start = time()
flatten2(l)
end = time()
print("Flatten2:", end - start)  # Flatten2: 0.01397848129272461
