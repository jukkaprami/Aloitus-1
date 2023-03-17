# Esimerkkejä päivämäärien, tiedostojen ja JSON-tietojen käytöstä

import json # Sisäänrakennettu kirjasto JSON objektien käsittelyä varten


#  Luodaan tyhjä lista pino perustaksi
jumppari_lista = []
# Määritellään Python-sanakirja
jumppari = {'nimi': 'Erkki', 'Pituus': 171, 'Paino': 75.5}
jumppari2 = {'nimi': 'Essi', 'Pituus': 165, 'Paino': 61.2}

# Lisätään jumpparit listaan
jumppari_lista.append(jumppari)
jumppari_lista.append(jumppari2)

print(jumppari_lista)

json_jumppari = json.dumps(jumppari)

print(json_jumppari)

"""""
# Luodaan tiedosto
file_to_use = open('kuntoilijat.json', 'x')
file_to_use.close() # Suljetaan tiedosto operaation jälkeen

# Kirjotetaan tiedostoon JSON-objekti
file_to_use = open('kuntoilijat.json', 'w')
json.dump(jumppari, file_to_use) # Muutetaan sanakirja JSON-muotoon ja tallennetaan 
file_to_use.close() # Suljetaan tiedosto

# Luetaan JSON-objekti tiedostosta
file_to_use = open('kuntoilijat.json', 'r')
data = json.load(file_to_use)
file_to_use.close()
print(data)


# Lisätään toinen JSON-objekti tiedoston loppuun
with open('kuntoilijat.json', 'a') as file_to_use:
    json.dump(jumppari2, file_to_use)
"""

with open('kuntoilijat.json', 'w') as file_to_use:
    json.dump(jumppari_lista, file_to_use, indent=4)

with open('kuntoilijat.json', 'r') as file_to_use:
    read_data = json.load(file_to_use)
    last_data = read_data.pop()
    print(last_data)
