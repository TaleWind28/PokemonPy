class Tipo:
    def __init__(self,nome,efficacia,debolezze):
        self.nome = nome
        self.weak = debolezze    #array
        self.eff = efficacia     #array
        #self.res = resistenze   #array

class Doppiotipo:
    def __init__(self,t1,t2):
        self.first = t1
        self.second = t2

class Arraytipi():
    def __init__(self):
        self.tobeat = [normale,lotta,volante,veleno,terra,roccia,coleottero,spettro,acciaio,fuoco,acqua,erba,elettro,psico,ghiaccio,drago,buio,folletto]

#dichiarazione dei tipi pokemon
normale =  Tipo("normale",[],["lotta"])
lotta =  Tipo("lotta",["acciaio","roccia","ghiaccio","normale","buio"],["psico","volante","folletto"])
volante =  Tipo("volante",["lotta","erba","coleottero"],["roccia","elettro","ghiaccio"])
veleno =  Tipo("veleno",["folletto","erba"],["psico","terra"])
terra =  Tipo("terra",["acciaio","roccia","veleno","elettro","fuoco"],["acqua","ghiaccio","erba"])
roccia =  Tipo("roccia",["volante","coleottero","fuoco","ghiaccio"],["acqua","acciaio","erba","lotta","terra"])
coleottero =  Tipo("coleottero",["erba","psico","buio"],["roccia","fuoco","volante"])
spettro =  Tipo("spettro",["psico","spettro"],["spettro","buio"])
acciaio =  Tipo("acciaio",["ghiaccio","roccia","folletto"],["terra","fuoco","lotta"])
fuoco =  Tipo("fuoco",["erba","coleottero","ghiaccio","acciaio"],["terra","acqua","roccia"])
acqua =  Tipo("acqua",["fuoco","terra","roccia"],["elettro","erba"])
erba =  Tipo("erba",["terra","roccia","acqua"],["veleno","fuoco","volante","ghiaccio","coleottero"])
elettro =  Tipo("elettro",["volante","acqua"],["terra"])
psico =  Tipo("psico",["veleno","lotta"],["coleottero","buio","spettro"])
ghiaccio =  Tipo("ghiaccio",["volante","erba","terra","drago"],["lotta","fuoco","acciaio","roccia"])
drago =  Tipo("drago",["drago"],["drago","ghiaccio","folletto"])
buio =  Tipo("buio",["spettro","psico"],["lotta","coleottero","folletto"])
folletto =  Tipo("folletto",["drago","buio","lotta"],["acciaio","veleno"])

