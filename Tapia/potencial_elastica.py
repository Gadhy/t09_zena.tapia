import os
import libreria

constante_elastica_del_resorte=float(os.sys.argv[1])
deformacion_del_resorte=float(os.sys.argv[2])
b= libreria.energia_potencial_elastica(constante_elastica_del_resorte,deformacion_del_resorte)
print(b)
