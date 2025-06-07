import matplotlib.pyplot as plt
import numpy as np
from pulp import value

# Parâmetros do problema (copiados do seu código)
area_cimento = 0.25
area_argamassa = 0.20
pilha_cimento = 10
pilha_argamassa = 15
Tc = 2
Ta = 1
Ec = Tc + 1
Ea = Ta + 1
Cmax = 3 * valor_cim_max
Amax = 3 * valor_arg_max

# Restrição inferior mínima
x_min = int(np.ceil((Cmax * (Tc + Ec)) / pilha_cimento))
y_min = int(np.ceil((Amax * (Ta + Ea)) / pilha_argamassa))

# Faixas de valores para o gráfico
x_vals = np.arange(max(0, x_min - 2), x_min + 10)
y_vals = np.arange(max(0, y_min - 2), y_min + 10)
X, Y = np.meshgrid(x_vals, y_vals)

# Função objetivo Z = área_cimento * x + area_argamassa * y
Z = area_cimento * X + area_argamassa * Y

# Gráfico
plt.figure(figsize=(10, 7))
contours = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.clabel(contours, inline=True, fontsize=8)

# Restrições
plt.axvline(x_min, color='red', linestyle='--', label=f'Restrição cimento (x ≥ {x_min})')
plt.axhline(y_min, color='blue', linestyle='--', label=f'Restrição argamassa (y ≥ {y_min})')

# Solução ótima (resultado do solver PuLP)
x_opt = x.varValue
y_opt = y.varValue
area_opt = value(model.objective)
plt.plot(x_opt, y_opt, 'ro', label=f'Solução ótima ({x_opt}, {y_opt}) - Área: {area_opt:.2f} m²')

# Estética
plt.title('Modelo de Dimensionamento de Almoxarifado')
plt.xlabel('Pilhas de Cimento (x)')
plt.ylabel('Pilhas de Argamassa (y)')
plt.legend()
plt.grid(True)
plt.show()
