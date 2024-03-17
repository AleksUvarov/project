# project

Объяснение:

Функция can_fill_cell проверяет, можно ли закрасить ячейку.
Функция fill_cell закрашивает ячейку и ее соседей.
Функция find_trajectory находит траекторию инструмента.
Функция plot_area_and_trajectory отрисовывает область и траекторию.

Ограничения:

Эта программа работает только для двоичных изображений.
Эта программа не учитывает форму области.
Эта программа не оптимизирует траекторию инструмента.

Переменная line_width отвечает за ширину линии при закрашивании области. 

Чем больше значение line_width, тем толще будет линия.

Пример:

line_width = 1: Линия будет иметь толщину в один пиксель.
line_width = 2: Линия будет иметь толщину в два пикселя.
line_width = 3: Линия будет иметь толщину в три пикселя.