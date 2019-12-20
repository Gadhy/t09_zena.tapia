import os
import libreria

masa=int(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])
b= libreria.fuerza_resultante(masa,aceleracion)
print(b)
