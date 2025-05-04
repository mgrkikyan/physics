import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Настраиваем общий стиль
sns.set_style("whitegrid")  # Использование белого фона от Seaborn

# Вспомогательные функции для расчета физических величин
def centripetal_acceleration(v, r):
    return v**2 / r

def period(v, r):
    return 2 * np.pi * r / v

def frequency(v, r):
    return 1 / period(v, r)

# Диапазон данных
radiuses = np.linspace(0.1, 2.0, 100)  # диапазон радиусов
velocities = np.linspace(0.1, 5.0, 100)  # диапазон скоростей

# Создаем фигуру обычного размера
fig = plt.figure(figsize=(10, 6))

# График 1: Центростремительное ускорение vs Радиус
plt.subplot(2, 2, 1)
fixed_v = 1.0  # зафиксированная скорость
acc_values = centripetal_acceleration(fixed_v, radiuses)
plt.plot(radiuses, acc_values, color='blue')
plt.title('Центростремительное ускорение в зависимости от радиуса')
plt.xlabel('Радиус (м)')
plt.ylabel('Ускорение (м/с²)')

# График 2: Период обращения vs Радиус
plt.subplot(2, 2, 2)
fixed_v = 1.0  # та же зафиксированная скорость
period_values = period(fixed_v, radiuses)
plt.plot(radiuses, period_values, color='orange')
plt.title('Период обращения в зависимости от радиуса')
plt.xlabel('Радиус (м)')
plt.ylabel('Период (с)')

# График 3: Частота вращения vs Скорость
plt.subplot(2, 2, 3)
fixed_r = 1.0  # зафиксированный радиус
freq_values = frequency(velocities, fixed_r)
plt.plot(velocities, freq_values, color='green')
plt.title('Частота вращения в зависимости от скорости')
plt.xlabel('Скорость (м/с)')
plt.ylabel('Частота (Гц)')

# График 4: Кинетическая энергия vs Скорость
plt.subplot(2, 2, 4)
m = 1.0  # масса тела
kinetic_energy = 0.5 * m * velocities**2
plt.plot(velocities, kinetic_energy, color='purple')
plt.title('Кинетическая энергия в зависимости от скорости')
plt.xlabel('Скорость (м/с)')
plt.ylabel('Энергия (Дж)')

# Автоматически расставляем подписи и выравниваем расположение графиков
plt.tight_layout()

# Переключаемся в полноэкранный режим
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

# Показываем все графики
plt.show()