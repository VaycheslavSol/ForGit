class TCat:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed

    def getname(self):
        return self._name

    def getage(self):
        return self._age

    def getbreed(self):
        return self._breed

    def find(self, ag = 5):
        if self._age < ag:
            return True
        else:
            return False




a = TCat("Vasya", 1, "pers")
b = TCat("Ivan", 18, "Mencun")
c = TCat("Masha", 12, "D")
d = TCat("Lena", 3, "V")
e = TCat("Tom", 3, "C")


#print(a.getname(), a.getage(), a.getbreed())
#print(b.getname(), b.getage(), b.getbreed())
#print(c.getname(), c.getage(), c.getbreed())

#cats = [a.getname(), b.getname(), c.getname()]
#for i in range(len(cats)):
 #   print(cats[i])

#ages = [a.find(), b.find(), c.find(), d.find(), e.find()]
#for i in range(len(ages)):
 #   print(ages[i])

