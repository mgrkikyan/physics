import numpy as np
import matplotlib.pyplot as plt

# Параметры
a_max = 2.0
b_max = 1.0
v_value = 1.0

# Эллипс
a_value = 1.0
b_value = 0.5
theta = np.linspace(0, 2*np.pi, 100)
x_ellipsoid = a_value * np.cos(theta)
y_ellipsoid = b_value * np.sin(theta)

# Диапазоны значений
a_range = np.linspace(0.5, a_max, 50)

# Период и частота
periods = 2 * np.pi * a_range / v_value
frequencies = 1 / periods

# Центростремительное ускорение
accelerations = (v_value / a_range)**2 * a_range

# Создаем сетку из четырёх графиков
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Эллипс
axes[0, 0].plot(x_ellipsoid, y_ellipsoid, color='royalblue', lw=2)
axes[0, 0].scatter(a_value, 0, s=100, c='red', zorder=5)
axes[0, 0].scatter(-a_value, 0, s=100, c='red', zorder=5)
axes[0, 0].set_title('Эллипс', fontsize=14)
axes[0, 0].set_xlabel('X', fontsize=12)
axes[0, 0].set_ylabel('Y', fontsize=12)
axes[0, 0].axis('equal')
axes[0, 0].grid(True) # Добавляем сетку

# Период
axes[0, 1].plot(a_range, periods, color='forestgreen', lw=2)
axes[0, 1].set_title('Период', fontsize=14)
axes[0, 1].set_xlabel('Большая полуось (a)', fontsize=12)
axes[0, 1].set_ylabel('Период (с)', fontsize=12)
axes[0, 1].grid(True) # Добавляем сетку

# Центростремительное ускорение
axes[1, 0].plot(a_range, accelerations, color='darkorange', lw=2)
axes[1, 0].set_title('Центростремительное ускорение', fontsize=14)
axes[1, 0].set_xlabel('Большая полуось (a)', fontsize=12)
axes[1, 0].set_ylabel('Ускорение (м/с²)', fontsize=12)
axes[1, 0].grid(True) # Добавляем сетку

# Частота
axes[1, 1].plot(a_range, frequencies, color='indigo', lw=2)
axes[1, 1].set_title('Частота', fontsize=14)
axes[1, 1].set_xlabel('Большая полуось (a)', fontsize=12)
axes[1, 1].set_ylabel('Частота (Гц)', fontsize=12)
axes[1, 1].grid(True) # Добавляем сетку

# Общие настройки
plt.tight_layout()
plt.show()