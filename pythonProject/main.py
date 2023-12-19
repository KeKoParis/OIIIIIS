import numpy
from PIL import Image
import copy

Anaglyphs0 = [[0.299, 0.587, 0.114],
              [0, 0, 0],
              [0, 0, 0]]
Anaglyphs1 = [[0, 0, 0],
              [0, 0, 0],
              [0.299, 0.587, 0.114]]
Anaglyphs2 = [[0, 0, 0],
              [0.299, 0.587, 0.114],
              [0.299, 0.587, 0.114]]
Anaglyphs3 = [[1, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
Anaglyphs4 = [[0, 0, 0],
              [0, 1, 0],
              [0, 0, 1]]
Anaglyphs5 = [[0, 0.7, 0.3],
              [0, 0, 0],
              [0, 0, 0]]


def open_files():
    img_list = [numpy.asarray(Image.open("colour.png")),
                numpy.asarray(Image.open("half_colour.png")),
                numpy.asarray(Image.open("optimized.png"))]
    return img_list


def matrix_multiplication(matrix_from, matrix_to):
    resulting_matrix = []
    for row in range(3):
        temp_result = 0
        for collumn in range(3):
            temp_result += matrix_from[row][collumn] * matrix_to[collumn]
        resulting_matrix.append(temp_result)
    return resulting_matrix


def matrix_addition(matrix_from, matrix_to):
    resulting_matrix = copy.deepcopy(matrix_to)
    for number in range(len(matrix_from)):
        resulting_matrix[number] += matrix_from[number]
    return resulting_matrix


def Anaglyphs(img_to, img_from, anaglyph_to, anaglyph_from):
    result_array = img_to.tolist()
    for row in range(len(img_to)):
        for collumn in range(len(img_to[row])):
            result_array[row][collumn] = matrix_addition(matrix_multiplication(
                anaglyph_to, img_to[row][collumn]), matrix_multiplication(anaglyph_from, img_from[row][collumn]))
    result_array = numpy.array(result_array, int).astype(numpy.uint8)
    processed_image = Image.fromarray(result_array)
    return processed_image


def AllAnaglyphs(img_list):
    half_an = Anaglyphs(img_list[0], img_list[1], Anaglyphs0, Anaglyphs4)
    colour_an = Anaglyphs(img_list[0], img_list[1], Anaglyphs3, Anaglyphs4)
    optimised_an = Anaglyphs(img_list[0], img_list[1], Anaglyphs5, Anaglyphs4)
    colour_an.save("colour_an.png")
    half_an.save("half_an.png")
    optimised_an.save("optimised_an.png")


def main():
    img_list = open_files()
    AllAnaglyphs(img_list)


if __name__ == "__main__":
    main()
