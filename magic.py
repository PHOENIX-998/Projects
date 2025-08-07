# Global variables initialised
namedata = []
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
        if self.name in [n for n,_ in namedata]:
            print(self.name,self.age)
if __name__ == "__main__":
    name = str(input("Enter the name:\n"))
    age = int(input("Enter the age:\n"))
    obj = person_details(name,age)
    obj.enterdata()
    obj.print_details()