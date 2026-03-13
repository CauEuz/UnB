import numpy as np
import matplotlib.pyplot as plt

n = 10
k_final = 20
L = 2.0
x = np.linspace(0.0, L, n + 1)
delta_x = L/n
delta_t = 0.2 * (delta_x ** 2)
print(delta_t)

#condicoes iniciais
temperaturas_iniciais = []
for distancia in x:
    temperatura = np.sin(distancia * np.pi / 2)
    temperaturas_iniciais.append(temperatura)
temp = np.array(temperaturas_iniciais)

#condicoes de contorno
temp[0] = 0
temp[n] = 0

temp_nova = np.copy(temp)

for k in range(1, k_final + 1):
    for i in range(1, n):
        temp_nova[i] = temp[i] + (delta_t / (delta_x ** 2)) * (temp[i + 1] - 2 * temp[i] + temp[i - 1])

    temp = np.copy(temp_nova)

t = k_final * delta_t

fig = plt.figure()
ax = fig.add_subplot()

fig.suptitle('t = %.3f' %t, fontsize = 18, fontweight = 'bold')
ax.set_ylabel('$T$', fontsize = 18)
ax.set_xlabel('$x$', fontsize = 18)

plt.plot(x, temp, '-r', lw = 4)
plt.savefig('figura3n10_final.png', dpi = 100)

plt.ylim(-0.05, 1.05)
plt.show()
