import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation
import seaborn as sns  # Импортируем seaborn

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

# Применяем стиль Seaborn ко всей фигуре
sns.set(style="whitegrid")

# Окно и фигура
fig = plt.figure(figsize=(8, 10))  # увеличили высоту фигуры
ax = fig.add_subplot(111)
plt.subplots_adjust(bottom=0.25)

# Дополнительно настраиваем размещение элементов внутри окна
plt.subplots_adjust(top=0.85)            

# Открываем фигуру в полноэкранном режиме
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()

# История точек траектории
history_points = []

# Эллиптическая траектория
ellipse_trajectory, = ax.plot([], [], color=sns.color_palette()[0], lw=2, label='Эллиптическая траектория')

# Текущая позиция
position_marker, = ax.plot([], [], marker='o', markersize=10, color=sns.color_palette()[1], label='Текущее положение')

# Центростремительное ускорение
accel_vector, = ax.plot([], [], color=sns.color_palette()[2], linewidth=2, label='Вектор ускорения')

# Параметры графика
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')  
ax.grid(True, linestyle='--', alpha=0.3)
ax.legend()

# Ползунки
ax_major_axis = plt.axes([0.25, 0.15, 0.65, 0.03])  # Ползунок для большой полуоси
ax_minor_axis = plt.axes([0.25, 0.10, 0.65, 0.03])  # Ползунок для малой полуоси
ax_velocity = plt.axes([0.25, 0.05, 0.65, 0.03])    # Ползунок для скорости

slider_major_axis = Slider(ax_major_axis, 'Большая полуось (м)', 0.1, 2.0, valinit=1.0)
slider_minor_axis = Slider(ax_minor_axis, 'Малая полуось (м)', 0.1, 2.0, valinit=0.5)
slider_velocity = Slider(ax_velocity, 'Скорость (м/с)', 0.1, 1.0, valinit=1.0)

# Обновляем график при изменении параметров
def update(val):
    global history_points
    motion.a = slider_major_axis.val
    motion.b = slider_minor_axis.val
    motion.velocity = slider_velocity.val
    
    # Очищаем историю траектории при изменении параметров
    history_points.clear()
    ellipse_trajectory.set_data([], [])
    
    # Рассчитываем новую начальную позицию
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
    title_text = (
        f'Эллиптическое движение\n'
        f'Большая полуось: {motion.a:.2f} м, Малая полуось: {motion.b:.2f} м,\n'
        f'Скорость: {motion.velocity:.2f} м/с\n'
        f'Центростремительное ускорение: {acceleration:.2f} м/с²\n'
        f'Период: {period:.2f} с, Частота: {frequency:.2f} Гц'
    )
    ax.set_title(title_text)
    
    fig.canvas.draw_idle()

# Регистрируем обработчики для ползунков
slider_major_axis.on_changed(update)
slider_minor_axis.on_changed(update)
slider_velocity.on_changed(update)

# Функция обновления анимации
def animate(i):
    global history_points
    time = i * 0.1
    x, y = motion.get_position(time)
    
    # Добавляем текущую позицию в список истории
    history_points.append((x, y))
    
    # Отображаем историю движения
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

# Получаем расчетные характеристики модели
period = motion.calculate_period()
frequency = motion.calculate_frequency()
acceleration = motion.calculate_centripetal_acceleration()

# Настраиваем и выводим заголовок с уменьшенным размером шрифта
title_text = (
    f'Эллиптическое движение\n'
    f'Большая полуось: {motion.a:.2f} м, Малая полуось: {motion.b:.2f} м,\n'
    f'Скорость: {motion.velocity:.2f} м/с\n'
    f'Центростремительное ускорение: {acceleration:.2f} м/с²\n'
    f'Период: {period:.2f} с, Частота: {frequency:.2f} Гц'
)
ax.set_title(title_text)   

# Создаем анимацию
ani = animation.FuncAnimation(fig, animate, frames=1000, interval=50, blit=True)

# Первоначальная визуализация
update(None)

# Показываем окно
plt.show()