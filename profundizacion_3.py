# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura_1 = int(input('\nIngrese un valor de temperatura: '))
temperatura_2 = int(input('Ingrese otro valor de temperatura: '))
temperatura_3 = int(input('Ingrese un último valor de temperatura: '))

print('')

if temperatura_1 > temperatura_2 and temperatura_1 > temperatura_3:
    print(f'Temperatura 1 es la mayor y vale: {temperatura_1}')

    if temperatura_2 < temperatura_3:
        print(f'Temperatura 2 es la mínima y vale: {temperatura_2}')

    elif temperatura_3 < temperatura_2:
        print(f'Temperatura 3 es la mínima y vale: {temperatura_3}')
    else:
        print(f'Temperatura 2 y 3 son iguales y valen: {temperatura_2}')

elif temperatura_2 > temperatura_1 and temperatura_2 > temperatura_3:
    print(f'Temperatura 2 es la mayor y vale: {temperatura_2}')

    if temperatura_1 < temperatura_3:
        print(f'Temperatura 1 es la mínima y vale: {temperatura_1}')

    elif temperatura_3 < temperatura_1:
        print(f'Temperatura 3 es la mínima y vale: {temperatura_3}')

    else:
        print(f'Temperatura 1 y 3 son iguales y valen: {temperatura_1}')

elif temperatura_3 > temperatura_2 and temperatura_3 > temperatura_1:
    print(f'Temperatura 3 es la mayor y vale: {temperatura_3}')

    if temperatura_2 < temperatura_1:
        print(f'Temperatura 2 es la mínima y vale: {temperatura_2}')

    elif temperatura_1 < temperatura_2:
        print(f'Temperatura 1 es la mínima y vale: {temperatura_1}')

    else:
        print(f'Temperatura 1 y 2 son iguales y valen: {temperatura_1}')

else:
    if temperatura_1 == temperatura_2 and temperatura_1 > temperatura_3:
        print(f'Temperatura 1 y 2 son iguales y valen: {temperatura_1}')
        print(f'Temperatura 3 es la minima y vale: {temperatura_3}')

    elif temperatura_2 == temperatura_3 and temperatura_2 > temperatura_1:
        print(f'Temperatura 2 y 3 son iguales y valen: {temperatura_2}')
        print(f'Temperatura 1 es la minima y vale: {temperatura_1}')

    elif temperatura_1 == temperatura_3 and temperatura_1 > temperatura_2:
        print(f'Temperatura 1 y 3 son iguales y valen: {temperatura_1}')
        print(f'Temperatura 1 es la minima y vale: {temperatura_2}')
        
    else:
        print(f'Todas las temperaturas ingresadas son iguales: {temperatura_1}')

