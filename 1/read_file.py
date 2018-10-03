# 1.2

from quicksort import Quicksort

numbers_list = [int(line.rstrip('\n')) for line in open('numbers.txt')]
Quicksort(numbers_list)

print(numbers_list)