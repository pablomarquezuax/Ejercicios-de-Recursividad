def busqueda_binaria_recursiva(lista, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    
    if inicio > fin:
        return -1  # Elemento no encontrado
    
    medio = (inicio + fin) // 2
    
    if lista[medio] == elemento:
        return medio
    elif lista[medio] < elemento:
        return busqueda_binaria_recursiva(lista, elemento, medio + 1, fin)
    else:
        return busqueda_binaria_recursiva(lista, elemento, inicio, medio - 1)

# Pedir al usuario que ingrese la lista y el elemento a buscar
lista = input("Ingrese la lista ordenada de números separados por espacios: ").split()
lista = [int(x) for x in lista]  # Convertir los elementos de la lista a enteros
elemento_buscar = int(input("Ingrese el elemento que desea buscar en la lista: "))

# Verificar si la lista está ordenada
if lista != sorted(lista):
    print("Error: La lista ingresada no está ordenada.")
else:
    # Realizar la búsqueda binaria recursiva
    indice = busqueda_binaria_recursiva(lista, elemento_buscar)
    if indice != -1:
        print(f"El elemento {elemento_buscar} se encuentra en el índice {indice}.")
    else:
        print(f"El elemento {elemento_buscar} no se encuentra en la lista.")
