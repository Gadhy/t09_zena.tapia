import os
import libreria

base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
altura=int(os.sys.argv[3])
b= libreria.area_del_trapecio(base_mayor,base_menor,altura)
print(b)
