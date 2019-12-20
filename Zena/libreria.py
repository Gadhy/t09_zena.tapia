def sumar(a,b):
    sumar=a+b
    return sumar

def restar(a,b):
    restar=a-b
    return restar

def mayor(a,b):
    mayor= a>10 and b>10
    return mayor

def problemas(a,b,c):
    problema= a*(b**c+a)/b
    return problema

def elevar_al_cuadrado(a,b):
    cuadrados= a**2+b**2
    return cuadrados

def mayor2(a,b):
    if (a > b):
        return a
    else:
        return b

def menor(a,b):
    if (a < b):
        return a
    else:
        return b

def distancia(velocidad,tiempo):
    return velocidad*tiempo

def altura(tiempo):
    return 5*(tiempo**2)

def perimetro(l1,l2,l3):
    return l1+l2+l3

def area_circulo(pi,r):
    return pi*(r**2)

def area_trapecio(altura,base_mayor,base_menor):
    return ((base_mayor+base_menor)*altura)/2

def v_media(v_inicial,v_final):
    return (v_inicial-v_final)/2

def compras(zapatillas,polos,pantalon):
    return zapatillas+pantalon+polos

def v_final(v_inicial,aceleracion,tiempo):
    return v_inicial+(aceleracion*tiempo)

def fuerza(masa,aceleracion):
    return masa*aceleracion

def hallar_x(a,b,c):
    x=((a*2)+b**2)/c
    return x

def ejer(a,b,c,d):
    return ((a*d)-(c-b))/4

def combinacion (a,b,c,d):
    return (a+8)/3*(c**d)

def peso(masa,gravedad):
    return masa*gravedad

def area_triangulo(base,altura):
    return (base*altura)/2

def v_angular(frecuencia):
    return frecuencia*2

def igual(x,y):
    if (x == y):
        return x
    else:
        return y

def ejercicio4(x,y,z):
    return ((x/y)+5)**2

def presion(fuerza, area):
    return fuerza/area
