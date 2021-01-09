import numpy as np



n = [ele for ele in input().split(' ')]
np_arr = np.array(n,int)
print(np.reshape(np_arr,(3,3)))


