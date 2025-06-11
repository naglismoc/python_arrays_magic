#             0  1  2  3  4  5  6  7  8  9 INDEKSAI
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

###################### PIRMAS PARAMETRAS INCLUSIVE, JI IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO######################
# print(my_numbers[pradzia:galas:zingsnis])
print(my_numbers)#atspausdiname viska
print(my_numbers[6])#vienas
print(my_numbers[0:4])#nuo iki
print(my_numbers[4:8])
print(my_numbers[7:])#nuo iki galo
print(my_numbers[:4])#nuo pradzios iki nurodytos pozicijos (exclusive, jos neima. IKI jos)
print(my_numbers[-2])#antra pozicija nuo galo
print(my_numbers[-5:])#nuo 5 pozicijos nuo galo iki pat galo
print(my_numbers[:-5])#nuo pradzios iki 5 pozicijos nuo galo
print(my_numbers[2:-5])# nuo 2 pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2])#imame nuo 6 nuo galo iki 2 nuo galo
print(my_numbers[-8:4])#teoriskai veikia, neapsikraukis =D
print(my_numbers[:])#paima viska nuo pradzios iki galo, lygiai taip pat, kaip ir neirasius nieko
print(my_numbers[::2])#visa imtis, kas antras elementas
print(my_numbers[::3])#visa imtis, kas 3cias elementas
print(my_numbers[1::2])#visa imtis nuo 1o indekso iki galo, kas antras elementas
print(my_numbers[3:7:2])#nuo 3 indekso inclusive iki 7 exclusive kas antras elementas
print(my_numbers[2:-2:2])#paimu viska be pirmu dvieju IR paskutiniu dvieju kas antra
print(my_numbers[::-1])#visi elementai, bet nuo galo.
print(my_numbers[::-2])# visa imtis, kas antras elementas BET nuo GALO




empty_list = []
print(empty_list)
empty_list.append(20)
print(empty_list)
empty_list.extend([14,20,4]) #extend naudojame lauztinius skliaustus [] ir juose isvardinam reiksmes kurias norime
print(empty_list)
print(empty_list.count(20)) # suranda KIEK yra ieskomos reiksmes vienetu
empty_list.remove(14) #panaikina pirma reiskme kuri yra ieskoma reiksme
print(empty_list)
popped_element = empty_list.pop()
print(empty_list)
print(popped_element)

students = ['Ingrida','Anzelika','Arnas','Mangirdas','Paulius','Julija','Neringa','Raimundas','Rolandas','Dalia',
            'Edvinas','Vytautas']

print(students)
students.sort()
print(students)
students.sort(reverse=True)
print(students)

copy = my_numbers.copy()
copy.remove(7)
print(copy)
print(my_numbers)


arr_2d = [
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [4,5,6]
]
print(arr_2d)
print(arr_2d[2])
print(arr_2d[2][0])

sum = 0
count = 0

for vidinis_masyvukas in arr_2d:
    for num in vidinis_masyvukas:
        sum += num
        count += 1

print(sum)
print(count)
print(sum / count)

for x in range(10): #0, 1, 2, 3, 4, 5...
    for y in range(10):
        print("x="+str(x) +"+y="+str(y), end=" ")
    print()

students = [
    ["jonas","jonauskas",24],
    ["petras","petrauskas",26],
    ["Viktoras","jakubauskas",38],
    ["Juozapas","sabonis",42],
]

for student in students:
    for info in student:
        print(info, end=", ")
    print()
