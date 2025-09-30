from .tipi import *

def calcdeb(coverage):
    obj = {"normale":0,"lotta":0,"volante":0,"veleno":0,"terra":0,"roccia":0,"coleottero":0,"spettro":0,"acciaio":0,"fuoco":0,"acqua":0,"erba":0,"elettro":0,"psico":0,"ghiaccio":0,"drago":0,"buio":0,"folletto":0}
    at = Arraytipi()
    for x in coverage.need:
        for y in x.weak:
            obj[y]+=1
    mem = -1
    tp = ""
    for x in obj:
        if obj[x] > mem:
            mem =obj[x]
            tp = x 
    for x in at.tobeat:
        if x.nome == tp:
            coverage.add_beaten(x)
            break

def complete(coverage):
    if coverage.Is_Full():  print("coverage completata", end=" ");return coverage.show_team()        #Controllo che la coverage non sia completa
    calcdeb(coverage)
    return complete(coverage)

# #TEST CASE
# c = Coverage()
# c.add_beaten(acciaio)
# c.add_beaten(lotta)
# c.add_beaten(normale)
# complete(c)
# c.show_team()