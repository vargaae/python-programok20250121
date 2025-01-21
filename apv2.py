from random import randint
# --- 2. -----------
print('# --- 2. ----------- ')
# Készítsen tippelő játékot az alábbi instrukciók szerint: 
#   A program sorsoljon egy véletlen számot 1 és 100 között, majd kérdezze meg a felhasználót, hogy szerinte 
# mi lehet az! 
#   Amennyiben a felhasználó nagyobb számot ír be, mint a generált szám, a program írja ki, hogy „túl 
# magas!” 
#   Amennyiben a  felhasználó kisebb számot  ír be,  mint  a  generált  szám, a  program  írja  ki,  hogy „túl 
# alacsony!” 
#   Ismételje a szám bekérését és elbírálását mindaddig, amíg a felhasználónak nem sikerül eltalálnia a 
# generált számot. Ebben az esetben a program írja ki, hogy „eltaláltad!”. 
#   A program számolja tippeket a játék alatt. Ha vége a játéknak, írja ki a tippek számát. Az intervallum-
# felezéses stratégiával a szám legtöbb 7 tippből kitalálható. Ha a tippek száma több, mint 7 a játék végére, 
# írja ki a program, hogy „legközelebb gondold át a stratégiádat, megy ez jobban is!” 

sorsolt:int = randint(1, 100)
probalkozasok:int = 0
tipp:int = -1
print('gondoltam egy szamra, probald meg kitalalni! (1 és 100 közötti számra tippelj) ')
while tipp != sorsolt: 
  tipp:int = int(input('tipped: '))
  if 0 < tipp < 101:
    if tipp > sorsolt: print('tul magas!')
    elif tipp < sorsolt: print('tul alacsony!')
    probalkozasok += 1
  elif tipp == 0 or tipp > 100: print('1 és 100 közötti számra tippelj! ')
print('eltalaltad!')
print(f'probalkozasaid szama: {probalkozasok}')
if probalkozasok > 7: 
  print(f'legközelebb gondold át a stratégiádat, megy ez jobban is!')