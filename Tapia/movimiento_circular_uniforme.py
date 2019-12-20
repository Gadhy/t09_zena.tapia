import os
import libreria

velocidad_angular=int(os.sys.argv[1])
radio_de_la_curvatura_de_la_trayectoria=int(os.sys.argv[2])
b= libreria.movimiento_circular_uniforme(velocidad_angular,radio_de_la_curvatura_de_la_trayectoria)
print(b)
