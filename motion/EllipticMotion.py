import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation

class EllipticMotion:
    def __init__(self, major_axis=1.0, minor_axis=0.5, velocity=1.0):
        self.a = major_axis      # Большая полуось
        self.b = minor_axis      # Малая полуось
        self.velocity = velocity # Линейная скорость
    
    def get_position(self, time):
        omega = self.velocity / self.a     # Угловая скорость (определена по отношению к большой полуоси)
        x = self.a * np.cos(omega * time)  # Координата X по эллипсу
        y = self.b * np.sin(omega * time)  # Координата Y по эллипсу
        return x, y
    
    def calculate_centripetal_acceleration(self):
        omega = self.velocity / self.a
        return omega**2 * self.a           # Среднее центростремительное ускорение, учитывая большую полуось
    
    def calculate_period(self):
        return 2 * np.pi * self.a / self.velocity  # Период обращения вокруг эллипса
    
    def calculate_frequency(self):
        return 1 / self.calculate_period()          # Частота обращения


# Основной объект моделирования
motion = EllipticMotion()

# Окно и фигура
fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.25)

# История точек траектории
history_points = []



# Эллиптическая траектория
ellipse_trajectory, = ax.plot([], [], color='blue', lw=2, label='Эллиптическая траектория')

# Текущая позиция
position_marker, = ax.plot([], [], marker='o', markersize=10, color='green', label='Текущее положение')

# Центростремительное ускорение
accel_vector, = ax.plot([], [], color='red', linewidth=2, label='Вектор ускорения')

# Оси и сетка
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')  # Равномерное соотношение сторон
ax.grid(True, color='gray', linestyle='--', alpha=0.3)
ax.legend()

# Ползунки
ax_a = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_b = plt.axes([0.25, 0.10, 0.65, 0.03])
ax_v = plt.axes([0.25, 0.05, 0.65, 0.03])

major_axis_slider = Slider(ax_a, 'Большая полуось (м)', 0.1, 2.0, valinit=1.0)
minor_axis_slider = Slider(ax_b, 'Малая полуось (м)', 0.1, 2.0, valinit=0.5)
velocity_slider = Slider(ax_v, 'Скорость (м/с)', 0.1, 5.0, valinit=1.0)

# Обновляем график при изменении параметров
def update(val):
    global history_points
    motion.a = major_axis_slider.val
    motion.b = minor_axis_slider.val
    motion.velocity = velocity_slider.val
    
    # Очищаем историю точек
    history_points.clear()
    ellipse_trajectory.set_data([], [])
    
    # Пересчитываем траекторию эллипса
    theta = np.linspace(0, 2*np.pi, 100)
    x_ellipse = motion.a * np.cos(theta)
    y_ellipse = motion.b * np.sin(theta)
    ellipse_trajectory.set_data(x_ellipse, y_ellipse)
    
    # Текущая позиция
    current_x, current_y = motion.get_position(0)
    position_marker.set_data([current_x], [current_y])
    
    # Центростремительное ускорение
    acceleration = motion.calculate_centripetal_acceleration()
    center_x = 0
    center_y = 0
    vector_length = acceleration * 0.1
    accel_vector.set_data([current_x, center_x], [current_y, center_y])
    
    # Обновляем заголовок
    period = motion.calculate_period()
    frequency = motion.calculate_frequency()
    ax.set_title(f'Эллиптическое движение\nБольшая полуось: {motion.a:.2f} м, Малая полуось: {motion.b:.2f} м,\n'
                 f'Скорость: {motion.velocity:.2f} м/с\n'
                 f'Центростремительное ускорение: {acceleration:.2f} м/с²\n'
                 f'Период: {period:.2f} с, Частота: {frequency:.2f} Гц')
    
    fig.canvas.draw_idle()

# Регистрируем обработчики для ползунков
major_axis_slider.on_changed(update)
minor_axis_slider.on_changed(update)
velocity_slider.on_changed(update)

# Анимация
def animate(i):
    global history_points
    time = i * 0.1
    x, y = motion.get_position(time)
    
    # Добавляем текущую точку в историю
    history_points.append((x, y))
    
    # Преобразуем историю в массивы
    if len(history_points) > 0:
        xs, ys = zip(*history_points)
        ellipse_trajectory.set_data(xs, ys)
    
    # Текущая позиция
    position_marker.set_data([x], [y])
    
    # Центростремительное ускорение
    acceleration = motion.calculate_centripetal_acceleration()
    center_x = 0
    center_y = 0
    vector_length = acceleration * 0.1
    accel_vector.set_data([x, center_x], [y, center_y])
    
    return position_marker, accel_vector, ellipse_trajectory

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)

# Первоначальная визуализация
update(None)

plt.show()