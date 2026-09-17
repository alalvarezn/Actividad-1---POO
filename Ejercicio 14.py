class NumeroOperaciones:

    def __init__(self, numero):
        self.numero = numero
        self.cuadrado = 0
        self.cubo = 0

    def calcular_cuadrado(self):
        self.cuadrado = self.numero ** 2
        return self.cuadrado

    def calcular_cubo(self):
        self.cubo = self.numero ** 3
        return self.cubo

    def mostrar_resultados(self):
        print("Numero:", self.numero)
        print("Cuadrado:", self.cuadrado)
        print("Cubo:", self.cubo)


numero = float(input("Ingrese un numero: "))

obj = NumeroOperaciones(numero)
obj.calcular_cuadrado()
obj.calcular_cubo()
obj.mostrar_resultados()