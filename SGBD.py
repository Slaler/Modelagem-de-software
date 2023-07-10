class SGBD:
    def __init__(self):
        self.bebida = []
        self.comida = []
        self.filme = []
        self.sala = []
        
        self.tamB = len(self.bebida)
        self.tamC = len(self.comida)
        self.tamF = len(self.filme)
        self.tamS = len(self.sala)
        
    def get_bebida(self, i):
        return self.bebida[i]
    def get_comida(self, i):
        return self.comida[i]
    def get_filme(self, i):
        return self.filme[i]
    def get_sala(self, i):
        print(f"recebi: {i}")
        return self.sala[i]
    
    def get_tamB(self):
        return self.tamB
    def get_tamC(self):
        return self.tamC
    def get_tamF(self):
        return self.tamF
    def get_tamS(self):
        return self.tamS
    
    
    def set_bebida(self, i, p):
        self.bebida[i] = p
    def set_comida(self, i, p):
        self.comida[i] = p
    def set_filme(self, i, p):
        self.filme[i] = p
    def set_sala(self, i, p):
        self.sala[i] = p
        
    def insertNew_bebida(self, nome, valor, qnt):
        self.tamB += 3
        self.bebida.append(nome)
        self.bebida.append(valor)
        self.bebida.append(qnt)
        print("Criei e incrementei bebida")
    def insertNew_comida(self, nome, valor, qnt):
        self.comida.append(nome)
        self.comida.append(valor)
        self.comida.append(qnt)
        self.tamC += 3
        print("Criei e incrementei comida")
    def insertNew_filme(self, nome, tempo):
        self.tamF += 1
        self.filme.append(nome)
        self.filme.append(tempo)
        print("Criei e incrementei filme")
    def insertNew_sala(self, n):
        self.sala.append(n)
        self.tamS += 1
        print("Criei e incrementei sala")
 