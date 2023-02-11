"""
1. O variabila este o portiune din memorie in care se pot pune date/valori
2. String
Int
Float
Bool
"""

nume: str = 'Andreea'
numar = int(10)
cash = 50000.75
activ: bool = True

# 3 Utilizeaza functia type pt a verifica daca au tipul de date asteptat
print(type(nume))
print(type(numar))
print(type(cash))
print(type(activ))

# 4 Rotunjeste 'float'-ul folosind functia round si salveaza aceasta modificare in aceeasi variabila (suprascriere).
# Verifica tipul acesteia

cash = round(cash)

print(cash)
print(type(cash))

# 5 Foloseste print si printeza in consola 4 propozitii folosind cele 4 variabile
# Rezolva nepotrivirile de tip prin ce metoda doresti

print(f'Numele meu este Andreea: {nume}')

print(f'Numarul meu norocos este: {numar}')
print(f'O sa primesc cadou suma de: {cash}')
print(f'Sunt o persoana activa: {activ}')

# 6. Citeste de la tastatura: numele, prenumele. Afiseaza: 'Numele complet are x caractere

numele = input('Numele meu este: ')
prenumele = input('Prenumele meu este: ')
len_numesipren = int(len(numele) + len(prenumele))
print(f'Numele complet are: {len_numesipren}')

# 7. Citeste de la tastatura: lungimea, latimea si afiseaza aria dreptunghiului este x

lungimea = int(input('Lungimea: '))
latimea = int(input('Latimea: '))
print(f'Aria dreptunghiului este: {latimea*lungimea}')

# 8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock': afiseaza de cate ori apare cuvantul 'the'

prop = 'Coral is either the stupidest animal or the smartest rock'
the = prop.count('the')

# 9 Printeaza rezultatul
print(the)

# 10 Folositi un assert pt a verifica daca acest string contine doar numere

print(prop.isnumeric())
# assert prop.isnumeric() == True




