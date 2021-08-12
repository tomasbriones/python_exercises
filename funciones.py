# def miFuncion(nombre,apellido):
#     print(f'hola {nombre} {apellido}')

# miFuncion('tomas','briones')

# def suma(a,b):
#     return a+b

# resultado = suma(5,3)
# print(resultado)

# def multi(*args):
#     multi = 1
#     for i in args:
#         multi *= i
#     return multi

# print(multi(2,3,4,5))

# def listarTerminos(**terminos): #podemos recibir argumentos
#     for llave, valor in terminos.items():
#         print(f'llave: {llave}, valor: {valor}')

# listarTerminos(name='tomas',lastname='briones')

# def imprimirNUmero(numero):
#     if numero == 1:
#         print(1)
#         return 1
#     elif numero < 1:
#         return ''
#     else:
#         print(numero)
#         return imprimirNUmero(numero-1)

#  def imprimir_numero_recursivo(numero):
#     if numero >= 1:
#         print(numero)
#         imprimir_numero_recursivo(numero-1)

# imprimir_numero_recursivo(5)       

# imprimirNUmero(5)
# imprimirNUmero(3)