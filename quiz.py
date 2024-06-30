import random
import biblioteca_mus as mus

acertos=0
tons=['C','G','F']
def perguntas():
    global acertos
    respostas=['B#','C','C#','Db','D','D#','Eb','E','Fb','E#','F','F#','Gb','G','G#','Ab','A','A#','Bb','B','Cb']
    opcoes=['1','2','3','4']
    tom=random.choice(tons)
    select_pergunta=random.randint(1,12)
    if select_pergunta==1:
        pergunta=f"Qual é a segunda menor de {tom}?"
        resposta_certa=mus.Mus(tom).notas['b2']
    elif select_pergunta==2:
        pergunta=f"Qual é a segunda maior de {tom}?"
        resposta_certa=mus.Mus(tom).notas['2']
    elif select_pergunta==3:
        pergunta=f"Qual é a terça menor de {tom}?"
        resposta_certa=mus.Mus(tom).notas['b3']
    elif select_pergunta==4:
        pergunta=f"Qual é a quarta justa de {tom}?"
        resposta_certa=mus.Mus(tom).notas['4']
    elif select_pergunta==5:
        pergunta=f"Qual é a quarta aumentada de {tom}?"
        resposta_certa=mus.Mus(tom).notas['#4']
    elif select_pergunta==6:
        pergunta=f"Qual é a quinta diminuta de {tom}?"
        resposta_certa=mus.Mus(tom).notas['b5']
    elif select_pergunta==7:
        pergunta=f"Qual é a quinta justa de {tom}?"
        resposta_certa=mus.Mus(tom).notas['5']
    elif select_pergunta==8:
        pergunta=f"Qual é a quinta aumentada de {tom}?"
        resposta_certa=mus.Mus(tom).notas['#5']
    elif select_pergunta==9:
        pergunta=f"Qual é a sexta menor de {tom}?"
        resposta_certa=mus.Mus(tom).notas['b6']
    elif select_pergunta==10:
        pergunta=f"Qual é a sexta maior de {tom}?"
        resposta_certa=mus.Mus(tom).notas['6']
    elif select_pergunta==11:
        pergunta=f"Qual é a sétima menor de {tom}?"
        resposta_certa=mus.Mus(tom).notas['b7']
    elif select_pergunta==12:
        pergunta=f"Qual é a sétima maior de {tom}?"
        resposta_certa=mus.Mus(tom).notas['7']



    del(respostas[respostas.index(resposta_certa)])
    opcao_certa=random.choice(opcoes)
    del(opcoes[opcoes.index(opcao_certa)])
    resposta_errada1=random.choice(respostas)
    del(respostas[respostas.index(resposta_errada1)])
    opcao_errada1=random.choice(opcoes)
    del(opcoes[opcoes.index(opcao_errada1)])
    resposta_errada2=random.choice(respostas)
    del(respostas[respostas.index(resposta_errada2)])
    opcao_errada2=random.choice(opcoes)
    del(opcoes[opcoes.index(opcao_errada2)])
    resposta_errada3=random.choice(respostas)
    del(respostas[respostas.index(resposta_errada3)])
    opcao_errada3=opcoes[0]
    lista_respostas=[opcao_certa+f': {resposta_certa}',opcao_errada1+f': {resposta_errada1}',opcao_errada2+f': {resposta_errada2}',opcao_errada3+f': {resposta_errada3}']
    lista_respostas.sort()
    print(pergunta,'\n', lista_respostas[0],'\n', lista_respostas[1],'\n', lista_respostas[2],'\n',lista_respostas[3],'\n')
    palpite=input('Sua resposta(só o número)>>>')

    if palpite == opcao_certa:
        print('Certo!\n')
        acertos +=1
    else:
        print(f'Errado!\nResposta certa: {resposta_certa}\n')
        


while acertos<5:
    perguntas()
    print(f'Número de acertos: {acertos}\nFaltam {5-acertos} para vencer\n')

print('FIM')
