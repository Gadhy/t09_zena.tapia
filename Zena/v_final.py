import os
import libreria

aceleracion=int(os.sys.argv[1])
v_inicial=int(os.sys.argv[2])
tiempo=int(os.sys.argv[3])
x= libreria.v_final(aceleracion,v_inicial,tiempo)
print(x)
