ranks = list(range(8))
print(ranks)
r1, r2 = ranks[:4], ranks[4:]

process_group = [pid for pid in [r1, r2]]
print(process_group)