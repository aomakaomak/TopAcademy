start = 100
end = 999

sum_ = 0

while start <= end:
    first_figure = start // 100
    second_figure = (start - first_figure*100) // 10
    third_figure = start % 10
    if first_figure == second_figure and first_figure == third_figure:
        start += 1
        continue
    if first_figure == second_figure or first_figure == third_figure or second_figure == third_figure:
        sum_ += start
        print(first_figure, second_figure, third_figure)
    start += 1
print(sum_)