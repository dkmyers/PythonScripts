class Vector2D:
    x = 0
    y = 0
    def __init__(self, givenX, givenY):
        self.x = givenX
        self.y = givenY
    def printV(self):
        print("X:", str(self.x), "| Y:", str(self.y))
