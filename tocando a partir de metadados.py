#importando biblioteca de tempo e de tkinker
from datetime import datetime, timedelta
import time
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import threading
import pygame 
from mutagen.mp3 import MP3


#Iniciar player de música:
pygame.mixer.init()

#Atributos da música e arquivo de audio - 3 opções:

#1-Opção mais simples por código
'''
pygame.mixer.music.load("C:/Users/Lívia/Desktop/Projeto jogo/musicas/Ditado 1.mp3")
nome_musica = 'Música teste (C)'
tamanho_musica = timedelta(minutes=0, seconds=30, microseconds=0)
acorde1 = [1,0,10,0]
acorde2 = [2,0,15,0]
acorde3 = [5,0,20,0]
acorde4 = [1,0,25,0]
acordes = [acordeinicial, acorde2, acorde3, acorde4] 
acorde_inicial = acorde1[0]
'''

#2-atributos da música e arquivo de audio a partir do caminho do áudio
'''
caminho_arquivo_mp3 = 'musicas/Ditado 1.mp3'
pygame.mixer.music.load(caminho_arquivo_mp3)
#Carregar metadados da música
caminho_meta = caminho_arquivo_mp3[:-3] + 'txt'
arquivo_meta = open(caminho_meta)
#Guardando metadados em uma lista
lista_meta = list()
for linha in arquivo_meta:
    lista_meta.append(linha)    
#Extraindo nome e tonalidade
nome_musica = (lista_meta[0])[:-1]
tonalidade = (lista_meta[1])[:-1]
#Extraindo tamanho da música
tamanho_musica = lista_meta[2].replace('.',':')[:-1]
lista_tamanho_musica = tamanho_musica.split(':')
tamanho_musica = timedelta(hours=int(lista_tamanho_musica[0]),minutes=int(lista_tamanho_musica[1]),seconds=int(lista_tamanho_musica[2]),microseconds=int(lista_tamanho_musica[3]))
#Extraindo acordes
lista_acordes = list()
for acorde in lista_meta[3:]:
    acorde = acorde.rstrip()
    acorde = acorde.split()
    acorde[0] = int(acorde[0])
    acorde[1] = int(acorde[1])
    acorde[2] = int(acorde[2])
    acorde[3] = int(acorde[3])
    lista_acordes.append(acorde)
acorde1 = lista_acordes[0]
acorde_inicial = acorde1[0]'''


#3-pedindo para usuario abrir o arquivo
def abrir_arquivo():
    global tamanho_musica
    global nome_musica
    global tonalidade
    global lista_acordes
    global acorde_inicial
    caminho_arquivo_mp3 = tkinter.filedialog.askopenfilename(filetypes=[('Arquivos MP3', '*.mp3')], title = "Escolha um arquivo mp3") 
    try:
        pygame.mixer.music.load(caminho_arquivo_mp3)
        #Carregar metadados da música
        audiomp3 = MP3(caminho_arquivo_mp3)
        arquivo_meta=audiomp3.tags['COMM::XXX'].text[0]
        #Guardando metadados em uma lista
        lista_meta = arquivo_meta.split('\n')
        nome_musica = lista_meta[0]
        tonalidade = lista_meta[1]
        #Extraindo tamanho da música
        tamanho_musica = lista_meta[2].replace('.',':')
        lista_tamanho_musica = tamanho_musica.split(':')
        try:
            tamanho_musica = timedelta(hours=int(lista_tamanho_musica[0]),minutes=int(lista_tamanho_musica[1]),seconds=int(lista_tamanho_musica[2]),microseconds=int(lista_tamanho_musica[3]))
        except:
            tamanho_musica = timedelta(hours=int(lista_tamanho_musica[0]),minutes=int(lista_tamanho_musica[1]),seconds=int(lista_tamanho_musica[2]))
        
        #Extraindo acordes
        lista_acordes = list()
        for acorde in lista_meta[3:]:
            acorde = acorde.rstrip()
            acorde = acorde.split()
            acorde[0] = int(acorde[0])
            acorde[1] = int(acorde[1])
            acorde[2] = int(acorde[2])
            acorde[3] = int(acorde[3])
            acorde[4] = int(acorde[4])
            lista_acordes.append(acorde)
        acorde1 = lista_acordes[0]
        acorde_inicial = acorde1[0]
        botao_iniciar.config(state='normal')
        botao_gabarito.config(state='normal')
        botao_parar.config(state='normal')
        botao_ver_acordes.config(state='normal')
        botao_apenas_acordes_da_musica.config(state='normal')
        titulo_musica.config(text=nome_musica+'\nTom:'+tonalidade)
    except:
        titulo_musica.config(text='Erro ao abrir. \nTente com um arquivo válido')


#tonalidades
tom_C = {1:'C', 2:'Dm', 3:'Em',4:'F',5:'G',6:'Am',7:'Bm7(b5)',51:'G7',52:'A7',53:'B7', 54:'C7', 55:'D7',56:'E7',  48:'Fm',49:'F#dim'}
tom_G = {1:'G', 2:'Am', 3:'Bm',4:'C',5:'D',6:'Em',7:'F#m7(b5)',51:'D7',52:'E7',53:'F#7', 54:'G7', 55:'A7',56:'B7',   48:'Cm',49:'C#dim'}
tom_D = {1:'D', 2:'Em', 3:'F#m',4:'G',5:'A',6:'Bm',7:'C#m7(b5)',51:'A7',52:'B7',53:'C#7', 54:'D7', 55:'E7',56:'F#7',  48:'Gm',49:'G#dim'}
tom_A = {1:'A', 2:'Bm', 3:'C#m',4:'D',5:'E',6:'F#m',7:'G#m7(b5)',51:'E7',52:'F#7',53:'G#7', 54:'A7', 55:'B7',56:'C#7', 48:'Dm',49:'D#dim'}

ver_acordes_ativado = False
def ver_acordes():
    global ver_acordes_ativado
    if ver_acordes_ativado == True:
        botao_acordeI.config(text='I')
        botao_acordeII.config(text='IIm')
        botao_acordeIII.config(text='IIIm')
        botao_acordeIV.config(text='IV')
        botao_acordeVI.config(text='VIm')
        botao_acordeVII.config(text='VIIm7(b5)')
        botao_acordeV1.config(text='V7')
        botao_acordeV2.config(text='V7/IIm')
        botao_acordeV3.config(text='V7/IIIm')
        botao_acordeV4.config(text='V7/IV')
        botao_acordeV5.config(text='V7/V')
        botao_acordeV6.config(text='V7/VIm')
        botao_acordeIVm.config(text='IVm')
        botao_acordesustIVdim.config(text='#IVdim')
        ver_acordes_ativado = False
    elif ver_acordes_ativado == False:
        if tonalidade == 'C' or tonalidade =='Am':
            tom=tom_C
        elif tonalidade == 'G' or tonalidade == 'Em':
            tom=tom_G
        elif tonalidade == 'D' or tonalidade == 'Bm':
            tom=tom_D
        elif tonalidade == 'A' or tonalidade == 'F#m':
            tom=tom_A
        botao_acordeI.config(text=tom[1])
        botao_acordeII.config(text=tom[2])
        botao_acordeIII.config(text=tom[3])
        botao_acordeIV.config(text=tom[4])
        botao_acordeVI.config(text=tom[6])
        botao_acordeVII.config(text=tom[7])
        botao_acordeV1.config(text=tom[51])
        botao_acordeV2.config(text=tom[52])
        botao_acordeV3.config(text=tom[53])
        botao_acordeV4.config(text=tom[54])
        botao_acordeV5.config(text=tom[55])
        botao_acordeV6.config(text=tom[56])
        botao_acordeIVm.config(text=tom[48])
        botao_acordesustIVdim.config(text=tom[49])
        ver_acordes_ativado = True

apenas_acordes_da_musica_ativo = False
def apenas_acordes_da_musica():
    global apenas_acordes_da_musica_ativo
    if apenas_acordes_da_musica_ativo == True:
        habilitar_botoes_acorde()
        apenas_acordes_da_musica_ativo = False
    elif apenas_acordes_da_musica_ativo == False:
        desabilitar_botoes_acorde()
        for acorde in lista_acordes:
            if acorde[0] == 1:
                botao_acordeI.config(state='normal')
            elif acorde[0] == 2:
                botao_acordeII.config(state='normal')
            elif acorde[0] == 3:
                botao_acordeIII.config(state='normal')
            elif acorde[0] == 4:
                botao_acordeIV.config(state='normal')
            elif acorde[0] == 6:
                botao_acordeVI.config(state='normal')
            elif acorde[0] == 7:
                botao_acordeVII.config(state='normal')
            elif acorde[0] == 51:
                botao_acordeV1.config(state='normal')
            elif acorde[0] == 52:
                botao_acordeV2.config(state='normal')
            elif acorde[0] == 53:
                botao_acordeV3.config(state='normal')   
            elif acorde[0] == 54:
                botao_acordeV4.config(state='normal') 
            elif acorde[0] == 55:
                botao_acordeV5.config(state='normal')
            elif acorde[0] == 56:
                botao_acordeV6.config(state='normal')
            elif acorde[0] == 48:
                botao_acordeIVm.config(state='normal')
            elif acorde[0] == 49:
                botao_acordesustIVdim.config(state='normal')
        apenas_acordes_da_musica_ativo = True
    

#criando funções dos botões e definindo variáveis iniciais
acorde_palpite = 0
ativar_inicio = False
ver_gabarito = False

#botão com função de play musica e programa em funcionamento com musica
def comando_botao_start():
    global ativar_inicio
    global start_musica
    global tamanho_musica
    global end_musica
    global tempo_de_erro
    global tempo_de_acerto
    global tempo_de_acerto_start
    global tempo_de_erro_start
    global variavel_acerto
    pygame.mixer.music.play()
    print('start')
    start_musica = datetime.now()
    end_musica = start_musica + tamanho_musica
    tempo_de_erro = timedelta()
    tempo_de_acerto = timedelta()
    if acorde_inicial == acorde_palpite:
        tempo_de_acerto_start = datetime.now()
        variavel_acerto = 1    
    else:
        tempo_de_erro_start = datetime.now()
        variavel_acerto = 0
    ativar_inicio = True
    botao_iniciar.config(state='disabled')
    botao_gabarito.config(state='disabled')
    botao_abrir_arquivo.config(state='disabled')

#botão stop
def comando_botao_stop():
    global ativar_inicio
    global ver_gabarito
    global acorde_palpite
    pygame.mixer.music.stop()
    ativar_inicio = False
    ver_gabarito = False
    barra_de_progresso.config(value=0)
    botao_iniciar.config(state='normal')
    botao_gabarito.config(state='normal')
    botao_abrir_arquivo.config(state='normal')
    botao_apenas_acordes_da_musica.config(state='normal')
    botao_ver_acordes.config(state='normal')
    habilitar_botoes_acorde()
    desmarcar_botoes()
    acorde_palpite = 0

#checagem de acordes e acerto/erro
def checagem():
    global acorde_correto
    global tempo_de_erro_start
    global tempo_de_erro_fim
    global tempo_de_acerto_start
    global tempo_de_acerto_fim
    global tempo_de_erro
    global tempo_de_acerto
    global variavel_acerto
    for acorde in lista_acordes:
        if datetime.now() - start_musica <= timedelta(hours=acorde[1],minutes=acorde[2], seconds=acorde[3], microseconds=acorde[4]):
            acorde_correto = acorde[0]
            break
    if acorde_palpite == acorde_correto:
        print('correto')
        if variavel_acerto == 0:
            tempo_de_erro_fim = datetime.now()
            tempo_de_acerto_start = datetime.now()
            tempo_de_erro = tempo_de_erro + tempo_de_erro_fim - tempo_de_erro_start
            variavel_acerto = 1
    else:
        print('errado')
        if variavel_acerto == 1:
            tempo_de_acerto_fim = datetime.now()
            tempo_de_erro_start = datetime.now()
            tempo_de_acerto = tempo_de_acerto + tempo_de_acerto_fim - tempo_de_acerto_start
            variavel_acerto = 0

#botões de acorde
def habilitar_botoes_acorde():
    botao_acordeI.config(state='normal')
    botao_acordeII.config(state='normal')
    botao_acordeIII.config(state='normal')
    botao_acordeIV.config(state='normal')
    botao_acordeVI.config(state='normal')
    botao_acordeVII.config(state='normal')
    botao_acordeV1.config(state='normal')
    botao_acordeV2.config(state='normal')
    botao_acordeV3.config(state='normal')
    botao_acordeV4.config(state='normal')
    botao_acordeV5.config(state='normal')
    botao_acordeV6.config(state='normal')
    botao_acordeIVm.config(state='normal')
    botao_acordesustIVdim.config(state='normal')

def desabilitar_botoes_acorde():
    botao_acordeI.config(state='disabled')
    botao_acordeII.config(state='disabled')
    botao_acordeIII.config(state='disabled')
    botao_acordeIV.config(state='disabled')
    botao_acordeVI.config(state='disabled')
    botao_acordeVII.config(state='disabled')
    botao_acordeV1.config(state='disabled')
    botao_acordeV2.config(state='disabled')
    botao_acordeV3.config(state='disabled')
    botao_acordeV4.config(state='disabled')
    botao_acordeV5.config(state='disabled')
    botao_acordeV6.config(state='disabled')
    botao_acordeIVm.config(state='disabled')
    botao_acordesustIVdim.config(state='disabled')

def desmarcar_botoes():
    botao_acordeI.config(bg='white')
    botao_acordeII.config(bg='white')
    botao_acordeIII.config(bg='white')
    botao_acordeIV.config(bg='white')
    botao_acordeVI.config(bg='white')
    botao_acordeVII.config(bg='white')
    botao_acordeV1.config(bg='white')
    botao_acordeV2.config(bg='white')    
    botao_acordeV3.config(bg='white')
    botao_acordeV4.config(bg='white')
    botao_acordeV5.config(bg='white')
    botao_acordeV6.config(bg='white')
    botao_acordeIVm.config(bg='white')
    botao_acordesustIVdim.config(bg='white')

def botaoacorde1():
    global acorde_palpite
    acorde_palpite = 1
    desmarcar_botoes()
    botao_acordeI.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde2():
    global acorde_palpite
    acorde_palpite = 2
    desmarcar_botoes()
    botao_acordeII.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde3():
    global acorde_palpite
    acorde_palpite = 3
    desmarcar_botoes()
    botao_acordeIII.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde4():
    global acorde_palpite
    acorde_palpite = 4
    desmarcar_botoes()
    botao_acordeIV.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde6():
    global acorde_palpite
    acorde_palpite = 6
    desmarcar_botoes()
    botao_acordeVI.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde7():
    global acorde_palpite
    acorde_palpite = 7
    desmarcar_botoes()
    botao_acordeVII.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()


def botaoacorde51():
    global acorde_palpite
    acorde_palpite = 51
    desmarcar_botoes()
    botao_acordeV1.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde52():
    global acorde_palpite
    acorde_palpite = 52
    desmarcar_botoes()
    botao_acordeV2.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde53():
    global acorde_palpite
    acorde_palpite = 53
    desmarcar_botoes()
    botao_acordeV3.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde54():
    global acorde_palpite
    acorde_palpite = 54
    desmarcar_botoes()
    botao_acordeV4.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()

def botaoacorde55():
    global acorde_palpite
    acorde_palpite = 55
    desmarcar_botoes()
    botao_acordeV5.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()  

def botaoacorde56():
    global acorde_palpite
    acorde_palpite = 56
    desmarcar_botoes()
    botao_acordeV6.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem() 

def botaoacorde48():
    global acorde_palpite
    acorde_palpite = 48
    desmarcar_botoes()
    botao_acordeIVm.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem() 

def botaoacorde49():
    global acorde_palpite
    acorde_palpite = 49
    desmarcar_botoes()
    botao_acordesustIVdim.config(bg='blue')
    print(acorde_palpite)
    if ativar_inicio == True:
        checagem()            

def comando_botao_gabarito():
    global ver_gabarito
    ver_gabarito = True
    desabilitar_botoes_acorde()
    botao_abrir_arquivo.config(state='disabled')
    botao_apenas_acordes_da_musica.config(state='disabled')
    botao_ver_acordes.config(state='disabled')
    comando_botao_start()
    checagem()
    cor_botoes_gabarito()
   

def finalizacao():
    global ativar_inicio
    global end_musica
    global tempo_de_erro_start
    global tempo_de_erro_fim
    global tempo_de_acerto_start
    global tempo_de_acerto_fim
    global tempo_de_erro
    global tempo_de_acerto
    global variavel_acerto
    global pontuacao
    global ver_gabarito
    if variavel_acerto == 0:
        tempo_de_erro_fim = end_musica
        tempo_de_erro = tempo_de_erro + tempo_de_erro_fim - tempo_de_erro_start
    elif variavel_acerto == 1:
        tempo_de_acerto_fim = end_musica
        tempo_de_acerto = tempo_de_acerto + tempo_de_acerto_fim - tempo_de_acerto_start        
    print('Fim da música!\nTempo de acerto:', tempo_de_acerto,'Tempo de erro:', tempo_de_erro, 'Porcentagem de acerto:', round(tempo_de_acerto/tamanho_musica*100), 'Nota:', round(tempo_de_acerto/tamanho_musica*10))   
    if ver_gabarito == False:
        pontuacao = round(tempo_de_acerto/tamanho_musica*10)
        texto_nota = 'Nota:',pontuacao
        nota.config(text=texto_nota)  
    else:
        ver_gabarito = False
    ativar_inicio = False
    botao_iniciar.config(state='normal')
    botao_gabarito.config(state='normal')
    botao_abrir_arquivo.config(state='normal')
    botao_apenas_acordes_da_musica.config(state='normal')
    botao_ver_acordes.config(state='normal')
    habilitar_botoes_acorde()

def cor_botoes_gabarito():
    if acorde_correto == 1:
        desmarcar_botoes()
        botao_acordeI.config(bg='green')
    elif acorde_correto == 2:
        desmarcar_botoes()
        botao_acordeII.config(bg='green')
    elif acorde_correto == 3:
        desmarcar_botoes()
        botao_acordeIII.config(bg='green')
    elif acorde_correto == 4:
        desmarcar_botoes()
        botao_acordeIV.config(bg='green') 
    elif acorde_correto == 6:
        desmarcar_botoes()
        botao_acordeVI.config(bg='green')   
    elif acorde_correto == 7:
        desmarcar_botoes()
        botao_acordeVII.config(bg='green')
    elif acorde_correto == 51:
        desmarcar_botoes()
        botao_acordeV1.config(bg='green')
    elif acorde_correto == 52:
        desmarcar_botoes()
        botao_acordeV2.config(bg='green')
    elif acorde_correto == 53:
        desmarcar_botoes()
        botao_acordeV3.config(bg='green')
    elif acorde_correto == 54:
        desmarcar_botoes()
        botao_acordeV4.config(bg='green')
    elif acorde_correto == 55:
        desmarcar_botoes()
        botao_acordeV5.config(bg='green')
    elif acorde_correto == 56:
        desmarcar_botoes()
        botao_acordeV6.config(bg='green')
    elif acorde_correto == 48:
        desmarcar_botoes()
        botao_acordeIVm.config(bg='green')
    elif acorde_correto == 59:
        desmarcar_botoes()
        botao_acordesustIVdim.config(bg='green')


def ciclo_checagem():
    global fim_programa
    global tempo_corrido
    fim_programa = False
    tempo_corrido = timedelta(seconds=0)
    while fim_programa ==False:
        if ativar_inicio == True:
            tempo_corrido = datetime.now()-start_musica
            barra_de_progresso.config(value=(tempo_corrido/tamanho_musica)*100)
            checagem()
            if ver_gabarito == True:
                cor_botoes_gabarito()
            if datetime.now() >= end_musica:
                finalizacao()
        time.sleep(0.05)

def ativar_threads():
    ciclo_checar = threading.Thread(target=ciclo_checagem)
    ciclo_checar.start()

#criando ambiente visual
janelao = Tk()
janelao.geometry('600x600')
janelao.title('Ouvido harmônico')
ativar_threads()
botao_abrir_arquivo = tkinter.Button(janelao, text='Abrir arquivo', command=abrir_arquivo)
botao_abrir_arquivo.grid(column=1,row=1)
botao_iniciar = tkinter.Button(janelao, text="Iniciar música", command=comando_botao_start, bg='blue',fg='white', state='disabled')
botao_iniciar.grid(column=2, row=2)
titulo_musica = ttk.Label(janelao,text='Carregue uma música')
titulo_musica.grid(column=2,row=1)
botao_gabarito = tkinter.Button(janelao, text="Ver gabarito", command=comando_botao_gabarito,bg='green',state='disabled')
botao_gabarito.grid(column=1,row=2)
botao_parar = tkinter.Button(janelao, text="Stop", command=comando_botao_stop, bg='red',fg='white',state='disabled')
botao_parar.grid(column=2, row=3) 
botao_ver_acordes = tkinter.Button(janelao, text="Ver cifras", command=ver_acordes, bg='black',fg='white',state='disabled')
botao_ver_acordes.grid(column=1, row=3) 
botao_apenas_acordes_da_musica = tkinter.Button(janelao, text="Apenas acordes\n da música", command=apenas_acordes_da_musica, bg='orange',fg='white',state='disabled')
botao_apenas_acordes_da_musica.grid(column=1, row=4) 

janela_acordes = tkinter.Frame(janelao, width=400, height=400, bg="white")
janela_acordes.grid(row=5, column=2)
botao_acordeI = tkinter.Button(janela_acordes, text="I", command=botaoacorde1,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeI.grid(column=3, row=4)
botao_acordeII = tkinter.Button(janela_acordes, text="IIm", command=botaoacorde2,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeII.grid(column=4, row=4)
botao_acordeIII = tkinter.Button(janela_acordes, text="IIIm", command=botaoacorde3,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeIII.grid(column=5, row=4)
botao_acordeIV = tkinter.Button(janela_acordes, text="IV", command=botaoacorde4,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeIV.grid(column=6, row=4)
botao_acordeVI = tkinter.Button(janela_acordes, text="VIm", command=botaoacorde6,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeVI.grid(column=1, row=4)
botao_acordeVII = tkinter.Button(janela_acordes, text="VIIm7(b5)", command=botaoacorde7,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeVII.grid(column=2, row=4)
botao_acordeV1 = tkinter.Button(janela_acordes, text="V7", command=botaoacorde51,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV1.grid(column=3, row=3)
botao_acordeV2 = tkinter.Button(janela_acordes, text="V7/IIm", command=botaoacorde52,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV2.grid(column=4, row=3)
botao_acordeV3 = tkinter.Button(janela_acordes, text="V7/IIIm", command=botaoacorde53,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV3.grid(column=5, row=3)
botao_acordeV4 = tkinter.Button(janela_acordes, text="V7/IV", command=botaoacorde54,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV4.grid(column=6, row=3)
botao_acordeV5 = tkinter.Button(janela_acordes, text="V7/V", command=botaoacorde55,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV5.grid(column=3, row=1)
botao_acordeV6 = tkinter.Button(janela_acordes, text="V7/VIm", command=botaoacorde56,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeV6.grid(column=1, row=3)
botao_acordeIVm = tkinter.Button(janela_acordes, text="IVm", command=botaoacorde48,bg='white',height=3, width=8, disabledforeground='white')
botao_acordeIVm.grid(column=6, row=5)
botao_acordesustIVdim = tkinter.Button(janela_acordes, text="#IVdim", command=botaoacorde49,bg='white', height=3, width=8, disabledforeground='white')
botao_acordesustIVdim.grid(column=7, row=5)

barra_de_progresso = ttk.Progressbar(janelao, orient=HORIZONTAL, length=200, mode='determinate', maximum=100)
barra_de_progresso.grid(column=2, row=6)
nota = ttk.Label(janelao,text='Nota:')
nota.grid(column=2,row=4)
janelao.mainloop()

fim_programa = True