import arquivo as arq
import SGBD as sgbd
bd = sgbd.SGBD()

def get_tamB():
    print(arq.get_tamB())
    return arq.get_tamB()
def get_tamC():
    print(arq.get_tamC())
    return arq.get_tamC()

def lista_estoqueC(i):
    print(arq.get_comida(i))
    return arq.get_comida(i)
    
def lista_estoqueB(j):
    print(arq.get_bebida(j))
    return arq.get_bebida(j)

def set_comida(nome, preco, qnt, p, string):
    print("Socilitei mudanca na comida")
    arq.set_comida(nome, preco, qnt, p, string)

class bebidas:
    def __init__(self):
          self.nome = None
          self.preço = None
          self.qnt = None
    
    def Insirir_consumivel(nome,tipo,qnt):
             for i in bd.get_tamB():
                 if bd.get_bebida(i) == nome:
                     bd.set_bebida(i, qnt)
                     return
             preco = input("Preco: ")
             bd.insertNew_bebida(nome, preco, qnt)
        
class comida:
    def __init__(self):
        self.nome = None
        self.preço = None
        self.qnt = None
          
    def Insirir_consumivel(nome,tipo,qnt):
            for i in bd.get_tamC():
                if bd.get_comida(i) == nome:
                    bd.set_comida(i, qnt)
                    return
            preco = input("Preco: ")
            bd.insertNew_comida(nome, preco, qnt)
               

def venda_estoque(tipo,nome,qnt):
        if tipo == "comida":
            for i in bd.comida:
                if bd.comida[i] == nome and bd.comida[i+2] >= qnt:
                    print('Compra finalizada\n')
                    bd.comida[i+2] -= qnt
                    return
            print("Não tem estoque")
        elif tipo == "bebida":
            for i in bd.bebida:
                if bd.bebida[i] == nome and bd.bebida[i+2] >= qnt:
                    print('Compra Finalizada')
                    bd.bebida[i+2] -= qnt
                    return
            print("Não tem mais estoque")  
        else:
            print("Não foi possivels fazer a venda")             