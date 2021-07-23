class Cars():
    def __init__(self, brand, color, plates, speed_limit, company):
        self.brand = brand
        self.color = color
        self.plates = plates
        self.speed_limit = speed_limit
        self.company = company
    
    def carStart(self):
        print("started")

    def carStop(self):
        print("stop")
    
    def accelerate(self, speed_limit):
        print(self.speed_limit)

    def repaint(self, color):
        print(self.color)

camaro = Cars("Camaro", "red", "123456", 90, "Chevrolet")

print(camaro.carStart())
print(camaro.carStop())
print(camaro.accelerate(80))
print(camaro.repaint("red"))