"""
1. Declaram expected results - user, password, sold
2. Introducem un username
3. Verificam corectitudinea userului
4. Introducem o parola valida
5. Verificam corectitudinea parolei
6. If all ok - simulat press enter to login
7. Afisam mesaj string in care afisam 'expected sold'
8. Intampinam userul cu un mesaj "cat cash doriti sa transferati?"
9. Afisam in consola daca tranzactia are loc - cat sold ii ramane
10. Extragem si lungimea parolei
11. If lung parolei<5 codul va da "error" (assert)
12. Afisam in consola username-ul, dar parola sa fie inlocuita cu stelute in loc de caracterele propriuzise
"""

user: str = 'andreea'
password: str = 'Abc123!'
# special_characters = '!@#$%^&*()-+?_=,<>/'
sold: int = 50000

# 2
actual_user = input('Introduce nume user: ').lower()

# print(user)
# def remove(user):
#     return user.replace(" ", "")
#
#
# user = 'a n d r e e a'
# print(remove(user))


# 3
# assert user == actual_user
print(actual_user)

# scoate spatiile din cuvantul andreea si chiar daca introduc un spatiu din greseala e corect
def remove(actual_user):
    return actual_user.replace(" ", "")

user = 'a n d r e e a'
print(remove(actual_user))

# 4
actual_password = input('Introdu parola: ').strip().isupper() # strip scoate spatiile din ce introducem la tastatura lstrip - elimina left side si isupper - ne spune daca avem o litera mare
print(actual_password)
# assert password == actual_password





#
len_password = len(password)
assert len_password > 5
print(f'Parola introdusa este ok')
# 6
input('Press Enter to login ')
# 7
print(f'Soldul dvstra este: {sold}')
# 8
cash = int(input('Ce suma doriti sa retrageti?: '))

assert sold - cash >= 0
# dam update la sold!
sold = sold - cash
print(f'Tranzactia a fost efectuata cu succesc. Noul Sold este: {sold}')

# 10
print(len(password))


# 11

# # TODO checkul de parola sa il mutam la inceput
# # tema: daca am introdus un spatiu parola nu mai e corecta - sa eliminam orice spatiu fie ca e la inceput, la sfarsit, etc
# # sa verificam ca ea contine macar o litera mare si un caracter special (parola)
# # 12 tema

a, b, c, d, e = '!', '@', '#', '$', '%'
assert a in password or b in password or c in password or d in password or e in password


