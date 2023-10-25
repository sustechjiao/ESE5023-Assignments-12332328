#test4
def least_moves(x):
    if x < 1:
        raise ValueError

    moves = 0
    current = 1

    while current < x:
        if x % 2 == 0:  # 如果 x 是偶数，翻倍
            x //= 2
        else:  # 如果 x 是奇数，加一
            x -= 1
        moves += 1

    return moves

# 示例:
x1 = 2
x2 = 5

print(f"Least moves to reach {x1} RMB: {least_moves(x1)}")
print(f"Least moves to reach {x2} RMB: {least_moves(x2)}")
