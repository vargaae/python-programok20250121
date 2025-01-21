from filmek import *
# --- 3. -----------
print('# --- 3. ----------- ')
# Adott az UTF-8-as kódolású filmek.txt állomány, amely népszerű filmek adatait tartalmazza*. 
# Az állomány sorai azonos szerkezetűek, az adattagok pontosvessző karakter választja el egymástól. Az 
# állomány egy sora például: 
# Vissza a jövőbe;1985;Kaland, Vígjáték, Sci-Fi 
# ahol adattagok jelentése rendre a következők: 
#   a film címe 
#   a megjelenésének éve 
#   a film műfajai, vesszővel elválasztva 
# Olvassa be az állomány tartalmát, és tárolja le egy objektumpéldányokat tartalmazó listába! Ennek a 
# listának a felhasználásával oldja meg az alábbi feladatokat! A terminálra történő kiírást igénylő feladatok 
# eredményét a mintán látható módon jelenítse meg! 
filmlista:list[Filmek] = []

stream = open(file='filmek.txt', mode='r', encoding='utf-8')
for s in stream: filmlista.append(Filmek(s))
# 1.  Jelenítse meg a terminálon, hogy hány film adatai találhatóak az állományban! 
print(f'3.1: filmek szama: {len(filmlista)}')
# 2.  Határozza meg és jelenítse meg a terminálon, hogy hány 21. századi film van a listán (2001, vagy 
# későbbi megjelenésű). 
# KIVÁLOGATÁS
huszonegyedik_szazadiak: list[Filmek] = []
for f in filmlista:
    if int(f.ev) > 2000:
        huszonegyedik_szazadiak.append(f)
print(f'3.2: 21. szazadi filmek szama: {len(huszonegyedik_szazadiak)} db ')
# 3.  Határozza meg, és írja ki a terminálra, hogy mi a fileban szereplő legkorábbi megjelenésű film címe!

# szélsőérték meghatározás: megadja az adott sorozat legkisebb/legnagyobb elemének helyét

legkorabbi:int = 0
for index in range(1, len(filmlista)):
    if filmlista[index].ev < filmlista[legkorabbi].ev:
        legkorabbi = index
print(f'3.3: legkorabbi film: {filmlista[legkorabbi].film_cim}')

# 4.  kérjen be a felhasználótól egy műfaj nevét. Listázza ki Azon filmek címét, melyek műfajmegjelölései 
# közt szerepel a beírt szó! Ha egyetlen ilyen műfajú cím sincs a filmek közt, az „Ilyen műfajú film nem 
# található” szöveg jelenjen meg! 
keresett_mufaj = input('3.4 irja be a keresett mufaj nevet: ')
print(f'az "{keresett_mufaj}" mufajmegjelolesu filmek cimei:')
van_talalat = False
for f in filmlista:
    if keresett_mufaj in f.mufajok:
        print(f'         -{f.film_cim}')
        van_talalat = True
if not van_talalat:
        print("Ilyen műfaju film nem található")