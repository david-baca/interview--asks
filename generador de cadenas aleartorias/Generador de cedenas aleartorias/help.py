import random

def generate (longitud, cantidad):
    # Definimos el conjunto de caracteres permitidos (sin la letra ñ)
    caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789'
    cadenas_generadas = set()
    while len(cadenas_generadas) < cantidad:
        # Generamos una cadena aleatoria
        cadena = ''.join(random.choice(caracteres) for _ in range(longitud))
        cadenas_generadas.add(cadena)
    return list(cadenas_generadas)

def generar_cadenas_unicas(longitud, cantidad):
    
    # Calculamos cuántas combinaciones posibles hay 35 exponencial n
    posibles_combinaciones = 35 ** longitud
    # Si la cantidad solicitada es mayor que las combinaciones posibles, mostramos un mensaje y devolvemos None
    if cantidad >= posibles_combinaciones:
        print(f"No es posible generar {cantidad} cadenas únicas de longitud {longitud}. Solo hay {posibles_combinaciones} combinaciones posibles agregue una longitud más grande.")
        x = generate(longitud, posibles_combinaciones)
        y = generate(longitud+1, cantidad-(posibles_combinaciones))
        for i, cadena in enumerate(x, start=1):
            print(f"{i}.- {cadena}", end=" ")
        for i, cadena in enumerate(y, start=1):
            print(f"{i+(posibles_combinaciones)}.- {cadena}", end=" ")
        return None
    var = generate(longitud, cantidad)
    for i, cadena in enumerate(var, start=1):
            print(f"{i}.- {cadena}", end=" ")
    return None
    
# Ejemplo de uso:
longitud = int(input("Introduce la longitud de las cadenas a generar: "))
cantidad = int(input("Introduce la cantidad de cadenas a generar: "))
resultados = generar_cadenas_unicas(longitud, cantidad)

