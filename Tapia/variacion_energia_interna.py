import os
import libreria

cantidad_de_calor=int(os.sys.argv[1])
trabajo=float(os.sys.argv[2])
b= libreria.variacion_energia_interna(cantidad_de_calor,trabajo)
print(b)
