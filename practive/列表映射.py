def map_to_range(lst):
    if not lst:  # 检查列表是否为空
        return []
    min_val = min(lst)
    max_val = max(lst)
    range_size = len(lst) - 1
    return [(int((x - min_val) / (max_val - min_val) * range_size)) for x in lst]

a = [23,23,23,34,45,45,56,56,57,57,46,24,32,64,75]
map_list = map_to_range(a)
print(a)
print(map_list)