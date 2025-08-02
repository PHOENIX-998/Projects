class Myclass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Myclass("Rajarshi",21)
print(p1)