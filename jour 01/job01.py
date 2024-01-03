
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

def __repr__(self):
        return f'<{self.__class__.__name__} object at {hex(id(self))}>'

if __name__ == "__main__":
    
op_i = Operation(12, 3)   

print(op_i)