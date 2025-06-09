# Trabajo práctico integrador - Programación I - TUPaD
# Profesor: Sebastián Bruselario
# Tutor: Verónica Carbonari
# Alumnos: Juan Pablo Martinez, Nicolas Leonel Balverdi
# Comisión 25

# Funciones

def insertar(arbol, valor):
    if arbol == []:
        return [valor, [], []]
    if valor < arbol[0]:
        arbol[1] = insertar(arbol[1], valor)
    elif valor > arbol[0]:
        arbol[2] = insertar(arbol[2], valor)
    return arbol

def crear_arbol():
    arbol = []
    continuar = 1
    while continuar == 1:
        valor = int(input("Ingrese un código: "))
        if valor >= 0:
            arbol = insertar(arbol, valor)
        else:
            print("No se permiten códigos negativos.")
        continuar = int(input("Desea ingresar otro código? (1. Si / 2. No): "))
    return arbol

def mostrar_arbol(arbol, nivel=0):
    if arbol != []:
        mostrar_arbol(arbol[2], nivel + 1)
        print("    " * nivel + f"→ {arbol[0]}")
        mostrar_arbol(arbol[1], nivel + 1)

def encontrar_ruta(arbol, valor, ruta=[]):
    if arbol == []:
        return []

    ruta = ruta + [arbol[0]]

    if valor == arbol[0]:
        return ruta
    elif valor < arbol[0]:
        return encontrar_ruta(arbol[1], valor, ruta)
    else:
        return encontrar_ruta(arbol[2], valor, ruta)

def mostar_ruta(ruta = list):
    if ruta == []:
        return []
    else:
        for i in range(0, len(ruta)):
            if i == 0:
                print(ruta[i], end="")
            else:
                print(f" → {ruta[i]}", end="")

# Modificar un nodo

def minimo(arbol):
    actual = arbol
    while actual[1] != []:
        actual = actual[1]
    return actual[0]

def maximo(arbol):
    actual = arbol
    while actual[2] != []:
        actual = actual[2]
    return actual[0]

def modificar_nodo(arbol, valor_antiguo, nuevo_valor, padre=[], es_izquierdo=bool):
    if arbol == []:
        return []

    if valor_antiguo < arbol[0]:
        modificar_nodo(arbol[1], valor_antiguo, nuevo_valor, arbol, True)
    elif valor_antiguo > arbol[0]:
        modificar_nodo(arbol[2], valor_antiguo, nuevo_valor, arbol, False)
    else:
        # Validación con padre
        if padre != []:
            if es_izquierdo and nuevo_valor >= padre[0]:
                print(f"Un código a la izqierda de {padre[0]} no puede ser mayor. Si necesita cargarlo, utilice insertar.")
                return
            elif not es_izquierdo and nuevo_valor <= padre[0]:
                print(f"Un código a la derecha de {padre[0]} no puede ser menor. Si necesita cargarlo, utilice insertar.")
                return
        # Validación con hijos
        if arbol[1] != [] and nuevo_valor <= maximo(arbol[1]):
            print(f"{nuevo_valor} no puede ser menor o igual a {maximo(arbol[1])}, utilice la operación insertar si desea cargar {nuevo_valor} en el sistema")
            return
        if arbol[2] != [] and nuevo_valor >= minimo(arbol[2]):
            print(f"{nuevo_valor} no puede ser mayor o igual a {minimo(arbol[2])}, utilice la operación insertar si desea cargar {nuevo_valor} en el sistema.")
            return
        arbol[0] = nuevo_valor
        print(f"Se ha modificado correctamente {valor_antiguo} por {nuevo_valor}")
    return arbol

# Los 3 recorridos de los arboles binarios
def recorrer_preorden(arbol):
    if arbol == []:
        return []
    return [arbol[0]] + recorrer_preorden(arbol[1]) + recorrer_preorden(arbol[2])

def recorrer_inorden(arbol):
    if arbol == []:
        return []
    return recorrer_inorden(arbol[1]) + [arbol[0]] + recorrer_inorden(arbol[2])

def recorrer_postorden(arbol):
    if arbol == []:
        return []
    return recorrer_postorden(arbol[1]) + recorrer_postorden(arbol[2]) + [arbol[0]]

# Programa principal

print("== Trabajo Práctico Integrador ==")
print("A continuación debe cargar los códigos de sus productos al sistema")
arbol = crear_arbol()
print("Sus códigos han sido cargados correctamente en un árbol de busqueda binaria")
mostrar_arbol(arbol)

print("Desea realizar otra operación?")
print("1. Buscar un código")
print("2. Insertar un código")
print("3. Modificar un código")
print("4. Recorrer el sistema")
print("5. Salir")

operacion = int(input("Ingrese el número de la operación: "))

while operacion != 5 and (operacion > 0 and operacion < 6):
    if operacion == 1:
        codigo = int(input("Indique el código que esta buscando: "))
        ruta = encontrar_ruta(arbol, codigo)
        mostar_ruta(ruta)
        print()
    elif operacion == 2:
        codigo = int(input("Indique el código: "))
        if codigo > 0:
            insertar(arbol, codigo)
            mostrar_arbol(arbol)
        else:
            print("No se permiten códigos negativos.")
    elif operacion == 3:
        codigo = int(input("Ingrese el código que desea modificar: "))
        nuevoCodigo = int(input("Ingrese el nuevo código: "))
        modificar_nodo(arbol, codigo, nuevoCodigo)
        mostrar_arbol(arbol)
    elif operacion == 4:
        print("En qué orden desea visualizar el sistema?")
        print("1. Preorden / 2. Inorden / 3. Postorden")
        opcion = int(input("Ingrese el número de la opción: "))
        if opcion == 1:
            print(f"Recorrido en preorden: {recorrer_preorden(arbol)}")
        elif opcion == 2:
            print(f"Recorrido Inorden: {recorrer_inorden(arbol)}")
        elif opcion == 3:
            print(f"Recorrido Postorden: {recorrer_postorden(arbol)}")
        else:
            print("Opción incorrecta")
    else:
        print("Ha cerrado el sistema")
    
    print("Desea realizar otra operación?")
    print("1. Buscar un código")
    print("2. Insertar un código")
    print("3. Modificar un código")
    print("4. Recorrer el sistema")
    print("5. Salir")
    operacion = int(input("Ingrese el número de la operación: "))