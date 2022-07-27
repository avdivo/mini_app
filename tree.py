import random
import simple_draw as sd   # pip install simple_draw


sd.resolution = (1200, 700)

def draw_bunches(start_point, angle, length):
    if length < 1:
        return
    # Рисуем ветку
    thickness = int(length // 7 + 1) # толщина ветки зависит от длины
    color = sd.COLOR_DARK_ORANGE
    if  thickness < 4:
        color = sd.COLOR_DARK_GREEN
    if  thickness < 2:
        color = sd.COLOR_GREEN

    vector_1 = sd.get_vector(start_point=start_point, angle=angle, length=length, width=thickness)
    vector_1.draw(color)

    # Левая ветка
    length_new = length * random.uniform(0.6, 0.9) # Исхдящяя ветка 60%-90% длины
    angle_new = angle + 30 * random.uniform(0.6, 1) # Угол наклона ветки 18%-30%
    draw_bunches(start_point=vector_1.end_point, angle=angle_new, length=length_new)

    # Правая ветка
    length_new = length * random.uniform(0.6, 0.9) # Исхдящяя ветка 60%-90% длины
    angle_new = angle - 30 * random.uniform(0.6, 1) # Угол наклона ветки 18%-30%
    draw_bunches(start_point=vector_1.end_point, angle=angle_new, length=length_new) 

    # Прямая ветка
    # length_new = length * 0.75 # Исхдящяя ветка 75% длины
    # angle_new = angle * 0.9 + angle * random.uniform(0, 0.2) # Угол наклона ветки 18%-30%
    # draw_bunches(start_point=vector_1.end_point, angle=angle_new, length=length_new)

root_point = sd.get_point(350, 30)
draw_bunches(start_point=root_point, angle=90, length=100)

root_point = sd.get_point(900, 30)
draw_bunches(start_point=root_point, angle=90, length=90)

sd.pause()


