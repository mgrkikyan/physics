import numpy as np
import matplotlib.pyplot as plt

# Вспомогательная функция для расчётов
def centripetal_acceleration(v, r):
    return v**2 / r

def period(v, r):
    return 2 * np.pi * r / v

def frequency(v, r):
    return 1 / period(v, r)


# ... existing imports and functions ...

# Данные для графиков
radiuses = np.linspace(0.1, 2.0, 100)  # диапазон радиусов
velocities = np.linspace(0.1, 5.0, 100)  # диапазон скоростей

# Создаем фигуру с черным фоном
plt.figure(figsize=(10, 6), facecolor='black')

# График 1: Центростремительное ускорение vs Радиус
plt.subplot(2, 2, 1)
plt.gca().set_facecolor('black')  # Устанавливаем черный фон для осей
fixed_v = 1.0  # Зафиксированная скорость
acc_values = centripetal_acceleration(fixed_v, radiuses)
plt.plot(radiuses, acc_values, color='blue')
plt.title('Центростремительное ускорение в зависимости от радиуса', color='white')
plt.xlabel('Радиус (м)', color='white')
plt.ylabel('Ускорение (м/с²)', color='white')
plt.tick_params(axis='both', colors='white')  # Устанавливаем цвет меток осей
plt.grid(True, color='gray')  # Устанавливаем цвет сетки

# График 2: Период обращения vs Радиус
plt.subplot(2, 2, 2)
plt.gca().set_facecolor('black')  # Устанавливаем черный фон для осей
fixed_v = 1.0  # Та же зафиксированная скорость
period_values = period(fixed_v, radiuses)
plt.plot(radiuses, period_values, color='orange')
plt.title('Период обращения в зависимости от радиуса', color='white')
plt.xlabel('Радиус (м)', color='white')
plt.ylabel('Период (с)', color='white')
plt.tick_params(axis='both', colors='white')  # Устанавливаем цвет меток осей
plt.grid(True, color='gray')  # Устанавливаем цвет сетки

# График 3: Частота вращения vs Скорость
plt.subplot(2, 2, 3)
plt.gca().set_facecolor('black')  # Устанавливаем черный фон для осей
fixed_r = 1.0  # Зафиксированный радиус
freq_values = frequency(velocities, fixed_r)
plt.plot(velocities, freq_values, color='green')
plt.title('Частота вращения в зависимости от скорости', color='white')
plt.xlabel('Скорость (м/с)', color='white')
plt.ylabel('Частота (Гц)', color='white')
plt.tick_params(axis='both', colors='white')  # Устанавливаем цвет меток осей
plt.grid(True, color='gray')  # Устанавливаем цвет сетки

# График 4: Кинетическая энергия vs Скорость
plt.subplot(2, 2, 4)
plt.gca().set_facecolor('black')  # Устанавливаем черный фон для осей
m = 1.0  # масса тела
kinetic_energy = 0.5 * m * velocities**2
plt.plot(velocities, kinetic_energy, color='purple')
plt.title('Кинетическая энергия в зависимости от скорости', color='white')
plt.xlabel('Скорость (м/с)', color='white')
plt.ylabel('Энергия (Дж)', color='white')
plt.tick_params(axis='both', colors='white')  # Устанавливаем цвет меток осей
plt.grid(True, color='gray')  # Устанавливаем цвет сетки

# Автоматически расставляем подписи и выравниваем расположение графиков
plt.tight_layout()

# Показываем все графики
plt.show()