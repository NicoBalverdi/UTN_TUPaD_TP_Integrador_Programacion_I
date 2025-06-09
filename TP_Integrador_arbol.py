# Trabajo práctico integrador - Programación I - TUPaD
# Profesor: Sebastián Bruselario
# Tutor: Verónica Carbonari
# Alumnos: Juan Pablo Martinez, Nicolas Leonel Balverdi
# Comisión 25

# Funciones

# Insertar un nodo
def insertar(arbol, valor): # Receibe un arbol y un valor para asignar a un nodo del arbol indicado
    if arbol == []: # Comprueba si el arbol o lista anidada esta vacia
        return [valor, [], []] # En caso de que la condición se cumpla, asigna el valor en la pos #0 y crea 2 listas anidadas
    if valor < arbol[0]: # Verificación del valor con respecto al nodo padre
        arbol[1] = insertar(arbol[1], valor) # Si es menor, se ubica en la lista anidada izquierda
    elif valor > arbol[0]: # Nueva verificación si la condición anterior no se cumple. Ahora es mayor?
        arbol[2] = insertar(arbol[2], valor) # Si es mayor, se coloca en la lista anidada derecha.
    return arbol # Retorna un árbol de búsqueda binaria con los nuevos valores insertados.

# Crear el árbol
def crear_arbol():
    arbol = [] # Inicia el árbol como una lista vacia
    continuar = 1 # Bandera para que el usuario controle el ingreso de inputs
    while continuar == 1: # Condición del ciclo donde utilizamos la bandera
        valor = input("Ingrese un código: ") # Registro del input del usuario
        if valor.isdigit(): # Verificación de tipo de input
            codigo = int(valor) # Casteo del string a entero
            arbol = insertar(arbol, codigo) # Se le pasan los argumentos a la función insertar
        else:
            print("No se permiten códigos negativos o letras, el sistema trabaja con inputs numéricos") # Si el input no es un dígito, se le informa al usuario del error
        continuar = int(input("Desea ingresar otro código? (1. Si / 2. No): ")) # Se le da la opción de continuar o terminar el ingreso de valores al usuario
    return arbol # Se devuelve el árbol resultante (ABB)

# Graficar los elementos en forma de árbol
def mostrar_arbol(arbol, nivel=0):
    if arbol != []: # Verificar que el árbol (lista o lista anidada) no este vacío.
        mostrar_arbol(arbol[2], nivel + 1) # Se llama recursivamente la función para la lista anidada con un valor mayor al nodo padre
        print("    " * nivel + f"→ {arbol[0]}") # Si no lo esta, el valor en la pos #0 se imprime en el centro, si es una lista anidada dependiendo del nivel tendrá una cantidad de espacios entre el nodo y la raíz
        mostrar_arbol(arbol[1], nivel + 1) # Se llama recursivamente la función para la lista anidada con un valor inferior al nodo padre

# Buscar y graficar la ruta a un valor
def encontrar_ruta(arbol, valor, ruta=[]):
    if arbol == []: # Si el arbol esta vacío
        return [] # Se retorna una lista vacía

    ruta = ruta + [arbol[0]] # Se agrega el valor de la pos #0 a la lista ruta

    if valor == arbol[0]: # Si el valor es igual a la pos #0 del árbol o la lista anidada entonces llegamos a destino
        return ruta # Retornamos la ruta
    elif valor < arbol[0]: # Sino verificamos si el valor menor a la pos #0 del árbol o lista anidada
        return encontrar_ruta(arbol[1], valor, ruta) # Se llama recursivamente a la función para buscar el valor en la lista anidada izquierda
    else: # Si el valor era mayor...
        return encontrar_ruta(arbol[2], valor, ruta) # Se llama recursivamente a la función para buscar el valor en la lista anidada derecha

def mostar_ruta(ruta = list):
    if ruta == []: # Si ruta esta vacía
        return [] # Se retorna una ruta vacía
    else: # Sino...
        for i in range(0, len(ruta)): # Se recorre una lista utilizando el ciclo for segun su longitud
            if i == 0: # Para la posición #0...
                print(ruta[i], end="") # Se imprime ruta pos # 0 y se indica que los siguientes prints se imprimiran al lado en lugar de realizar un salto de linea
            else: # Si no es la posición #0...
                print(f" → {ruta[i]}", end="") # Se imprime el próximo valor de la lista separandolo del primero con una flecha entre ambos para graficar la ruta recorrida

# Modificar un nodo

def minimo(arbol): # función que determinará el valor mínimo de una lista anidada en caso de modificar un nodo con hijos
    actual = arbol # Toma como arbol actual para trabajar el subarbol donde se encuentra el nodo a modifciar y su hijo/s
    while actual[1] != []: # Si el nodo padre tiene un hijo menor
        actual = actual[1] # El subarbol ahora se convierte en una lista donde se encuentra únicamente el valor del hijo menor
    return actual[0] # Se retorna el hijo menor

def maximo(arbol): # función que determinará el valor máximo de una lista anida en caso de modificar un nodo con hijos
    actual = arbol # Toma como arbol actual para trabajar el subarbol donde se encuentra el nodo a modifciar y su hijo/s
    while actual[2] != []: # Si el nodo padre tiene un hijo mayor
        actual = actual[2] # El subarbol ahora se convierte en una lista donde se encuentra únicamente el valor del hijo mayor
    return actual[0] # Se retorna el hijo mayor

def modificar_nodo(arbol, valor_antiguo, nuevo_valor, padre=[], es_izquierdo=bool): # La función principal para modificar un nodo
    if arbol == []: # Si el árbol o subarbol esta vacío...
        return [] # Se retorna una lista vacía

    if valor_antiguo < arbol[0]: # Por otra parte si el valor antiguo es menor al valor en la pos #0 del arbol/subarbol debemos buscar en el subarbol izquierdo
        modificar_nodo(arbol[1], valor_antiguo, nuevo_valor, arbol, True) # Llamamos recursivamente a la función para que explore el subarbol izquierdo pero esta vez agregamos el arbol padre y le indicamos que efectivamente el valor es del lado izquierdo
    elif valor_antiguo > arbol[0]: # Si el valor antiguo es mayor...
        modificar_nodo(arbol[2], valor_antiguo, nuevo_valor, arbol, False) # Se buscará en el subarbol derecho, tambien enviamos el arbol padre e indicamos que no es un valor del subarbol izquierdo
    else:
        # Validación con padre
        if padre != []:
            if es_izquierdo and nuevo_valor >= padre[0]: # Si es izquierdo y el nuevo valor es mayor o igual al valor del padre...
                print(f"Un código a la izqierda de {padre[0]} no puede ser mayor. Si necesita cargarlo, utilice insertar.") # Se le indica el problema al usuario
                return # El return termina el proceso
            elif not es_izquierdo and nuevo_valor <= padre[0]: # Si el valor es derecho y es menor o igual al padre...
                print(f"Un código a la derecha de {padre[0]} no puede ser menor. Si necesita cargarlo, utilice insertar.") # Se le indica el problema al usuario
                return # Se termina el proceso
        # Validación con hijos
        if arbol[1] != [] and nuevo_valor <= maximo(arbol[1]): # Si existe un subarbol izquierdo y el nuevo valor es menor o igual al hijo más grande de ese subarbol...
            print(f"{nuevo_valor} no puede ser menor o igual a {maximo(arbol[1])}, utilice la operación insertar si desea cargar {nuevo_valor} en el sistema") # Se explica el error
            return # Se termina el proceso
        if arbol[2] != [] and nuevo_valor >= minimo(arbol[2]): # Si existe un subarbol derecho y el nuevo valor es mayor o igual al hijo más chico de ese subarbol...
            print(f"{nuevo_valor} no puede ser mayor o igual a {minimo(arbol[2])}, utilice la operación insertar si desea cargar {nuevo_valor} en el sistema.") # Se notifica el error
            return # Se termina el proceso
        arbol[0] = nuevo_valor # Si se pasaron todas las verificaciones, se reemplaza el valor viejo por el nuevo
        print(f"Se ha modificado correctamente {valor_antiguo} por {nuevo_valor}") # Se notifica al usuario de que no hubo inconvenientes y el cambio fue efecutado
    return arbol # Se retorna el arbol

# Los 3 recorridos de los arboles binarios
def recorrer_preorden(arbol): # Se ingresa un arbol
    if arbol == []: # Si el arbol esta vacio...
        return [] # Se retorna una lista vacía
    return [arbol[0]] + recorrer_preorden(arbol[1]) + recorrer_preorden(arbol[2]) # Sino se retorna una lista con los elementos iniciando por la raíz luego a los arboles izquierdos listando primero sus padres luego los hijos izquierdos. Una vez recorridos los subarboles izquierdos se recorren los derechos, iniciando por sus padres, luego hijos izquierdos y finalmente los derechos  

def recorrer_inorden(arbol):
    if arbol == []:
        return [] # Si el árbol esta vacío, se retorna una lista vacía.
    return recorrer_inorden(arbol[1]) + [arbol[0]] + recorrer_inorden(arbol[2]) # Sino se recorre desde los nodos hoja izquierdos hacia sus padres y luego a sus hermanos derechos. Una vez se recorre el el subarbol izquierdo se lista la raiz, luego el subarbol derecho iniciando por las hojas izquierdas hacia sus padres y luego a los hermanos derechos

def recorrer_postorden(arbol): 
    if arbol == []:
        return [] # Si el arbol esta vacío, se retorna una lista vacía.
    return recorrer_postorden(arbol[1]) + recorrer_postorden(arbol[2]) + [arbol[0]] # Sino se recorre el subarbol izquierdo desde los nodos hoja izquierdos hacia sus hermanos derechos y luego al padre de ambos. Una vez recorrido el subarbol izquierdo se salta al nodo hoja izquierdo del subarbol derecho, luego se lista su hermano derecho y finalmente el padre. El proceso se repite hasta finalizar el recorrido del subarbol derecho donde finalmente se visita la raíz del árbol.

# Programa principal

print("== Trabajo Práctico Integrador ==")
print("A continuación debe cargar los códigos de sus productos al sistema")
arbol = crear_arbol()
print("Sus códigos han sido cargados correctamente en un árbol de búsqueda binaria")
mostrar_arbol(arbol)

print("Desea realizar otra operación?")
print("1. Buscar un código")
print("2. Insertar un código")
print("3. Modificar un código")
print("4. Recorrer el sistema")
print("5. Salir")

valor = input("Ingrese el número de la operación: ")
while not valor.isdigit():
    print("El sistema sólo permite inputs numéricos positivos.")
    valor = input("Ingrese el número de la operación: ")

operacion = int(valor)

while operacion != 5 and (operacion > 0 and operacion < 6):
    if operacion == 1:
        valor = input("Indique el código que esta buscando: ")
        if valor.isdigit():
            codigo = int(valor)
            ruta = encontrar_ruta(arbol, codigo)
            mostar_ruta(ruta)
            print()
        else:
            print("El sistema sólo trabaja con inputs numéricos positivos")
    elif operacion == 2:
        valor = input("Indique el código: ")
        if valor.isdigit():
            codigo = int(valor)
            if codigo > 0:
                insertar(arbol, codigo)
                mostrar_arbol(arbol)
        else:
            print("El sistema sólo trabaja con inputs numéricos positivos")
    elif operacion == 3:
        valor = input("Ingrese el código que desea modificar: ")
        valor2 = input("Ingrese el nuevo código: ")
        if valor.isdigit() and valor2.isdigit():
            codigo = int(valor)
            nuevoCodigo = int(valor2)
            modificar_nodo(arbol, codigo, nuevoCodigo)
            mostrar_arbol(arbol)
        else:
            print("El sistema sólo trabaja con inputs numéricos positivos")
    elif operacion == 4:
        print("En qué orden desea visualizar el sistema?")
        print("1. Preorden / 2. Inorden / 3. Postorden")
        valor = input("Ingrese el número de la opción: ")
        if valor.isdigit():
            opcion = int(valor)
            if opcion == 1:
                print(f"Recorrido en preorden: {recorrer_preorden(arbol)}")
            elif opcion == 2:
                print(f"Recorrido Inorden: {recorrer_inorden(arbol)}")
            elif opcion == 3:
                print(f"Recorrido Postorden: {recorrer_postorden(arbol)}")
        else:
            print("Opción incorrecta. El sistema sólo trabaja con inputs numéricos positivos")
    else:
        print("Ha cerrado el sistema")
    
    print("Desea realizar otra operación?")
    print("1. Buscar un código")
    print("2. Insertar un código")
    print("3. Modificar un código")
    print("4. Recorrer el sistema")
    print("5. Salir")
    
    valor = input("Ingrese el número de la operación: ")
    while not valor.isdigit():
        print("El sistema sólo permite inputs numéricos positivos.")
        valor = input("Ingrese el número de la operación: ")

    operacion = int(valor)