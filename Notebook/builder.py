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
    else: print(f'La tua squadra {squad} batte tutti i tipi, utilizzando {math.ceil(len(squad)/2)}')
    
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

def pretty_comb(combs):
    for comb in combs:
        print(comb)
        
def user_init_squad(squad=[]):
    next_type = "init"
    while next_type != "exit":
        next_type = insertType(input("Inserisci il prossimo tipo: "),squad)
        print(next_type)
    return squad

import requests
import urllib.robotparser
from bs4 import BeautifulSoup
# URL of the website you want to scrape
base_url = 'https://bulbapedia.bulbagarden.net/wiki/'

# Parse the robots.txt file
rp = urllib.robotparser.RobotFileParser()
rp.set_url(base_url + 'robots.txt')
rp.read()

# Function to check if a URL is allowed by robots.txt
def is_allowed(url):
    return rp.can_fetch('*', url)

# Function to scrape a URL if allowed by robots.txt
def scrape_url(url):
    if is_allowed(url):
        response = requests.get(url)
        return response.text
    else:
        print(f"Scraping blocked by robots.txt: {url}")
        return 'blocked'
# Example usage



translation_dict = {
    'Normal' : 'Normale',
    'Fighting' : 'Lotta',
    'Flying' : 'Volante',
    'Poison' : 'Veleno',
    'Ground' : 'Terra',
    'Rock' : 'Roccia',
    'Bug' : 'Coleottero',
    'Ghost' : 'Spettro',
    'Steel' : 'Acciaio',
    'Fire' : 'Fuoco',
    'Water' : 'Acqua',
    'Grass' : 'Erba',
    'Electric' : 'Elettro',
    'Psychic' : 'Psico',
    'Ice' : 'Ghiaccio',
    'Dragon' : 'Drago',
    'Dark' : 'Buio',
    'Fairy' : 'Folletto',
}

import pandas as pd
def convert_from_b4s_to_dataframe(b4s):
    rows = b4s.find_all("tr")
    base_headers = [th.get_text(strip=True) for th in rows[0].find_all(["th", "td"])]
    # individua la colonna Type (se c’è) e prepara i nuovi header
    type_idx = base_headers.index("Type") if "Type" in base_headers else None
    core_headers = (base_headers[:type_idx] if type_idx is not None else base_headers)[:3]
    #aggiungo le colonne first Type e Second Type per esprimere meglio i valori relativi ai tipi pokemon
    headers = core_headers + ["First Type", "Second Type"]
    #Rimuovo ehader MS perchè è adibita all'imamgine ma non ci serve per i nostri scopi
    headers.remove('MS')


    data = []
    last_index_number = '#0001'

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if not cells:
            continue

        texts = [cell.get_text(strip=True) for cell in cells]
        
        base_cells = texts

        if base_cells[0] != '':last_index_number = base_cells[0]
        base_cells.remove('')
        if base_cells[0][0] != '#':
            base_cells.reverse()
            base_cells.append(last_index_number)
            base_cells.reverse()

        base_cells[2] = translation_dict[base_cells[2]]
        if len(base_cells)>=4 : base_cells[3] = translation_dict[base_cells[3]]

        

        if any(base_cells):
            data.append(base_cells)

    return pd.DataFrame(data, columns=headers)


def create_mask(clauses):
    mask = clauses[0]
    for clause in clauses[1:]:
        mask = mask & clause
    return mask


def reduce_df(dataframe,types):
    if not types:
        return dataframe
    
    hits = pd.Series(0, index=dataframe.index, dtype="int64")

    for type_name in types:
        clause = (
            (dataframe["First Type"] == type_name) |
            (dataframe["Second Type"] == type_name)
        )
        hits += clause.astype("int64")  # conta i match

    mask = hits <= 1  # sopravvivono solo i Pokémon con 0 o 1 match
    return dataframe[mask]


def build_extensive_pokemon_df(coverage):
    pokemon = pd.DataFrame()
    for type in coverage:
        for gen in generations:
            second_clause = gen['Second Type'] == type
            first_clause = gen['First Type'] == type
            element = gen[ first_clause | second_clause]
            if not element.empty:
                pokemon = pd.concat([pokemon,element])
    return pokemon


import numpy as np

def choose_pkmon(pokemon,squad,choice):
  
    mask = create_mask([( pokemon['First Type'] == type) | (pokemon['Second Type'] == type ) for type in choice ])

    pick = pokemon.loc[mask].head(1)
    
    if not squad.empty:
        covers_all = all(
            ((squad['First Type'] == t) | (squad['Second Type'] == t)).any()
            for t in choice
        )

        if covers_all:
            return squad
    
    return pd.concat([squad,pick])

def squad_building_step(pokemon,combs,squad):
    #scelta randomica in base ai tipi possibili
    choice = combs[np.random.randint(0,len(combs))]
    combs.remove(choice)
    len_ = len(squad)
    squad = choose_pkmon(pokemon,squad,choice)
    #se non ho aggiunto ritorno
    if len_ == len(squad): return [pokemon,combs,squad]
    
    pokemon = reduce_df(pokemon,choice)
    return [pokemon, combs,squad]


def choose_your_pokemon(coverage):
    np.random.seed()
    squad = pd.DataFrame()
    combs = calculate_combinations(coverage)

    #creo il dataframe in base ai tipi necessari
    pokemon = build_extensive_pokemon_df(coverage)
    
    while(len(combs)>0 and len(squad)<6):
        [pokemon,combs,squad] = squad_building_step(pokemon,combs,squad)

    return squad

def type_input(message):
    next_type = input(message)
    next_type = next_type.lower()
    if wants_to_exit(next_type):return "exit"
    next_type = next_type[0].upper()+next_type[1:]
    assert next_type in pokemon_types, f"{next_type} non è un tipo Pokémon valido"
    return next_type

def interactive_choose_pokemon(pokemon,choice):
  
    mask = create_mask([( pokemon['First Type'] == type) | (pokemon['Second Type'] == type ) for type in choice ])

    possible_picks = pokemon.loc[mask].drop_duplicates()
    print(possible_picks)

    chosen_pokemon = input('inserisci il nome del pokemon che vorresti aggiungere alla squadra')
    print(chosen_pokemon)
    
    chosen = possible_picks[possible_picks['Pokémon'] == chosen_pokemon] 
    if chosen.empty:
        return None
    else:
        return chosen.iloc[0]['Pokémon']


def reduce_coverage(coverage,choices):
    for choice in choices:
        for type in coverage:
            if type == choice:
                coverage.remove(choice)
    return coverage


def interactive_squad_building_step(pokemon,squad,coverage):
    print(coverage)
    choices = []
    while len(choices)<2:
        choice = type_input('Scegli una delle combinazioni di tipi elencati per cercare un pokemon corrispondente, (esempio Terra,Lotta)')
        if choice == 'exit':
            if len(choices)>0:
                break
            else: 
                continue
        choices.append(choice)
    #modifico la copertura in base ai tipi già presenti
    type_list = squad['First Type'].tolist()
    type_list.append(squad['Second Type'].tolist())
    coverage = calculate_coverage(type_list)
    
    
    #scelta randomica in base ai tipi possibili
    chosen = interactive_choose_pokemon(pokemon,choices)

    if chosen == None:
        return [pokemon,squad,coverage]
    
    picked = pokemon[pokemon['Pokémon'] == chosen]
    squad = pd.concat([squad,picked])
    chosen_types = [picked.iloc[0]['First Type'], picked.iloc[0]['Second Type']]
    coverage = reduce_coverage(coverage,chosen_types)
    pokemon = reduce_df(pokemon,choices)
    
    return [pokemon,squad,coverage]



def interactive_choose_your_pokemon(coverage):
    squad = pd.DataFrame()
    # combs = calculate_combinations(coverage)

    #creo il dataframe in base ai tipi necessari
    pokemon = build_extensive_pokemon_df(coverage)
    pokemon = pokemon.drop_duplicates()
    while(len(coverage)>0 and len(squad)<6):
        
        [pokemon,squad,coverage] = interactive_squad_building_step(pokemon,squad,coverage)
        print(squad)

    return squad


coverage = calculate_coverage(['Fuoco','Lotta'],False)

print('Fetching Pokemon from Bulbapedia...')
result = scrape_url(base_url + 'List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number')

#se non ho potuto scrapare allora esco
if result== 'blocked':
    exit(0)

soup = BeautifulSoup(result,'html.parser')

table = soup.find_all('table',class_='roundy')

first_gen = table[0]
second_gen = table[1]
third_gen = table[2]
fourth_gen = table[3]
fifth_gen = table[4]
sixth_gen = table[5]
seventh_gen = table[6]
eight_gen = table[7]
ninth_gen = table[8]

first_gen_df = convert_from_b4s_to_dataframe(first_gen)
second_gen_df = convert_from_b4s_to_dataframe(second_gen)
third_gen_df = convert_from_b4s_to_dataframe(third_gen)
fourth_gen_df = convert_from_b4s_to_dataframe(fourth_gen)
fifth_gen_df = convert_from_b4s_to_dataframe(fifth_gen)
sixth_gen_df = convert_from_b4s_to_dataframe(sixth_gen)
seventh_gen_df = convert_from_b4s_to_dataframe(seventh_gen)
eight_gen_df = convert_from_b4s_to_dataframe(eight_gen)
ninth_gen_df = convert_from_b4s_to_dataframe(ninth_gen)

generations = [first_gen_df,second_gen_df,third_gen_df,fourth_gen_df,fifth_gen_df,sixth_gen_df,seventh_gen_df,eight_gen_df,ninth_gen_df]


squad = interactive_choose_your_pokemon(coverage)



