from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
 #    Изменяет размер изображения до заданной ширины и высоты.
 #   :param input_path: Путь к входному изображению.
 #   :param output_path: Путь для сохранения изменённого изображения.
 #   :param new_width: Новая ширина изображения.
 #   :param new_height: Новая высота изображения.
    
    try:
        with Image.open(input_path) as img:
            img = img.resize((new_width, new_height), Image.ANTIALIAS)
            img.save(output_path)
            print(f"Изображение изменено и сохранено как {output_path}")
    except Exception as e:
        print(f"Ошибка при изменении размера изображения: {e}")

def rotate_image(input_path, output_path, angle):

 #   Поворачивает изображение на заданный угол.
 #   :param input_path: Путь к входному изображению.
 #   :param output_path: Путь для сохранения повёрнутого изображения.
 #   :param angle: Угол поворота в градусах.
    
    try:
        with Image.open(input_path) as img:
            img = img.rotate(angle, expand=True)
            img.save(output_path)
            print(f"Изображение повёрнуто на {angle} градусов и сохранено как {output_path}")
    except Exception as e:
        print(f"Ошибка при повороте изображения: {e}")
