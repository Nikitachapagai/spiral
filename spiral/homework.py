def spiralize(number):
    mid_point = (number - 1) / 2
    diagonal = (3 + 2 * mid_point * (8 * mid_point * mid_point + 15 * mid_point + 13)) / 3
    return int(diagonal)


print(spiralize(501))
