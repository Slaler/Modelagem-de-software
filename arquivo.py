import SGBD as sgbd
bd = sgbd.SGBD()

def insere():
    print(bd.filme)
    bd.insertNew_comida("Pipoca","  R$15.00   ","30uni")
    bd.insertNew_comida("Chocolate","   R$9.50  ","45uni")
    bd.insertNew_bebida("Pepsi","   R$6.5  ","100uni")
    bd.insertNew_bebida("Coca-Cola","   R$6.5   ","200uni")
 
    bd.insertNew_filme("Avatar", "150min")
    bd.insertNew_filme("Sonic", "120min")

    bd.insertNew_sala(1)
    bd.insertNew_sala(2)
    bd.insertNew_sala(3)
    bd.insertNew_sala(4)
    print("Inseri todos os dados!")
    
def getFilme(i):
    return bd.get_filme(i)
def getTamF():
    return bd.get_tamF()
def get_sala(i):
    return bd.get_sala(i)
def get_tamB():
    return bd.get_tamB()
def get_tamC():
    return bd.get_tamC()
def get_comida(i):
    return bd.get_comida(i)
def get_bebida(i):
    return bd.get_bebida(i)

def set_filme(nome, tempo, indice):
    if indice == -1:
        bd.insertNew_filme(nome, tempo)
    else:
        bd.set_filme(indice, nome)
        bd.set_filme(indice+1, tempo)
        print(f"Modifiquei filme para {nome} e {tempo} no indicie {indice-1}")
        
def set_comida(nome, preco, qnt, indice, tipo):
    if indice == -1:
        print("Inseri comida")
        if tipo == "comida":
            bd.insertNew_comida(nome, preco, qnt)
            print("Comida ja inserida")
        elif tipo == "bebida":
            bd.insertNew_bebida(nome, preco, qnt)
    else:
        if tipo == "comida":
            bd.set_comida(indice, nome)
            bd.set_comida(indice+1, preco)
            bd.set_comida(indice+2, qnt)
        elif tipo == "bebida":
            bd.set_bebida(indice, nome)
            bd.set_bebida(indice+1, preco)
            bd.set_bebida(indice+2, qnt)