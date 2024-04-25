def ordenar_fichas(fichas):
    # Contar la frecuencia de cada color
    frecuencia = {'rojo': 0, 'verde': 0, 'azul': 0}
    for ficha in fichas:
        if ficha == 'rojo':
            frecuencia['rojo'] += 1
        elif ficha == 'verde':
            frecuencia['verde'] += 1
        elif ficha == 'azul':
            frecuencia['azul'] += 1

    # Generar la secuencia ordenada de fichas
    orden = []
    for color, cantidad in frecuencia.items():
        orden.extend([color] * cantidad)

    return orden

# Pedir al usuario que ingrese las fichas
fichas = input("Ingrese las fichas separadas por espacios (rojo, verde, azul): ").split()

# Verificar si las fichas son válidas
colores_validos = {'rojo', 'verde', 'azul'}
if not all(ficha in colores_validos for ficha in fichas):
    print("Error: Las fichas ingresadas no son válidas. Por favor, ingrese solo 'rojo', 'verde' o 'azul'.")
else:
    # Ordenar las fichas
    orden = ordenar_fichas(fichas)
    print("Orden original de las fichas:", fichas)
    print("Fichas ordenadas:", orden)
