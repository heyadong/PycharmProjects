# from PIL import Image
# import matplotlib.pyplot as plt
# from datetime import datetime
# import numpy as np
# start_time = datetime.now()

# print(im1)
# # im1.histogram 获取直方图数据
# data_1 = np.array(im1.histogram())
# data_2 = np.array(im2.histogram())
# # 计算相似度
# print(sum(1-abs(data_1-data_2)/max(max(data_2),max(data_1)))/len(data_1))
# end_time = datetime.now()
# print((end_time-start_time))
# from PIL import Image
# from PIL import ImageFilter
# from PIL import ImageOps
# import math
#
#
# # This module classify the image by  Discrete Cosine Transform and the  accurate rate has a little improve.
# #

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps
import math
def get_code(List, middle):
    result = []
    for index in range(0, len(List)):
        if List[index] > middle:
            result.append("1")
        else:
            result.append("0")
    return result


def comp_code(code1, code2):
    num = 0
    for index in range(0, len(code1)):
        if str(code1[index]) != str(code2[index]):
            num += 1
    return 1-num/len(code1)


def get_middle(List):
    li = List.copy()
    li.sort()
    value = 0
    if len(li) % 2 == 0:
        index = int((len(li) / 2)) - 1

        value = li[index]
    else:
        index = int((len(li) / 2))
        value = (li[index] + li[index - 1]) / 2
    return value


def get_matrix(image):
    matrix = []
    size = image.size
    for height in range(0, size[1]):
        pixel = []
        for width in range(0, size[0]):
            pixel_value = image.getpixel((width, height))
            pixel.append(pixel_value)
        matrix.append(pixel)

    return matrix


def get_coefficient(n):
    matrix = []
    PI = math.pi
    sqr = math.sqrt(1 / n)
    value = []
    for i in range(0, n):
        value.append(sqr)
    matrix.append(value)

    for i in range(1, n):
        value = []
        for j in range(0, n):
            data = math.sqrt(2.0 / n) * math.cos(i * PI * (j + 0.5) / n);
            value.append(data)
        matrix.append(value)

    return matrix


def get_transposing(matrix):
    new_matrix = []

    for i in range(0, len(matrix)):
        value = []
        for j in range(0, len(matrix[i])):
            value.append(matrix[j][i])
        new_matrix.append(value)

    return new_matrix


def get_mult(matrix1, matrix2):
    new_matrix = []

    for i in range(0, len(matrix1)):
        value_list = []
        for j in range(0, len(matrix1)):
            t = 0.0
            for k in range(0, len(matrix1)):
                t += matrix1[i][k] * matrix2[k][j]
            value_list.append(t)
        new_matrix.append(value_list)

    return new_matrix


def DCT(double_matrix):
    n = len(double_matrix)
    A = get_coefficient(n)
    AT = get_transposing(A)

    temp = get_mult(double_matrix, A)
    DCT_matrix = get_mult(temp, AT)

    return DCT_matrix


def sub_matrix_to_list(DCT_matrix, part_size):
    w, h = part_size
    List = []
    for i in range(0, h):
        for j in range(0, w):
            List.append(DCT_matrix[i][j])
    return List


def classify_DCT(image1, image2, size=(32, 32), part_size=(8, 8)):

    assert size[0] == size[1], "size error"
    assert part_size[0] == part_size[1], "part_size error"
    image1 = image1.resize(size).convert('L').filter(ImageFilter.BLUR)
    image1 = ImageOps.equalize(image1)
    matrix = get_matrix(image1)
    DCT_matrix = DCT(matrix)
    List = sub_matrix_to_list(DCT_matrix, part_size)
    middle = get_middle(List)
    code1 = get_code(List, middle)

    image2 = image2.resize(size).convert('L').filter(ImageFilter.BLUR)
    image2 = ImageOps.equalize(image2)
    matrix = get_matrix(image2)
    DCT_matrix = DCT(matrix)
    List = sub_matrix_to_list(DCT_matrix, part_size)
    middle = get_middle(List)
    code2 = get_code(List, middle)

    return comp_code(code1, code2)
im1 = Image.open('example_jpg/1.jpg')
im2 = Image.open('example_jpg/2.jpg')
print(classify_DCT(im1, im2))
