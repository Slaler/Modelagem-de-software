import tkinter as tk
import arquivo as arq
import obj_Alimentos as a
import obj_Filme as film

import obj_Funcionario as fun


nome_filme = ""
comida = ""
qnt = 0

obj_comida = a.comida()
obj_bebida = a.bebidas()

janela = tk.Tk() 



def limpar():
    for destroy in janela.winfo_children():
        destroy.destroy()
        
def fim_ingresso(v):
    limpar()
    global nome_filme
    _ingresso = (f"Nome do filme: {nome_filme}\nCadeira: {v}")
    rotulo = tk.Label(janela, text=_ingresso)
    rotulo.pack()
    botao_fim = tk.Button(janela, text="Finalizar", command=tela_funcionario_vendas)
    botao_fim.pack()
        
def escolhe_cadeiras(nome):
    nomeFilme = nome.get()
    global nome_filme
    nome_filme = nomeFilme
    limpar()
    rotulo = tk.Label(janela, text="Venda de ingressos\n")
    rotulo.grid(row=0, column=0)
    rotulo1 = tk.Label(janela, text="Escolha sua cadeira:\n")
    rotulo1.grid(row=5, column=0)
    i = 0
    j = 0
    while i < 41:
        botao_cadeira = tk.Button(janela, text=str(i), command=lambda v=i: fim_ingresso(v))
        botao_cadeira.grid(row = j+10, column = i-(j*8))
        if(i == 8 or i== 16 or i == 24 or i == 32):
            j += 1
        i += 1
    botao_voltar = tk.Button(janela, text="voltar", command=venda_ingresso)
    botao_voltar.grid(row=10, column= 0)

def venda_ingresso():
    limpar()
    rotulo = tk.Label(janela, text="Venda de ingressos\n")
    rotulo.pack()
    p = 0
    while p < (film.getTamF() * 2):
        listaDeFilmes = tk.Label(janela, text= film.lista_filmes(p))
        listaDeFilmes.pack()
        p += 2

    rotulo1 = tk.Label(janela, text="Insira o nome do filme: ")
    rotulo1.pack()
    filme_entrada = tk.Entry(janela)
    filme_entrada.pack()
    botao_confirma = tk.Button(janela, text="confirmar", command=lambda: escolhe_cadeiras(filme_entrada))
    botao_confirma.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_funcionario_vendas)
    botao_voltar.pack()
    
def finaliza_compra_comida():
    limpar()
    global comida
    global qnt
    comida = tk.Label(janela, text=comida)
    comida.pack()
    qnt = tk.Label(janela, text=qnt)
    qnt.pack()
    botao_fim = tk.Button(janela, text="Finalizar", command=tela_funcionario_vendas)
    botao_fim.pack()
    
def get_comida(a):
    global comida
    comida = a.get()
def get_qnt(a, b):
    get_comida(a)
    global qnt
    qnt = int(b.get())
    finaliza_compra_comida()
    
def venda_comida():
    limpar()
    i = 0
    j = 0
    while i < a.get_tamB():
        menuB = tk.Label(janela, text=f"{a.lista_estoqueB(i)}")
        menuB.pack()
        i += 1
    while j < a.get_tamC():
        menuC = tk.Label(janela, text=f"{a.lista_estoqueC(j)}")
        menuC.pack()
        j += 1
    comida = tk.Label(janela, text="comida:")
    comida.pack()
    compra_comida = tk.Entry(janela)
    compra_comida.pack()
    qnt = tk.Label(janela, text="qnt:")
    qnt.pack()
    compra_qnt = tk.Entry(janela)
    compra_qnt.pack()
    botao_qnt = tk.Button(janela, text="confirmar", command= lambda: get_qnt(compra_comida, compra_qnt))
    botao_qnt.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_funcionario_vendas)
    botao_voltar.pack()
    

def tela_funcionario_vendas():
    limpar()
    rotulo = tk.Label(janela, text="TELA DE USUARIO")
    rotulo.pack()
    botao_venderIngresso = tk.Button(janela, text="Vender Ingresso", command=venda_ingresso)
    botao_venderIngresso.pack()
    botao_venderComida = tk.Button(janela, text="Vender Comida", command=venda_comida)
    botao_venderComida.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_login)
    botao_voltar.pack()
    
def tela_funcionario_filme():
    limpar()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_login)
    botao_voltar.pack()
    
def recebe_filme(nome, tempo, p):
    _nome = nome.get()
    _tempo = tempo.get()
    print("Recebi o filme")
    film.set_film(_nome, _tempo, p)
    print("Filme modificado!")
    rotulo = tk.Label(janela, text="Filme modificado!")
    rotulo.pack()
    botao = tk.Button(janela, text="OK", command=tela_adm)
    botao.pack()
    
def edita_filme_fim(a, p):
    limpar()
    rotulo = tk.Label(janela, text="Digite os parametros novos do filme")
    rotulo.pack()
    nome = tk.Entry(janela)
    nome.pack()
    tempo = tk.Entry(janela)
    tempo.pack()
    botao_confirma = tk.Button(janela, text="confirmar", command=lambda: recebe_filme(nome, tempo, p))
    botao_confirma.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=editar_ingresso_busca)
    botao_voltar.pack()
    
def editar_ingresso_busca(a):
    filme = a.get()
    limpar()
    p = 0
    listaDeFilmes = ["debug"]
    while p < (film.getTamF() * 2):
        listaDeFilmes.append(film.lista_filmes_only(p))
        p += 2
    p = 0
    for i in listaDeFilmes:
        print(f"verificando se {listaDeFilmes[p]} == {filme}")
        if listaDeFilmes[p] == filme:
            #filme4 encontrado
            edita_filme_fim(filme, p-1)
            return
        p += 1
    rotulo = tk.Label(janela, text="Filme nao encontrado")
    rotulo.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=editar_ingresso)
    botao_voltar.pack()
    
def editar_ingresso():
    limpar()
    rotulo = tk.Label(janela, text="Qual filme deseja editar?")
    rotulo.pack()
    entrada = tk.Entry(janela)
    entrada.pack()
    botao_confirma = tk.Button(janela, text="Confirmar", command=lambda:editar_ingresso_busca(entrada))
    botao_confirma.pack()
    
def insere_filme():
    limpar()
    rotulo = tk.Label(janela, text="Digite os parametros do novo filme")
    rotulo.pack()
    nome = tk.Entry(janela)
    nome.pack()
    tempo = tk.Entry(janela)
    tempo.pack()
    botao_confirma = tk.Button(janela, text="confirmar", command=lambda: recebe_filme(nome, tempo, -1))
    botao_confirma.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_adm)
    botao_voltar.pack()
    
def edita_ingresso():
    limpar()
    rotulo = tk.Label(janela, text="O que deseja fazer?")
    rotulo.pack()
    botao_editar = tk.Button(janela, text="editar", command=editar_ingresso)
    botao_editar.pack()
    botao_criar = tk.Button(janela, text="Inserir Filme", command=insere_filme)
    botao_criar.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_adm)
    botao_voltar.pack()
    
def recebe_comida(nome, preco, qnt, p, string):
    _nome = nome.get()
    _preco = preco.get()
    _qnt = qnt.get()
    if p == -1:
        tipo = string.get()
    else:
        tipo = string
    print("Recebi a comida")
    a.set_comida(_nome, _preco, _qnt, p, tipo)
    print("Comida modificada!")
    rotulo = tk.Label(janela, text="Comida modificada!")
    rotulo.pack()
    botao = tk.Button(janela, text="OK", command=tela_adm)
    botao.pack()
    
def edita_comida_fim(comida, p, string):
    limpar()
    rotulo = tk.Label(janela, text="Digite os parametros novos da comida")
    rotulo.pack()
    nome = tk.Entry(janela)
    nome.pack()
    preco = tk.Entry(janela)
    preco.pack()
    qnt = tk.Entry(janela)
    qnt.pack()
    botao_confirma = tk.Button(janela, text="confirmar", command=lambda: recebe_comida(nome, preco, qnt, p, string))
    botao_confirma.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=editar_comida_busca)
    botao_voltar.pack()
    
def editar_comida_busca(entrada):
    comida = entrada.get()
    limpar()
    p = 0
    listaDeComidas = ["debug"]
    listaDeBebidas = ["debug"]
    while p < (a.get_tamB() * 3):
        listaDeBebidas.append(a.lista_estoqueB(p))
        p += 3
    p = 0
    while p < (a.get_tamC() * 3):
        listaDeComidas.append(a.lista_estoqueC(p))
        p += 3
    p = 0
    for i in listaDeComidas:
        print(f"verificando se {listaDeComidas[p]} == {comida}")
        if listaDeComidas[p] == comida:
            #comida encontrada
            edita_comida_fim(comida, p-1, "comida")
            return
        p += 1
    p = 0
    for i in listaDeBebidas:
        print(f"verificando se {listaDeBebidas[p]} == {comida}")
        if listaDeBebidas[p] == comida:
            #comida encontrada
            edita_comida_fim(comida, p-1, "bebida")
            return
        p += 1
    rotulo = tk.Label(janela, text="comida nao encontrada")
    rotulo.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_adm)
    botao_voltar.pack()
    
def editar_comida():
    limpar()
    rotulo = tk.Label(janela, text="Qual comida deseja editar?")
    rotulo.pack()
    entrada = tk.Entry(janela)
    entrada.pack()
    botao_confirma = tk.Button(janela, text="Confirmar", command=lambda:editar_comida_busca(entrada))
    botao_confirma.pack()
    
def insere_comida():
    limpar()
    rotulo = tk.Label(janela, text="Digite os parametros da nova comida")
    rotulo.pack()
    nome = tk.Entry(janela)
    nome.pack()
    preco = tk.Entry(janela)
    preco.pack()
    qnt = tk.Entry(janela)
    qnt.pack()
    tipo = tk.Entry(janela)
    tipo.pack()
    botao_confirma = tk.Button(janela, text="confirmar", command=lambda: recebe_comida(nome, preco, qnt, -1, tipo))
    botao_confirma.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_adm)
    botao_voltar.pack()
    
def edita_comida():
    limpar()
    rotulo = tk.Label(janela, text="O que deseja fazer?")
    rotulo.pack()
    botao_editar = tk.Button(janela, text="editar", command=editar_comida)
    botao_editar.pack()
    botao_criar = tk.Button(janela, text="Inserir", command=insere_comida)
    botao_criar.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_adm)
    botao_voltar.pack()
    
def tela_adm():
    limpar()
    rotulo = tk.Label(janela, text="TELA ADM")
    rotulo.pack()
    botao_editarIngresso = tk.Button(janela, text="Editar Ingresso", command=edita_ingresso)
    botao_editarIngresso.pack()
    botao_editarComida = tk.Button(janela, text="Editar Comida", command=edita_comida)
    botao_editarComida.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_login)
    botao_voltar.pack()

def entrada_login(senha):
    entrada = senha.get()
    if entrada == "user123":
        tela_funcionario_vendas()
    elif entrada == "film123":
        tela_funcionario_filme()
    elif entrada == "ADM123":
        tela_adm()

def tela_login():
    limpar()
    rotulo = tk.Label(janela, text="Login")
    rotulo.pack()
    botao_senha = tk.Entry(janela)
    botao_senha.pack()
    botao_login = tk.Button(janela, text="login", command=lambda: entrada_login(botao_senha))
    botao_login.pack()
    botao_voltar = tk.Button(janela, text="voltar", command=tela_inicial)
    botao_voltar.pack()

def tela_inicial():
    limpar()
    rotulo = tk.Label(janela, text = "SISTEMA GERAL DO CINEMA")
    rotulo.pack()

    botao_login = tk.Button(janela, text = "login", command=tela_login)
    botao_login.pack()

    janela.mainloop()
    
arq.insere()

tela_inicial()

