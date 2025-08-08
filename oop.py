# oop.py
a = []
b = []
c = []

class Myclass:
    @staticmethod
    def multiply(n):
        for i in range(n):
            for j in range(n):
                a.append(i)
                b.append(j)
                c.append(i * j)
        return a, b, c
