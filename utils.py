from functools import reduce
game = [[1,3], [1,4] , [2,4]]


max_heigt_each_x = lambda t1,t2 : t2[1] if t2[1] > t1[1] else t1[1]

def ordem(lista, f):
    return reduce(lambda x, y: x if f(x,y) else y ,lista)



def separar(lista):
    if not lista:
        return [],[]
    else:
        lst1, lst2 = separar(lista[1:])
        lst1 = [lista[0][0]] + lst1
        lst2 = [lista[0][1]] + lst2
        return lst1, lst2

def max_height_x(game):
    x_list, y_list= separar(game)
    heights = {}
    for x in x_list:
