from Module import * #importa tutto il contenuto della directory

# t = team.Squadra()
# t.add(tipi.acciaio)
# t.show()
# tp = tipi.Arraytipi()

# for x in tp.tobeat:
#     print (x.nome)

# c = copertura.Coverage()

# #Test Case
# c.add_beaten(tipi.acciaio)
# c.add_beaten(tipi.lotta)
# c.add_beaten(tipi.normale)
# c.show_team()
# c.Permuta()
#TEST CASE
c = copertura.Coverage()
c.add_beaten(tipi.terra)
c.add_beaten(tipi.erba)
c.add_beaten(tipi.lotta)
c.add_beaten(tipi.psico)
c.add_beaten(tipi.acciaio)
c.add_beaten(tipi.elettro)
c.add_beaten(tipi.roccia)
c.add_beaten(tipi.folletto)
c.add_beaten(tipi.fuoco)

building.complete(c)