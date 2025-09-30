from .tipi import *

class Coverage:
    def __init__(self):
        self.team = []                      # "Squadra" pokemon             :Tipo
        self.beaten = []                    # tipi battuti con la "squadra" :stringhe
        self.need = Arraytipi().tobeat      # tipi ancora da battere        :Tipo
        self.poss = []                      # possibili combinazioni        :Doppiotipo

    def add_beaten(self,tipo):                          #Aggiunge un tipo alla "Squadra",rimuove quelli su cui è superefficace dal need ed aggiunge i tipi rimossi a beaten
        self.team.append(tipo)
        for x in tipo.eff:
            for y in self.need:
                if x == y.nome:
                    self.need.remove(y)
                    self.beaten.append(x)
        
    def show_team(self):                                #Stampa la "Squadra" ottenuta
        i=1
        print("[",end="")
        for x in self.team:
            if i == self.team.__len__():
                print(x.nome,end="")
            else:
                print(x.nome,end=",")
                i+=1
        print("]")
    
    def Is_Full(self):                                  #Ritorna true se ho coperto tutti i tipi
        if self.need.__len__() == 0:
            return True
        return False
    
    def show_comb(self):                                #Stampa tutte le combinazioni
        i=1
        print("[",end="")
        for x in self.poss:
            if i == self.poss.__len__():
                print(x.first+"/"+x.second,end="")
            else:
                print(x.first+"/"+x.second,end=",")
                i+=1
        print("]")
    
    def Permuta(self):                                  #Calcola tutte le possibili combinazioni di tipi da poter aggiungere alla squadra per completare la coverage
        count = 0;pteam =[]
        for x in self.team:
            pteam.append(x.nome)
        for x in pteam:
            for y in pteam:
                if x != y:
                    self.poss.append(Doppiotipo(x,y))
                    count+=1
            pteam.remove(x)
        self.show_comb()
        return print(count,"numero di combinazioni di tipi possibili")
    
#Test Case
# c = Coverage()
# c.add_beaten(acciaio)
# c.add_beaten(lotta)
# c.add_beaten(normale)
# c.show_team()
# c.Permuta()