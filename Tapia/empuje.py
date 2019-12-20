import os
import libreria
densidad= int(os.sys.argv[1])
aceleracion_por_la_gravedad= int(os.sys.argv[2])
volumen_del_liquido_desplazado= int(os.sys.argv[3])
b= libreria.empuje(densidad,aceleracion_por_la_gravedad,volumen_del_liquido_desplazado)
print(b)
