import random
import itertools

def Iteraciones(longitud, cantidad):
    #calculamos las posibles combinaciones de letras donde logitud x longitud nos dara las posibles combianaciones 
    base = 35 # se tienen 35 posible acaracteres
    exponenteResult = base ** longitud
    #una vez que sabemos la cantidad de combuinaciones generamos las combinacionesposibles mientras no sea mayor que su longitud
    if exponenteResult >= longitud :
        caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
        #generar una lista con las posibles cadenas
        #retornar solo la cantudad {$cantidad} pero aleartoriamente de los reultados encontrados
    #en caso de no cumplir la condicion decirla al usuario que no solo son posibles generar {$exponeteReult} y no {$cantidad}
    # | > decirle que agrege mas datos a longtud

longitud = int(input("introduice la longitud de las cadenas a generar"))
cantidad = int(input("introduice la cantidad de cadenas a generar"))
var = Iteraciones(longitud, cantidad)

