class Squadra:
    def __init__(self,team = []):
        self.team = team
    
    def add(self,x):
        self.team.append(x)
    
    def show(self):
        for x in self.team:
            print(x.nome)