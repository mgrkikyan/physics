import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation

class CircularMotion:
    def __init__(self, radius=1.0, velocity=1.0):
        self.radius = radius
        self.velocity = velocity
    
    def calculate_centripetal_acceleration(self):
        return (self.velocity ** 2) / self.radius
    
    def get_position(self, time):
        omega = self.velocity / self.radius  # Угловая скорость
        x = self.radius * np.cos(omega * time)
        y = self.radius * np.sin(omega * time)
        return x, y
    
    def calculate_period(self):
        return 2 * np.pi * self.radius / self.velocity
    
    def calculate_frequency(self):
        return 1 / self.calculate_period()

# Основной объект моделирования
motion = CircularMotion()

# Рисуем основную фигуру
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
plt.subplots_adjust(bottom=0.25)

# История точек траектории
history_points = []

# Настройки внешнего вида
ax.set_facecolor('black')

# Линия траектории
trajectory, = ax.plot([], [], color='cyan', lw=2, label='Траектория')

# Текущая позиция
position_marker, = ax.plot([], [], marker='o', markersize=10, color='yellow', label='Текущее положение')

# Центростремительное ускорение
accel_vector, = ax.plot([], [], color='red', linewidth=2, label='Вектор ускорения')

# Параметры границ
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.grid(True, color='gray', linestyle='--', alpha=0.3)
ax.legend(facecolor='black', edgecolor='white', labelcolor='white')

# Ползунки
ax_radius = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_velocity = plt.axes([0.25, 0.10, 0.65, 0.03])

radius_slider = Slider(ax_radius, 'Радиус (м)', 0.1, 2.0, valinit=1.0)
velocity_slider = Slider(ax_velocity, 'Скорость (м/с)', 0.1, 5.0, valinit=1.0)

# Обновляем график при изменении параметров
def update(val):
    global history_points
    motion.radius = radius_slider.val
    motion.velocity = velocity_slider.val
    
    # Чистим историю точек
    history_points.clear()
    trajectory.set_data([], [])
    
    # Обновляем позицию
    current_x, current_y = motion.get_position(0)
    position_marker.set_data([current_x], [current_y])
    
    # Центростремительное ускорение
    acceleration = motion.calculate_centripetal_acceleration()
    center_x = 0  # Центр окружности
    center_y = 0
    vector_length = acceleration * 0.1  # Длина вектора
    accel_vector.set_data([current_x, center_x], [current_y, center_y])
    
    # Обновляем заголовок
    period = motion.calculate_period()
    frequency = motion.calculate_frequency()
    ax.set_title(f'Круговое движение\nРадиус: {motion.radius:.2f} м, '
                 f'Скорость: {motion.velocity:.2f} м/с\n'
                 f'Центростремительное ускорение: {acceleration:.2f} м/с²\n'
                 f'Период: {period:.2f} с, Частота: {frequency:.2f} Гц')
    
    fig.canvas.draw_idle()

# Регистрируем обработчики для ползунков
radius_slider.on_changed(update)
velocity_slider.on_changed(update)

# Анимация
def animate(i):
    global history_points
    time = i * 0.1
    x, y = motion.get_position(time)
    
    # Добавляем текущую точку в историю
    history_points.append((x, y))
    
    # Преобразуем историю в NumPy-массивы для удобного присвоения
    if len(history_points) > 0:
        xs, ys = zip(*history_points)
        trajectory.set_data(xs, ys)
    
    # Текущая позиция
    position_marker.set_data([x], [y])
    
    # Центростремительное ускорение
    acceleration = motion.calculate_centripetal_acceleration()
    center_x = 0  # Центр окружности
    center_y = 0
    vector_length = acceleration * 0.1  # Длина вектора
    accel_vector.set_data([x, center_x], [y, center_y])
    
    return position_marker, accel_vector, trajectory

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Запускаем начальную визуализацию
update(None)

plt.show()