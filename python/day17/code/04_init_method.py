

class Car(object):
    def __init__(self, c, b, m):
        self.color = c
        self.brand = b
        self.model = m

    def set_color(self, clr):
        self.color = clr

a4 = Car('红色','奥迪','A4')
