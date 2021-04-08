"""
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın.
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""


def tersimPistir(l):
    return l if not isinstance(l, list) else [tersimPistir(i) for i in l[::-1]]


l = [[1, 2], [3, 4], [5, 6, 7]]
print(tersimPistir(l))
