class Dice:
    def __init__(self,a,b,c,d,e,f):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e = e
        self.f =f

    def rot(self,way):

        if(way == "W"):
            tmp = self.a
            self.a=self.c
            self.c=self.f
            self.f=self.d
            self.d=tmp

        elif way == "E":
            cc = self.a
            self.a = self.d
            self.d=self.f
            self.f=self.c
            self.c=cc

        elif way=="S":
            cc = self.a
            self.a=self.e
            self.e=self.f
            self.f=self.b
            self.b=cc

        elif way=="N":
            cc = self.a
            self.a=self.b
            self.b=self.f
            self.f=self.e
            self.e=cc

    def prin(self):
         print(self.a)


a,b,c,d,e,f = map(int, input().split())

dice = Dice(a,b,c,d,e,f)

for i in range(int(input())):
    x1, x2 = map(int, input().split())
