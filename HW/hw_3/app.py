from helper import task, count_family_numbers,list_to_set
#
task(3.1)
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2])

print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])


task(3.2)
list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
sum_of_el = [summ for summ in list_1 if isinstance(summ,int)]
print(sum(sum_of_el))


sum_of_el2= sum(summ for summ in list_1 if isinstance(summ,int))
print(sum_of_el2)

task(3.2)
el_a = [el for el in list_1 if isinstance(el,str) and 'a' in el]
print(el_a)

task(3.3)
anim =['cat', 'dog', 'horse', 'cow']
anim_tuple = tuple(anim)
print(anim_tuple)

task(3.4)

family_1 = input("Введите членов первой семьи, разделяя их запятой: ")
family_2 = input("Введите членов второй семьи, разделяя их запятой: ")

print(count_family_numbers(family_1,family_2))

task(3.5)
my_film ={
    "title":"Тёмный рыцарь:Возрождение легенды",
    "director":"Christopher Nolan",
    "year":"2012",
    "budget":"250 000 000",
    "main_actor":"Christian Bale",
    "slogan":"Why so serious?"
}
for item in my_film.items():
    print(item)
    # key,value = item
    # print(item)
    # print(key)

    # print(key)
    # print(value)

task(3.6)
my_dictionary = {'num1': 375,
                 'num2': 567,
                 'num3': -37,
                 'num4': 21}
summ = 0
for summa in my_dictionary.values():
    summ=summ+summa

print(summ)

task(3.7)
original_list = [1, 2, 3, 4, 5, 3, 2, 1]
unique_list = list(set(original_list))
print(unique_list)

task(3.7)
print(list_to_set(original_list))

task(3.8)
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

common = set1&set2
print(common)

individual = set1.symmetric_difference(set2)
print(individual)
individual2 = ((set1|set2)-set1.intersection(set2))
print(individual2)
individual3 = ((set1|set2)-(set1&set2))
print(individual3)

res1 = set1.issubset(set2)
print(res1)
res2 = set2.issubset(set1)
print(res2)

sup1 = set1.issuperset(set2)
print(sup1)
sup2 =set2.issuperset(set1)
print(sup2)
