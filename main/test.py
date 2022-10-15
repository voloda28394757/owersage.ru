a=10
b="hello"
c=[]
d=True
x={"key":"value", "key2":"value2"}
y=(1,2,3)
z={1,3,2,2}


class Kat:
    def __init__(self, name, color, age):
        self.name=name
        self.color=color
        self.age=age
    def music(self):
        print("may")
    def eat(self):
        print("am am am")

class Cyber_kat(Kat):
    def __init__(self, name, color, age, power, time):
        super().__init__(name, color, age)
        self.power=power
        self.time=time
    def stats(self):
        print(f"power: {self.power} time: {self.time}") 


g=Cyber_kat("барсик2.0", "silver", 100, 10000, 360000)
g.music()
g.stats()
w=Kat("барсик", "белый", 3)
v=Kat("дуся", age=14, color="черный")
print(v.name)
v.music()
w.eat()
print(w.name)


