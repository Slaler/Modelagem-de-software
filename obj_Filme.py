import SGBD as sgbd
import arquivo as arq
bd = sgbd.SGBD()

def getTamF():
    tamF = arq.getTamF()
    print(tamF)
    return tamF

def set_film(nome, tempo, a):  
    print("Solicitei a mudança no filme")
    arq.set_filme(nome, tempo, a)

def lista_filmes(i):
    return(f'Nome: {arq.getFilme(i)} | Duração:{arq.getFilme(i+1)}\n')
def lista_filmes_only(i):
    return arq.getFilme(i)
    
class Sala:

    #atributos
    def __init__(self,limite) :
        self.limite   = int(limite)
        self.filme
        self.horario
        self.cadeiras = []
        
    
    
    def Prencher_Salas(self):
       for i in range(4): 
           self.cadeiras.append([i] * int(self.limite))
       posição = 1   
       for i in range(4):
           for j in range(self.limite):
             self.cadeiras[i][j] = posição
             posição += 1
           posição = 1  
           
    def mostrar_lugares(self):     
        print(self.cadeiras)
         
    def insirir_filme(self,filme,horarios):
        self.filmes.append(filme)
        self.horarios.append(horarios)
        print("Filme Insirido no Sistema!!")
        

    
    def remover_filme(self,nome,horario):
        cont = 0
        res = 0
        for filme in self.filmes:
            for hrs in self.horarios:
                 if filme.nome ==  nome and hrs == horario:  
                    res = cont
                    print(cont)
                    del self.filmes[res]
                    del self.horarios[res]
                    del self.cadeiras[res]
                 cont += 1   
                   
            
    
    def editar(self,nome,horarioant,horarionew):
        cont = 0
        
        for filme in self.filmes:
            for hrs in self.horarios:
                 if filme.nome ==  nome and hrs == horarioant:  
                    self.horarios[cont] = horarionew
                    return
                    
            cont += 1    
        print("Filme não encontrado ou horario não encontrado")     
        
            
    def comprar_Acentos(self,lugar,nome,horario):
        cont = 0
        res = -1
        for filme in self.filmes:
            for hrs in self.horarios:
                 if filme.nome ==  nome and hrs == horario:  
                    res = cont
                    
            cont += 1
        
        if res == -1:
            print("\nSeção mão encontrada\n!!")
            return
        
        if self.cadeiras[res][lugar-1] == -1 :
            print("Não é possivel vender !! Ja esta Comprado")     
            return  
        
        print("Acento Comprado com sucesso!!")
        
        self.cadeiras[res][lugar-1] = -1    
            
         
           
class Filme:
    iniciado = False
    def __init__(self,nome,tempo) :
        self.nome  = nome
        self.tempo = tempo
    
        
       
    
    def Iniciar_Filme(self):
        if self.iniciado == True:
            print("\n Filmes Já esta em andamento!!\n")
        else:
            print(f'\n Iniciado o Filme:{self.nome}')
            self.iniciado = True
    
    def Encerrar_Filme(self):
        if self.iniciado == True:
            print("\n Filmes Terminado!!\n")
            self.iniciado = False
        else:
            print(f'\n Filme ainda não foi exibido:{self.nome}')  
    
        

                
        