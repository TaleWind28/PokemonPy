
pokemon_types = {
    "Normale": {
        "debolezze": ["Lotta"],
        "resistenze": [],
        "immunità": ["Spettro"],
        "superefficacie": []
    },
    "Fuoco": {
        "debolezze": ["Acqua", "Terra", "Roccia"],
        "resistenze": ["Fuoco", "Erba", "Ghiaccio", "Coleottero", "Acciaio", "Folletto"],
        "immunità": [],
        "superefficacie": ["Erba", "Coleottero", "Ghiaccio", "Acciaio"]
    },
    "Acqua": {
        "debolezze": ["Elettro", "Erba"],
        "resistenze": ["Fuoco", "Acqua", "Acciaio", "Ghiaccio"],
        "immunità": [],
        "superefficacie": ["Fuoco", "Terra", "Roccia"]
    },
    "Erba": {
        "debolezze": ["Fuoco", "Ghiaccio", "Veleno", "Volante", "Coleottero"],
        "resistenze": ["Acqua", "Erba", "Terra", "Elettro"],
        "immunità": [],
        "superefficacie": ["Acqua", "Terra", "Roccia"]
    },
    "Elettro": {
        "debolezze": ["Terra"],
        "resistenze": ["Acciaio", "Elettro", "Volante"],
        "immunità": [],
        "superefficacie": ["Acqua", "Volante"]
    },
    "Ghiaccio": {
        "debolezze": ["Fuoco", "Lotta", "Roccia", "Acciaio"],
        "resistenze": ["Ghiaccio"],
        "immunità": [],
        "superefficacie": ["Erba", "Terra", "Volante", "Drago"]
    },
    "Lotta": {
        "debolezze": ["Volante", "Psico", "Folletto"],
        "resistenze": ["Roccia", "Coleottero", "Buio"],
        "immunità": [],
        "superefficacie": ["Normale", "Roccia", "Acciaio", "Ghiaccio", "Buio"]
    },
    "Veleno": {
        "debolezze": ["Psico", "Terra"],
        "resistenze": ["Erba", "Lotta", "Veleno", "Coleottero", "Folletto"],
        "immunità": [],
        "superefficacie": ["Erba", "Folletto"]
    },
    "Terra": {
        "debolezze": ["Acqua", "Erba", "Ghiaccio"],
        "resistenze": ["Veleno", "Roccia"],
        "immunità": ["Elettro"],
        "superefficacie": ["Fuoco", "Elettro", "Veleno", "Roccia", "Acciaio"]
    },
    "Volante": {
        "debolezze": ["Elettro", "Ghiaccio", "Roccia"],
        "resistenze": ["Erba", "Lotta", "Coleottero"],
        "immunità": ["Terra"],
        "superefficacie": ["Erba", "Lotta", "Coleottero"]
    },
    "Psico": {
        "debolezze": ["Buio", "Spettro", "Coleottero"],
        "resistenze": ["Lotta", "Psico"],
        "immunità": [],
        "superefficacie": ["Lotta", "Veleno"]
    },
    "Coleottero": {
        "debolezze": ["Fuoco", "Volante", "Roccia"],
        "resistenze": ["Erba", "Lotta", "Terra"],
        "immunità": [],
        "superefficacie": ["Erba", "Psico", "Buio"]
    },
    "Roccia": {
        "debolezze": ["Acqua", "Erba", "Lotta", "Acciaio", "Terra"],
        "resistenze": ["Normale", "Fuoco", "Veleno", "Volante"],
        "immunità": [],
        "superefficacie": ["Fuoco", "Ghiaccio", "Volante", "Coleottero"]
    },
    "Spettro": {
        "debolezze": ["Spettro", "Buio"],
        "resistenze": ["Veleno", "Coleottero"],
        "immunità": ["Normale", "Lotta"],
        "superefficacie": ["Psico", "Spettro"]
    },
    "Drago": {
        "debolezze": ["Ghiaccio", "Drago", "Folletto"],
        "resistenze": ["Fuoco", "Acqua", "Erba", "Elettro"],
        "immunità": [],
        "superefficacie": ["Drago"]
    },
    "Buio": {
        "debolezze": ["Lotta", "Coleottero", "Folletto"],
        "resistenze": ["Spettro", "Buio"],
        "immunità": ["Psico"],
        "superefficacie": ["Psico", "Spettro"]
    },
    "Acciaio": {
        "debolezze": ["Fuoco", "Lotta", "Terra"],
        "resistenze": ["Normale", "Volante", "Roccia", "Coleottero", "Acciaio", "Erba", "Psico", "Ghiaccio", "Drago", "Folletto"],
        "immunità": ["Veleno"],
        "superefficacie": ["Ghiaccio", "Roccia", "Folletto"]
    },
    "Folletto": {
        "debolezze": ["Acciaio", "Veleno"],
        "resistenze": ["Lotta", "Coleottero", "Buio"],
        "immunità": ["Drago"],
        "superefficacie": ["Lotta", "Buio", "Drago"]
    }
}

def covered_types(squad):
    
    if(len(squad)== 0):return set()

    coverage = set(analyzed_type 
                    for analyzed_type in pokemon_types 
                    for unchecked_type in pokemon_types[analyzed_type]["debolezze"] 
                    for acquired in squad  if unchecked_type == acquired)
    return coverage

def uncovered_types(squad):
    coverage = covered_types(squad)
    
    uncovered_types = set(key for key in pokemon_types.keys())
    
    if len(squad) == 0 or len(coverage)== 0 :
        return uncovered_types
    else:
        return uncovered_types.difference(coverage)
    
def create_weights():return {pkmon_type:len(pokemon_types[pkmon_type]["superefficacie"]) for pkmon_type in pokemon_types}

def calculate_weight(super_effectivness,useless_types):
    weight = len(super_effectivness) - sum(1 for pkmon_type in super_effectivness for useless_type in useless_types if pkmon_type == useless_type)
    if weight == 0:
        return -1
    else:
        return weight

def update_wheights(types_checked):
    return {pkmon_type:calculate_weight(pokemon_types[pkmon_type]["superefficacie"],types_checked) for pkmon_type in pokemon_types}

def next_weight(weighted_types):
    max = 0
    for type in weighted_types:
        if weighted_types[type] > max :
            max = weighted_types[type]
    return max

def initialize_squad(squad=[]):
    #scrito qui solo per migliorare la leggibilità del codice
    mandatory_types = {pokemon_types[pkmon_type]["debolezze"][0] for pkmon_type in pokemon_types if len(pokemon_types[pkmon_type]["debolezze"]) == 1}
    return list(dict.fromkeys([*squad,*mandatory_types]))

def next_types_to_add(coverage):

    if(len(coverage)==0):return set(initialize_squad());

    updated = update_wheights(coverage)
    
    return set(
            pkmon_type 
            for pkmon_type in pokemon_types 
            for covered_type in coverage 
            if pkmon_type != covered_type and updated[pkmon_type] == next_weight(updated)
    )

def find_best_types(squad,want_print = True ):
    #cerco i tipi richiesti
    requested_types = uncovered_types(squad);
    #se non ne ho allora non devo fare niente
    if len(requested_types)== 0 :return print('La tua squadra batte già tutti i tipi, complimenti!')
    #creo la coverage dei tipi in base alla squadra
    coverage = covered_types(squad)
    #cerco i prossimi tipi da far aggiungere all'utente
    suggested_types = next_types_to_add(coverage)
    if want_print: print(f'La squadra ha bisogno di questi tipi: {suggested_types}')
    return suggested_types

def wants_to_exit(user_input):
    if user_input==" ":return True
    if user_input=="":return True
    if user_input=="\n":return True
    
    return False

def insertType(next_type,squad=[]):
    try:
        next_type = next_type.lower()
        if wants_to_exit(next_type):return "exit"
        next_type = next_type[0].upper()+next_type[1:]
        assert next_type in pokemon_types, f"{next_type} non è un tipo Pokémon valido"
        squad.append(next_type)
        return next_type
    except AssertionError as error:
        print(f'{error}')
        return error

import math
def interactive_calculate_coverage(squad):
    first = True
    while len(covered_types(squad)) <18 and (math.ceil(len(squad)/2) <6 or len(squad) <12):
        print(f'Squadra attuale: {squad}')
        if first:
            squad = initialize_squad(squad)
            first = False
            print(f'Alla tua squadra sono stati aggiunti i tipi: {initialize_squad()}, in quanto sono necessari per battere tipi con una sola debolezza')
            continue
        find_best_types(squad)
        next_type = insertType(input('Inserisci il prossimo tipo: '),squad)
        if next_type == 'exit': return squad 
        print(f'Tipo {next_type} aggiunto')
    
    if len(covered_types(squad))<18:print(f'Purtroppo la tua squadra non riesce a battere tutti i tipi')
    else: print(f'La tua squadra {squad} batte tutti i tipi, utilizzando {math.ceil(len(squad)/2)} slot')
    
    return squad

def calculate_coverage(squad,want_print = True):
    first = True
    while len(covered_types(squad)) <18:
        if want_print: print(f'Squadra attuale: {squad}')
        if first:
            squad = initialize_squad(squad)
            first = False
            if want_print:print(f'Alla tua squadra sono stati aggiunti i tipi: {initialize_squad()}, in quanto sono necessari per battere tipi con una sola debolezza')
            continue
        suggested_types = find_best_types(squad,want_print)
        if want_print:print(suggested_types)
        if suggested_types: squad.append(suggested_types.pop())
    print(f'La tua squadra {squad} batte tutti i tipi')
    return squad

import itertools

def calculate_combinations(squad):
    return list(itertools.combinations(squad, 2))

def pretty_print_combs(combs_list):
    i = 1
    for comb in combs_list:
        print(comb,end="\t")
        if i%7== 0 :
            print('\n')
        i+=1
    return

def user_init_squad(squad=[]):
    next_type = "init"
    while next_type != "exit":
        next_type = insertType(input("Inserisci il prossimo tipo: "),squad)
    return squad


# Script Effettivo
# print("Scegli i tipi iniziali dei pokemon che vuoi avere in squadra, oppure metti quelli che hai già; Appena hai finito premi invio per uscire")

# squad = user_init_squad();

# print(f"La tua squadra ha attualmente questi tipi: {squad}");

# squad = interactive_calculate_coverage(squad)
squad = calculate_coverage([],want_print=False);
combs = calculate_combinations(squad)

print(f'Hai a disposizione {len(combs)} combinazioni di tipi, che sono elencate di seguito')

# pretty_print_combs(combs)