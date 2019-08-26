import julia
import timeit
from functools import partial

julia_large = partial(julia.julia_set,2048,1536)

print(timeit.timeit(julia_large,number=1))