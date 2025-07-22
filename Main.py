class object(self, tipo, vida, daño):
    def __init__: 
        self.tipo = tipo
        if self.tipo == "jugador":
            self.vida = int(vida)
            self.daño = int(daño)
        elif self.tipo == "bot":
            self.vida = int(vida)
            self.daño = int(personaje.daño / 2)
        elif self.tipo == "pared":
            self.vida == int(int(vida) + int(daño))
            self.daño == 0
        else:
            self.vida = int(vida)
            self.daño = int(daño)

comando = str(input("cmd python:/main.py: ")

if comando = "new.object": 
    
