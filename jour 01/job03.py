class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(f"{self.nombre1} + {self.nombre2} = {self.nombre1 + self.nombre2}")

if __name__ == "__main__":
    op = Operation(12, 3)
    op.addition()