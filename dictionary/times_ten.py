def times_ten(s_index: int, e_index: int):
    times_ten_dict = {}
    for i in range(e_index - s_index + 1):
        times_ten_dict[s_index] = s_index * 10
        s_index += 1
    return times_ten_dict
