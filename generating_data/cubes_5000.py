# 25/02/2023 - Lucas Garzuze Cordeiro

# Fazer um gráfico que mostre os 5000 primeiros números ao cubo

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Define o título do gráfico e o nome dos eixos x e y

ax.set_title("Números ao cubo", fontsize=20)
ax.set_ylabel("Número elevado ao cubo", fontsize=10)
ax.set_xlabel("Número", fontsize=10)

# Define o alcance dos eixos x e y

ax.axis([0, 5001, 0, 125000000000])

plt.show()