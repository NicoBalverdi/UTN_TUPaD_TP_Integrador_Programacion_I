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