word = input('Кто запретит нам писать буквы - ') + ' запретил букву '
alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
for j in alf:
    if word.count(j) > 0:
        print(word + j)
        while word.count(j)>=1:
            zapr = word.find(j) 
            word = word[:zapr] + word[zapr+1:]
