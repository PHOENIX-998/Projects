a = []
b = []
c = []
class Myclass:
    def add(n):
        for i in range(n):
            a.append(i)
            b.append(i)
            c.append(i+i)
        return a,b,c