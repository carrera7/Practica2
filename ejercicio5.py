cadena = input(" ingrese el texto ")
cadena = cadena.lower()
palabra = input(" ingrese alpasaba a buscar")
cadena_busqueda = cadena.split(' ')
resultado = 0
for i in cadena_busqueda :
    if palabra  == i:
        resultado = resultado + 1 
print(f"el texto fue: {cadena}")
print(f" la palabra a buscar fue : {palabra}")
print(f" se encontraron : {resultado}")