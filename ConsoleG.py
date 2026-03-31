import tkinter as tk
class CGCreateContext:
    def __init__(self, width=800, height=600, title="ConsoleG"):
        # Создаём главное окно
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")
        self.root.iconphoto(False, tk.PhotoImage(file="icon/exewin.png"))
        # Создаём холст для рисования
        self.canvas = tk.Canvas(self.root, bg="white", width=width, height=height)
        self.canvas.pack(expand=True)

    def CGDrawLine(self, x1, y1, x2, y2, color="black", width=1):
        """Рисует линию между двумя точками"""
        return self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)
    def CGDrawRectangle(self, x1, y1, x2, y2, outline="black", fill="", width=1):
        """Рисует прямоугольник (контур или заполненный)"""
        return self.canvas.create_rectangle(x1, y1, x2, y2, outline=outline, fill=fill, width=width)

    def CGDrawCube(self, x=100, y=100, size=80, color="blue",outline="black",width=1):
        x1, y1 = x, y
        x2, y2 = x + size, y + size
        cube = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline=outline,
            width=width,
        )
    def CGDrawOval(self, x1, y1, x2, y2, outline="black", fill="", width=1):
        """Рисует овал (эллипс)"""
        return self.canvas.create_oval(x1, y1, x2, y2, outline=outline, fill=fill, width=width)

    def CGDrawCircle(self, x, y, radius, outline="black", fill="", width=1):
        """Рисует круг с центром в (x, y) и заданным радиусом"""
        return self.CGDrawOval(x - radius, y - radius, x + radius, y + radius,
                              outline=outline, fill=fill, width=width)

    def CGDrawPolygon(self, points, outline="black", fill="", width=1):
        """Рисует многоугольник по списку точек [(x1,y1), (x2,y2), ...]"""
        return self.canvas.create_polygon(points, outline=outline, fill=fill, width=width)

    def CGUIText(self, x, y, text, color="black", font=("Arial", 10)):
        """Добавляет текст в указанной позиции"""
        return self.canvas.create_text(x, y, text=text, fill=color, font=font)
    def CGRenderClear(self):
        """Очищает холст"""
        self.canvas.delete("all")

    def CGUIButton(self, x, y, text, function=None, width=10, height=1,fill='white',foreground='black',outline=2,font=("Arial", 10)):
        """Создаёт кнопку на холсте"""
        button = tk.Button(
            self.canvas,
            text=text,
            command=function,
            width=width,
            bg=fill,
            bd=outline,
            fg=foreground,
            font=font,
            height=height
        )
        window_id = self.canvas.create_window(x, y, window=button)

    def CGVec2(self, object_id, dx, dy):
        """Двигает объект на dx, dy"""
        self.canvas.move(object_id, dx, dy)

    def CGDelete(self, object_id):
        """Удаляет объект"""
        self.canvas.delete(object_id)

    def CGOutlineColor(self, object_id, color):
        """Меняет цвет контура объекта"""
        self.canvas.itemconfig(object_id, outline=color)

    def CGFill(self, object_id, fill_color):
        """Меняет заливку объекта"""
        self.canvas.itemconfig(object_id, fill=fill_color)

    def CGBackground(self, color):
        """Меняет фон холста"""
        self.canvas.configure(bg=color)

    def CGRotate(self, object_id, angle, center_x, center_y):
        """Поворачивает объект вокруг точки (упрощённо)"""
        # Реализация требует математических вычислений координат
        pass

    def СGStartContext(self):
        """Запускает главный цикл приложения"""
        self.root.mainloop()