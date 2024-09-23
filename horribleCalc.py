# This is the worst calculator you have ever seen
class horribleCalc:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #gets numbers x and y
    def math1(self):
        # check if x + y is equal to x + y
        if (self.x + self.y == self.x + self.y):
            # if x + y = x + y, do x + y = z
            z = self.x + self.y
            # return z
            return z

    def math2(self):
        if(self.x > 0 and self.y > 0 or self.x < 0 and self.y < 0 ): #wtf is this stupid codw whoever did this should not live on this planet earth anymore jesus christ take this mans computer away good lord
            z = 0
            z = self.x * self.y
            return z

    def isDivision(self):
        return self.x/self.y

class math3(horribleCalc):
    def math4(self):
        return "Divsiosn"

horrible = horribleCalc(2, 3)
print(horrible.math1())
print(horrible.math2())

even_worse = math3(8,2)
print(even_worse.isDivision())
