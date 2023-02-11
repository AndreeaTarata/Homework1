# 1. Citeste de la tastatura un string de dimensiune impara

nume = input('Numele meu: ')
lenx = len(nume)
mijloc = int(lenx/2)
print(lenx)

#afiseaza caracterul din mijloc
print(nume[round(mijloc)])

# 2 folosind assert, verifica daca un string este palindrom

pali = 'cojoc'
print(pali[::-1])


pali1 = input('Introdu un palindrom: ')
assert pali1 == pali1[::-1]

# 3. Folosind o singură linie de cod : Pt o singura linie de cod se foloseste ;
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;


cuv1, cuv2 = input('Stringul: '), input('si: '); print(cuv1 + ' ' + cuv2)

# 4. Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

cuvant, cuv_urma = input('Stringul: '), input('si: ')
print(cuvant + ' ' + cuv_urma)
car1 = cuvant[0]
carM = car1.upper()
print(carM)
prop = cuvant + " " + cuv_urma
print(prop)
car2 = prop[len(prop) - 1]
print(car2)
print(prop)
new_prop = prop.replace(car1, carM)
# new_prop = prop.replace(car1, car1.lower())


# new_prop = prop.replace(car2, car2.lower())
print(new_prop)
carm = car1.lower()

print(new_prop[0].lower() + new_prop[1:] + new_prop[len(new_prop)-1].lower())

# 5.Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ***

user = input('User: ')
parol = input('Parola: ')
lungime = len(parol)
stelute = '*'
lun_stelute = len(stelute)
lun_stelute = lungime
print(lun_stelute)
parol1 = parol.replace(parol, '*'*lungime)
print(f'Parola pt userul: {user} este {parol1} si are {lungime} caractere')



