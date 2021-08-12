# def print_hi(name):
#     print(f'Hello {name}')

# if __name__ == '__main__':
#     print_hi('tomas')
# x: str = '10' #no define el tipo de dato
# print(id(x)) #posicion de memotia donde se almacena x de la literal 10, direccion de memoria 
# print(type(x))

# miNombre = 'Tomas Briones'
# for i in miNombre:
#     if i == " ":
#         print(i)
#     else:
#         print(i,end="")

# condicion = True
# i=0
# while i<3:
#     print('Ejecutando')
#     i+=1
# else:
#     print('fin ciclo while')

# nombres = []
# for i in range(0,2):
#     nombres.append(input('ingrese nombre: '))

# print(nombres)

# tupla = (13,1,8,3,2,5,8)
# lista = []
# for i in tupla:
#     if i<5:
#         lista.append(i)
# else:
#     print(lista)

diccionario = {
    'name':'tomas',
    'age':1,
    'genere':'male'
}
# print(diccionario['age'])
# print(diccionario.get('age'))

for termino, valor in diccionario.items(): #nos regresa los elementos separados por termino y valor .keys para terminos o .values para valores de cada termino
    print(termino, valor)

#si existe usaremos ('ide' in diccionario) con IN

#para agregar usamos diccionario['algo']= 'su valor'