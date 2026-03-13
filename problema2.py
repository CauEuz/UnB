import numpy as np
import matplotlib.pyplot as plt

n = 10
k_final = 91
L = 1.0
x = np.linspace(0.0, L, n + 1)
delta_x = L/n
delta_t = 0.0055

#condicoes iniciais
temp = np.zeros(n + 1, float)
#condicoes de contorno
temp[0] = 1.0
temp[n] = 0.0

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
plt.savefig('figura2instavel_final', dpi = 100)

plt.show()
