class Empleado:

    def __init__(self, horas, valor_hora, porcentaje_retencion):
        self.horas = horas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion
        self.salario_bruto = 0
        self.retencion_fuente = 0
        self.salario_neto = 0

    def calcular_salario_bruto(self):
        self.salario_bruto = self.horas * self.valor_hora
        return self.salario_bruto

    def calcular_retencion_fuente(self):
        self.retencion_fuente = self.salario_bruto * (self.porcentaje_retencion / 100)
        return self.retencion_fuente

    def calcular_salario_neto(self):
        self.salario_neto = self.salario_bruto - self.retencion_fuente
        return self.salario_neto

    def mostrar_resultados(self):
        print("Salario bruto:", self.salario_bruto)
        print("Retencion en la fuente:", self.retencion_fuente)
        print("Salario neto:", self.salario_neto)


horas = 48
valor_hora = 5000
porcentaje_retencion = 12.5

empleado = Empleado(horas, valor_hora, porcentaje_retencion)
empleado.calcular_salario_bruto()
empleado.calcular_retencion_fuente()
empleado.calcular_salario_neto()
empleado.mostrar_resultados()