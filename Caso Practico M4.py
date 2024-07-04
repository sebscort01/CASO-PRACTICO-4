import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"E:\Maestria y Diplomados\DIPLOMADO PYTHON\Full info\Modulo 4 Temas avanzados de python 2\Caso practico\graficar.txt",encoding='UTF-8')
print(df.to_string())


df.plot()
plt.show()
 