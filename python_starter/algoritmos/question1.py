import math
import os
import random
import re
import sys

def closestNumbers(numbers):
    numbers.sort()  # Ordenar em ordem crescente
    pares = []

    # Iterar pelo array ordenado para encontrar pares com diferença absoluta mínima de 1
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) == 1:
            pares.append((numbers[i], numbers[i + 1]))

    # Imprimir os pares com diferença absoluta mínima de 1
    for par in pares:
        print(par[0], par[1])  # Imprimir os elementos fora dos parênteses

if __name__ == '__main__':
    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    closestNumbers(numbers)
