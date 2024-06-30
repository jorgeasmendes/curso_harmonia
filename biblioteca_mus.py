import random
musC = ['C','Db','D','Eb','E','F','F#','Gb','G','G#','Ab','A','Bbb','Bb','B','D#']
musG = ['G','Ab','A','Bb','B','C','C#','Db','D','D#','Eb','E','Fb','F','F#','A#']
musF = ['F','Gb','G','Ab','A','Bb','B','Cb','C','C#','Db','D','Ebb','Eb','E','G#']



class Mus():
    def __init__(self, fundamental='C'):
        self.fundamental=fundamental
        if fundamental.lower()=='c':
            n=musC[:]
        elif fundamental.lower()=='g':
            n=musG[:]
        elif fundamental.lower()=='f':
            n=musF[:]
        self.notas={'1':n[0], 'b2':n[1], 'b9':n[1],'2':n[2], '9':n[2],'b3':n[3],'3':n[4], '4':n[5],'11':n[5],
                    '#4':n[6],'#11':n[6],'b5':n[7],'5':n[8],'#5':n[9],
                    'b6':n[10],'b13':n[10],'6':n[11],'13':n[11],'bb7':n[12], 'b7':n[13], '7':n[14],'#9':n[15]}
        self.escalaM=f'{self.notas['1']}  {self.notas['2']}  {self.notas['3']}  {self.notas['4']}  {self.notas['5']}  {self.notas['6']}  {self.notas['7']}'
        self.escalam=f'{self.notas['1']}  {self.notas['2']}  {self.notas['b3']}  {self.notas['4']}  {self.notas['5']}  {self.notas['b6']}  {self.notas['b7']}'
        self.escalamh=f'{self.notas['1']}  {self.notas['2']}  {self.notas['b3']}  {self.notas['4']}  {self.notas['5']}  {self.notas['b6']}  {self.notas['7']}'
        self.escalamm=f'{self.notas['1']}  {self.notas['2']}  {self.notas['b3']}  {self.notas['4']}  {self.notas['5']}  {self.notas['6']}  {self.notas['7']}'
    def chord(self, grau, tipo):
        return self.notas[grau]+tipo
    


