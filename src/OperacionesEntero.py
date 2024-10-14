class OperacionesEnteros:
    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1

    def MCM(self, numero1, numero2):
        return abs(numero1 * numero2) // self.MCD(numero1, numero2)

    def MCM_de_tres(self, numero1, numero2, numero3):
        return self.MCM(self.MCM(numero1, numero2), numero3)
    def MCM_de_cuatro(self, numero1, numero2, numero3, numero4):
        return self.MCM(self.MCM_de_tres(numero1, numero2, numero3), numero4)