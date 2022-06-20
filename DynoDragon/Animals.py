import random
colorset = ["gold", "red", "brown"]

class animal():
    def __init__(self, name, color, weight, wingL, spec, etalonweight, etalonwingL, etaloncolor, basiccost):
        # Ім’я, вага, колір, довжина розмаху крил, ціна, спеціальна особливість
        self.name = name
        self.color = color
        self.weight = weight
        self.wingL = wingL
        self.spec = spec
        self.eweight = etalonweight
        self.ewingL = etalonwingL
        self.ecolor = etaloncolor
        self.basiccost = basiccost
        dw = abs(self.eweight-self.weight)/self.eweight
        if self.ewingL > 0:
            dwL = abs(self.ewingL - self.wingL) / self.ewingL
        else:
            #special formula for dynozaur
            dwL = (self.wingL)/5
        if self.ecolor != self.color:
            dc = 1
        else:
            dc = 0
        perc = (3 - dw - dwL - dc)/3
        self.cost = round(self.basiccost * perc, 1)
    def whoami(self):
        print("class="+self.__class__.__name__, end="\t")
        #print all class variables
        temp = vars(self)
        for item in temp:
            print(item, ':', temp[item], end="\t")
        print("")

class dyno(animal):
    def __init__(self, name, color, weight, wingL):
        animal.__init__(self,name, color, weight, wingL, "hungry", 3250, 0, "brown", 2200000)
        if not ((1500<=weight<=5000)&(0<=wingL<=5)):
            self.cost = self.basiccost
class dragon(animal):
    def __init__(self, name, color, weight, wingL):
        animal.__init__(self, name, color, weight, wingL, "fly", 150, 50, "gold", 3000000)
        if not ((100<=weight<=300)&(30<=wingL<=50)):
            self.cost = self.basiccost
class salamander(animal):
    def __init__(self, name, color, weight, wingL):
        animal.__init__(self, name, color, weight, wingL, "nice", 900, 15, "red", 5000)
        if not ((300<=weight<=1500)&(10<=wingL<=30)):
            self.cost = self.basiccost
class cat(animal):
    def __init__(self, name, color, weight, wingL):
        animal.__init__(self, name, color, weight, wingL, "Kawaii", 12, 0.5, "any", 5000)
        self.cost = self.basiccost

class adapter():
    def check(creature):
        if (200 <= creature.weight <= 600) | (20 <= creature.wingL <= 40):
            xcat = cat(creature.name, colorset[random.randrange(0, 2)], random.randrange(100, 6000), 0.5)
            temp = xcat #animal will be CAT class
            del creature #delete source animal (empty memory from it)
        else:
            temp = creature #animal params are OK - we do not create CAT
        return temp

class fabric:
    def createit(self, name):
        kinder = 0
        while kinder == 0:
            color = colorset[random.randrange(0, 2)]
            weight = random.randrange(100, 5000)
            wingL = random.randrange(0, 60)
            if weight <= 300:
                kinder = dragon(name, color, weight, wingL)
            elif wingL <= 5:
                kinder = dyno(name, color, weight, wingL)
            elif color == "red":
                kinder = salamander(name, color, weight, wingL)
            else:
                # bad creature - try new one
                pass
        kinder_after_check = adapter.check(kinder)
        return kinder_after_check
class multi():
    def produce(self, reqdragons, reqdyno, reqsal, reqcat):
        self.totalcost = 0
        self.totaldragons = 0
        self.totalsalamanders = 0
        self.totaldyno = 0
        self.totalcat = 0
        while (self.totaldragons<reqdragons) | (self.totaldyno<reqdyno) | (self.totalsalamanders<reqsal) | (self.totalcat<reqcat):
            x = fabric().createit("-")
            x.whoami()
            if x.__class__.__name__ == "dragon":
                self.totaldragons = self.totaldragons + 1
                if self.totaldragons<=reqdragons:
                    self.totalcost = self.totalcost + x.cost
                else:
                    self.totalcost = self.totalcost + x.cost/3
            if x.__class__.__name__ == "dyno":
                self.totaldyno = self.totaldyno + 1
                if self.totaldyno<=reqdyno:
                    self.totalcost = self.totalcost + x.cost
                else:
                    self.totalcost = self.totalcost + x.cost/3
            if x.__class__.__name__ == "salamander":
                self.totalsalamanders = self.totalsalamanders + 1
                if self.totalsalamanders<=reqsal:
                    self.totalcost = self.totalcost + x.cost
                else:
                    self.totalcost = self.totalcost + x.cost/3
            if x.__class__.__name__ == "cat":
                self.totalcat = self.totalcat + 1
                if self.totalcat<=reqcat:
                    self.totalcost = self.totalcost + x.cost
                else:
                    self.totalcost = self.totalcost + x.cost/3

        #print(str(self.totaldragons) +" "+ str(self.totaldyno)+" "+str(self.totalsalamanders))
        return round(self.totalcost, 1)
class client():
    def run(self):
        self.totalcost = 0
        print("Welcome!")
        res = input("Need new pet or set(y/s/n)? ")
        while res != "n":
            if res == "y":
                x = fabric().createit("-")
                res = input("The " + x.__class__.__name__ + " was born! Give its name: ")
                x.name = res
                x.whoami()
                self.totalcost = self.totalcost + x.cost
            else:
                #setcost = multi().produce(1, 1, 1, 0)
                #setcost = multi().produce(0, 2, 3, 0)
                setcost = multi().produce(0, 0, 0, 7)
                self.totalcost = self.totalcost + setcost
            res = input("Need another pet or set(y/s/n)? ")
        print("Total cost is:"+str(self.totalcost))
        print("Bye!")

dyno1 = dyno("dyno1", "brown", 3250, 5)
dyno1.whoami()
dyno2 = dyno("dyno2", "gold", 3250, 15)
dyno2.whoami()

'''
dyno1 = dyno("dyno1", "brown", 3250, 5)
dyno1.whoami()

dyno2 = dyno("dyno2", "red", 259, 30)
dyno2.whoami()
z = adapter.check(dyno2)
z.whoami()
'''

#x = fabric().createit("-")
#x.whoami()

#shopping = client().run()

#a = animal("dracon1","gold",150,50,"aaaa",150,50,"grrr",3000000)
#a.whoami()

