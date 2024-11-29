import os


# print(os.environ["RANK"])
# print(os.environ["SLURM_PROCID"])
def assert_a(a):
    print(a)
    assert a == 4


assert_a(6)
