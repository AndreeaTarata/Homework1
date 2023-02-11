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



user = 'and'
password = 'AAA'
sold = 5
stelute = '************'

actual_user = input('Introdu User: ')

print(actual_user)
assert user == actual_user

actual_password = input('Introdu pass: ')

assert password == actual_password
password = stelute
print(stelute)





print(len(password))

len_password = len(password)
assert len_password > 2
print("Lungime parola este ok!")

input('Print Enter to login: ')

input(f'Soldul dvtrs este: {sold}')
cash = int(input("cat cash doriti: "))
sold = sold - cash
print(f'Noul sold: {sold}')

assert sold >= 0



# a = 1
# assert a == 1
# print('corect')
# # assert a == 2
# # print('not')
#
# prop = 'Andy este prescurtarea de la Andrei'
# print(len(prop))
# print(prop[0])
# print([prop[0:20:2]])
# print(prop[::-1])
# print(prop.upper())
cuvant, cuv_urma = input('Stringul: '), input('si: ')
print(cuvant + ' ' + cuv_urma)
car1 = cuvant[0]
carM = car1.upper()
print(carM)
prop = cuvant + " " + cuv_urma
print(prop)
car2 = prop[len - 1]
print(car2)
print(prop)
new_prop = prop.replace(car1, car1.lower())
new_prop = prop.replace(car2, car2.lower())
print(new_prop)