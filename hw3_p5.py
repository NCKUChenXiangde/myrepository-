#H24124068 陳祥德
input("input sequence of seats:")
def trap(height):
    if not height:
        return 0

    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n - 1] = height[n - 1]

    i = 1
    while i < n:
        left_max[i] = max(left_max[i - 1], height[i])
        i += 1

    j = n - 2
    while j >= 0:
        right_max[j] = max(right_max[j + 1], height[j])
        j -= 1

    water_volume = 0
    k = 0
    while k < n:
        water_volume += min(left_max[k], right_max[k]) - height[k]
        k += 1

    return water_volume

   