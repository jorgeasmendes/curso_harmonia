#importando bibliotecas
import mutagen
from mutagen.id3 import ID3, COMM
from mutagen.mp3 import MP3
from datetime import datetime, timedelta
import time
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import threading
import pygame 

#Iniciar player de música:
pygame.mixer.init()

#Pedindo para usuario abrir o arquivo
def abrir_arquivo():
    global lista_acordes
    global tamanho_musica
    global audiometa
    global caminho_arquivo_mp3
    global audiomp3
    caminho_arquivo_mp3 = tkinter.filedialog.askopenfilename(filetypes=[('Arquivos MP3', '*.mp3')], title = "Escolha um arquivo mp3") 
    audiomp3 = MP3(caminho_arquivo_mp3)
    pygame.mixer.music.load(caminho_arquivo_mp3)
    duracao = audiomp3.info.length
    tamanho_musica = timedelta(seconds=duracao)
    try:
        audiometa = ID3(caminho_arquivo_mp3)
    except:
        audiometa=ID3()
    botao_iniciar.config(state='normal')
    botao_parar.config(state='normal')




nome_musica='Sem nome'
tonalidade='C'
def salvar_arquivo():
    nome_musica=inserir_titulo.get()
    tonalidade=inserir_tonalidade.get()
    texto=""
    texto=texto+nome_musica+'\n'
    texto=texto+tonalidade+'\n'
    texto=texto+str(tamanho_musica)
    for chord in lista_acordes:
        texto=texto+'\n'
        for elemento in chord:
            elemento = str(elemento)
            elemento = elemento.replace('.', ' ')
            elemento = elemento.replace(':',' ')
            texto=texto+elemento+' '
    pygame.mixer.music.unload()
    audiometa.add(COMM(encoding=3, text=[texto]))
    audiometa.save(caminho_arquivo_mp3)
    pygame.mixer.music.load(caminho_arquivo_mp3)
    botao_salvar.config(state='disabled')



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
    global lista_acordes
    global acorde
    lista_acordes=[]
    acorde=[]
    acorde.append(acorde_palpite)
    pygame.mixer.music.play()
    print('start')
    start_musica = datetime.now()
    end_musica = start_musica + tamanho_musica
    ativar_inicio = True
    botao_iniciar.config(state='disabled')
    botao_abrir_arquivo.config(state='disabled')

#botão stop
def comando_botao_stop():
    global ativar_inicio
    global ver_gabarito
    global acorde_palpite
    pygame.mixer.music.stop()
    ativar_inicio = False
    botao_iniciar.config(state='normal')
    botao_abrir_arquivo.config(state='normal')
    desmarcar_botoes()
    acorde_palpite = 0

#checagem para salvamento de acordes
acorde=[]
lista_acordes=[]
def checagem():
    global acorde
    global lista_acordes
    acorde.append(datetime.now()-start_musica)
    lista_acordes.append(acorde)
    acorde=[]
    acorde.append(acorde_palpite)





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
   

def finalizacao():
    global ativar_inicio
    global end_musica
    global lista_acordes
    acorde.append(tamanho_musica)
    lista_acordes.append(acorde)
    print('Fim da música!')
    end_musica=datetime.now()
    ativar_inicio = False
    botao_iniciar.config(state='normal')
    botao_salvar.config(state='normal')
    botao_abrir_arquivo.config(state='normal')
    




def ciclo_checagem():
    global fim_programa
    global tempo_corrido
    fim_programa = False
    while fim_programa ==False:
        if ativar_inicio == True:
            if datetime.now() >= end_musica:
                finalizacao()
        time.sleep(0.5)

def ativar_threads():
    ciclo_checar = threading.Thread(target=ciclo_checagem)
    ciclo_checar.start()

#criando ambiente visual
janelao = Tk()
janelao.geometry('600x600')
janelao.title('Ouvido harmônico')
ativar_threads()
inserir_titulo= Entry(janelao, width=15)
inserir_titulo.grid(column=1,row=2)
inserir_tonalidade= Entry(janelao, width=5)
inserir_tonalidade.grid(column=1,row=3)
botao_abrir_arquivo = tkinter.Button(janelao, text='Abrir arquivo', command=abrir_arquivo)
botao_abrir_arquivo.grid(column=1,row=1)
botao_iniciar = tkinter.Button(janelao, text="Iniciar música", command=comando_botao_start, bg='blue',fg='white', state='disabled')
botao_iniciar.grid(column=2, row=2)
botao_parar = tkinter.Button(janelao, text="Stop", command=comando_botao_stop, bg='red',fg='white',state='disabled')
botao_parar.grid(column=2, row=3) 
botao_salvar = tkinter.Button(janelao, text="Salvar", command=salvar_arquivo, bg='red',fg='white',state='disabled')
botao_salvar.grid(column=2, row=4) 


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

janelao.mainloop()

fim_programa = True