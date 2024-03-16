import numpy as np
import matplotlib.pyplot as plt


# Функция для определения возможности закрашивания ячейки
def can_fill_cell(cell, filled_cells, width, height):
    # Проверка, находится ли ячейка внутри области
    if cell[0] < 0 or cell[0] >= width or cell[1] < 0 or cell[1] >= height:
        return False

    # Проверка, закрашена ли ячейка
    if filled_cells[cell[0], cell[1]]:
        return False

    # Проверка, закрашены ли соседние ячейки
    for neighbor in [(cell[0] + 1, cell[1]), (cell[0] - 1, cell[1]), (cell[0], cell[1] + 1), (cell[0], cell[1] - 1)]:
        if neighbor[0] < 0 or neighbor[0] >= width or neighbor[1] < 0 or neighbor[1] >= height:
            continue
        if filled_cells[neighbor[0], neighbor[1]]:
            return False

    return True


# Функция для закрашивания ячейки
def fill_cell(cell, filled_cells, width, height):
    filled_cells[cell[0], cell[1]] = True

    # Закрашивание соседних ячеек
    for neighbor in [(cell[0] + 1, cell[1]), (cell[0] - 1, cell[1]), (cell[0], cell[1] + 1), (cell[0], cell[1] - 1)]:
        if can_fill_cell(neighbor, filled_cells, width, height):
            fill_cell(neighbor, filled_cells, width, height)


# Функция для поиска траектории инструмента
def find_trajectory(area, line_width):
    # Преобразование области в растровое изображение
    width = area.shape[0]
    height = area.shape[1]
    filled_cells = np.zeros((width, height), dtype=bool)

    # Поиск стартовой точки
    start_cell = None
    for i in range(width):
        for j in range(height):
            if area[i, j]:
                start_cell = (i, j)
                break
        if start_cell is not None:
            break

    # Закрашивание области
    fill_cell(start_cell, filled_cells, width, height)

    # Построение траектории
    trajectory = []
    for i in range(width):
        for j in range(height):
            if filled_cells[i, j]:
                trajectory.append((i, j))

    return trajectory


# Отрисовка области и траектории
def plot_area_and_trajectory(area, trajectory):
    plt.imshow(area, cmap='gray')

    for point in trajectory:
        plt.plot(point[0], point[1], 'ro')

    plt.show()


# Пример использования
area = np.array([[0, 1, 1, 1, 1],
                [0, 1, 1, 1, 1],
                [1, 1, 1, 0, 0],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 1, 1]])

# Ширина линии
line_width = 2

trajectory = find_trajectory(area, line_width)

plot_area_and_trajectory(area, trajectory)
