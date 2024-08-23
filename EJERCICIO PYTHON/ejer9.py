
def areaCuadrado(lado:float)->float:
    return lado * lado

import math

def areaCirculo(radio: float) -> float:
    return math.pi * radio ** 2


def areaTriangulo(base:float, altura:float)->float:
    return base*altura/2

areaC = areaCuadrado(5.8)

areaCir = areaCirculo(3.8)

areaTri = areaTriangulo(5.3, 8.5)

print(f"El area del cuadrado con 5.8 es {areaC} ")

print(f"El area del circulo con radio 3.8 es {areaTri} ")

print(f"El area del triangulo con base 5.3 y altura 8.5 es {areaTri} ")


def operaciones():
    x=5
    y=8
opera = operaciones()
print(opera)
