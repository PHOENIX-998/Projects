# Global variables initialised
namedata = []
age = []
class database:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def enterdata(self):
        if self.name not in [n for n, _ in namedata]:
            namedata.append((self.name,self.age))
        else:
            print(f"Name is already inside the database\n printing {self.name} details......\n")
class person_details(database):
    def print_details(self):

