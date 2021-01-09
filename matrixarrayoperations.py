import numpy as np
n = np.array([input().split() for y in range(int(input().split()[0]))], int)
#ar = np.array(n,int)
print(np.transpose(n))
print(n.flatten())