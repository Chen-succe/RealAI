def map_to_unique_range(lst):
    # 找出所有唯一的值，并排序
    unique_values = sorted(set(lst))
    value_to_index = {value: index for index, value in enumerate(unique_values)}
    print(value_to_index)
    # 映射原始列表中的值到新范围
    mapped_list = [value_to_index[value] for value in lst]
    return mapped_list

# 示例列表
original_list = [23,23,23,34,45,45,56,56,57,57,46,24,32,64,75]

# 映射列表中的数字
mapped_list = map_to_unique_range(original_list)

print("原始列表:", original_list)
print("映射后的列表:", mapped_list)