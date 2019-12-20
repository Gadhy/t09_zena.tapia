import os
import libreria

coeficiente_de_roce=int(os.sys.argv[1])
fuerza_normal=float(os.sys.argv[2])
b= libreria.fuerza_friccion(coeficiente_de_roce, fuerza_normal)
print(b)
