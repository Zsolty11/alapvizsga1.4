'''
Visszaszámlálás.

Egy rakéta indítása előtt több órával visszaszámlálást kezdenek és óránként egyet számolnak vissza a rakéta indításáig. 
A felhasználó határozza meg, hogy hány órás a visszaszámlálás. 
A visszaszámlálást minden órában egy órára felfüggeszthetik, ha valamilyen váratlan esemény – műszaki hiba, időjárási probléma – merül fel. 
Amikor a visszaszámlálás eléri a 0-t, a rakétát fellövik.

Írjon programot, amely a visszaszámlálás számait jeleníti meg a képernyőn! 
Természetesen nem kell a visszaszámlálás lépései között eltelni időnek – minden üzenet megjelenését azonnal követheti a következő. 
A visszaszámlálás minden lépésénél kérdezze meg a felhasználót, hogy az adott órában szükség volt-e a visszaszámlálás fölfüggesztésére! 
A visszaszámlálás megjelenítését követően a program írja ki, hogy a visszaszámlálás kezdetétől hány óra telt el – a visszaszámlálás eredetileg tervezett hosszát a felfüggesztésekkel megnövelve!
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Hány órás visszaszámlálást tervezünk? 5
Visszaszámlálás: 5
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? n
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 5
-----
Hány órás visszaszámlálást tervezünk? 4
Visszaszámlálás: 4
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 3
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 2
Fel kell függeszteni a visszaszámlálást (i/n)? i
Visszaszámlálás: 1
Fel kell függeszteni a visszaszámlálást (i/n)? n
A rakéta a visszaszámlálást követően ennyi órával indult: 7
'''

kiloves = int(input("Hány órás visszaszámlását tervezünk?"))
i = kiloves
while i >= 1:
    fuggesztes = input("Fel kell függeszteni a visszaszámlálást (i/n) ?")
    if fuggesztes == 'n':
        print(f"Visszaszámlálás : {i}")
    elif fuggesztes == 'i':
        print(f"Visszaszámlálás:{i}")
    i -= 1
    if fuggesztes == 'i':
        kiloves += 1
print(f"A rakéta a visszaszámlálástkövetően ennyi órával indult: {kiloves}")


