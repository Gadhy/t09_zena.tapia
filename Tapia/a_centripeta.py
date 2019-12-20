import os
import libreria

velocidad=int(os.sys.argv[1])
radio=int(os.sys.argv[2])
b= libreria.aceleracion_centripeta(velocidad, radio)
print(b)
