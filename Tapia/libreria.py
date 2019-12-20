def notas(n1,n2,n3):
    suma=(n1+n2+n3)/3
    if suma>=10.5 and suma<=20:
        print("aprobado")
    if suma<=10.5:
        print("desaprobado")
    return suma
    print(suma)

def suma(x,y):
    suma= x+y
    return suma
    print(suma)

def multiplicacion(f,g):
    multiplicacion= f*g
    print("el resultado es:")
    return multiplicacion

def resta(p,o):
    resta= p-o
    if resta<10:
        print("resta valida")
    if resta>10:
        print("resta invalida")
    return resta

def fuerza_resultante(masa,aceleracion):
    fuerza_resultante= masa*aceleracion
    print("fuerza resultante:")
    return fuerza_resultante

def area_del_trapecio(base_mayor,base_menor,altura):
    area= (base_mayor + base_menor)/2 * altura
    print("el area es:")
    return area

def area_triangulo(base,altura):
    area= (base*altura)/2
    print("el area es:")
    return area

def promedio(n1,n2,n3):
    promedio= (n1+n2+n3)/3
    print("el promedio del alumno es:")
    return promedio

def movimiento_circular_uniforme(velocidad_angular,radio_de_la_curvatura_de_la_trayectoria):
    velocidad= velocidad_angular*radio_de_la_curvatura_de_la_trayectoria
    print("la velocidad es:")
    return velocidad

def periodo(frecuencia):
    periodo= 1/frecuencia
    print("el periodo es:")
    return periodo

def v_angular(frecuencia):
    velocidad_angular= 2*frecuencia
    print("la velocidad angular es:")
    return velocidad_angular

def fuerza_resultante(masa,aceleracion):
    fuerza_resultante= masa*aceleracion
    print("la fuerza resultante es")
    return fuerza_resultante

def peso(masa,gravedad):
    peso= masa*gravedad
    print("el peso es:")
    return peso

def fuerza_elastica(constante_elastica_del_resorte, deformacion_del_resorte):
    fuerza_elastica= constante_elastica_del_resorte*deformacion_del_resorte
    print("la fuerza elastica es:")
    return fuerza_elastica

def energia_potencial_elastica(constante_elastica_del_resorte, deformacion_del_resorte):
    energia_potencial_elastica= (1/2*constante_elastica_del_resorte)*deformacion_del_resorte**2
    print("la energia potencial elastica es:")
    return energia_potencial_elastica

def cantidad_movimiento(masa, velocidad):
    cantidad_de_movimiento= masa*velocidad
    print("la cantidad de movimiento es:")
    return cantidad_de_movimiento

def variacion_energia_interna(cantidad_de_calor, trabajo):
    variacion_de_energia_interna= cantidad_de_calor*trabajo
    print("variacion de energia interna es:")
    return variacion_de_energia_interna

def aceleracion_centripeta(velocidad, radio):
    aceleracion_centripeta= (velocidad**2)/radio
    print("la aceleracion centripeta es:")
    return aceleracion_centripeta

def presion(fuerza, area):
    presion= fuerza/area
    print("la presion es:")
    return presion

def cantidad_calor(masa, calor_latente):
    cantidad_de_calor= masa*calor_latente
    print("la cantidad de calor es:")
    return cantidad_de_calor

def empuje(densidad, aceleracion_por_la_gravedad, volumen_del_liquido_desplazado):
    empuje= (densidad*aceleracion_por_la_gravedad)*volumen_del_liquido_desplazado
    print("el empuje es:")
    return empuje

def fuerza_friccion(coeficiente_de_roce, fuerza_normal):
    fuerza_de_friccion= coeficiente_de_roce*fuerza_normal
    print("fuerza de friccion:")
    return fuerza_de_friccion

def impulso(fuerza, variacion_del_tiempo):
    impulso= fuerza*variacion_del_tiempo
    print("el impulso es:")
    return impulso

def area_rombo(diagonal_mayor, diagonal_menor):
    area= (diagonal_mayor*diagonal_menor)/2
    verificador_area_rombo= (area>45.8)
    print("el area es mayor a 45.8?", verificador_area_rombo)
    return area

def ejercicio(x,y,z):
    ejercicio=(x*y)+2-z**y
    print("resultado:")
    return ejercicio
