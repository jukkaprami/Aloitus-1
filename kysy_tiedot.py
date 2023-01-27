# OHJELMA, JOKA KYSYY BMI-TIETOJA USEASTA KUNTOILIJASTA
# =====================================================

# KIRJASTOT JA MODUULIT
# ---------------------

# Tuodaan fitness.py:n sisältämät toiminnot tähän ohjelmaan
import fitness

# Kysytään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa
while True: # Ikuinen silmukka, jossa ollaan kunnes annetaan tyhjä pituus
    
    pituus_teksti = input('Pituus (cm), tyhjä lopettaa: ')
    if pituus_teksti == '':
        break
    
    paino_teksti = input('Paino (kg): ')

    pituus = float(pituus_teksti)
    paino = float(paino_teksti)

    # Lasketaan painoindeksi fitness-modulin laske_bmi-funktiolla
    bmi = fitness.laske_bmi(paino, pituus)

    print('Painoindeksi on', bmi)