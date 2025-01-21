# --- 1. ----------- 
print('# --- 1. ----------- ')
# Kérjen be a terminálról két egész számot (a és b). Ha a felhasználó valamelyik inputot 0-ra állíja be, ne
# folytatódjon a program futása! Határozza meg a két szám összegének és szorzatának hányadosát [(a+b) / 
# (a*b)]. Ha a hányados egész szám (1-gyel osztva 0-t ad maradékul), akkor írja ki a terminálra, hogy „egész” 
# különben pedig azt, hogy „valós” szám. 
a:int = int(input(f'irja be "a" erteket: '))
if a > 0:
    b:int = int(input(f'irja be "b" erteket: '))
    if b > 0: 
        hanyados:float = (a+b) / (a*b)
        print(f'[({a}+{b}) / ({a}*{b})] = {hanyados}')
        print("valós szám") if hanyados % 1 else print("egész szám")