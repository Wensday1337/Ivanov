import os
from image_processing import resize_image, rotate_image

def get_user_input():
    
 #   Запрашивает у пользователя путь к изображению и параметры для обработки.
 #   :return: Путь к изображению, новый размер и угол поворота.
    
    input_path = input("Введите путь к изображению: ")
    
    while not os.path.isfile(input_path):
        print("Файл не найден. Пожалуйста, попробуйте ещё раз.")
        input_path = input("Введите путь к изображению: ")
    
    new_width = int(input("Введите новую ширину изображения: "))
    new_height = int(input("Введите новую высоту изображения: "))
    angle = int(input("Введите угол поворота изображения (в градусах): "))
    
    return input_path, new_width, new_height, angle

def main():
    input_path, new_width, new_height, angle = get_user_input()
    
    # Создание имен для выходных файлов
    resized_output_path = "resized_output.jpg"
    rotated_output_path = "rotated_output.jpg"
    
    # Вызов функций обработки изображений
    resize_image(input_path, resized_output_path, new_width, new_height)
    rotate_image(input_path, rotated_output_path, angle)

if __name__ == "__main__":
    main()
