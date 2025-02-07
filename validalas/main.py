def egyenletvizsgalat(egyenlet: str) -> bool:
    nyito_zarojel = 0
    
    for elem in egyenlet:
        if elem == "(":
            nyito_zarojel += 1
        elif elem == ")":
            if nyito_zarojel == 0:
                return False  # Ha egy lezáró zárójel előbb jön, mint nyitó
            nyito_zarojel -= 1

    return nyito_zarojel == 0  # Ha minden nyitó zárójelhez van egy lezáró

# Teszteljük a függvényt
print(egyenletvizsgalat("(3 + 9) + 9)"))  # False
print(egyenletvizsgalat("((3 + 9) + 9)"))  # True
print(egyenletvizsgalat("((3 + 9) + 9"))  # False
print(egyenletvizsgalat("()()()"))  # True
print(egyenletvizsgalat(")(3 + 9) + 9)(")) # False
print(egyenletvizsgalat("()3 + 9( + 9)"))  # True