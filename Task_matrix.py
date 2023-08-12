my_matrix = [[1, 2, 3], [4, 5, 6]]


def trans_for(matrix: list[list[int]]) -> list[list[int]]:
    temp = []
    for i in range(len(matrix[0])):
        temp.append([])
        for j in range(len(matrix)):
            temp[i].append(matrix[j][i])
    return temp

def trans_zip(matrix: list[list[int]]) -> list[list[int]]:
    return list(zip(*matrix))

print(trans_for(my_matrix))
print(trans_zip(my_matrix))