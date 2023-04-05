import numpy as np

data = [1,2,3,4,5,6,7,8,9,10,11,12]
m1 = np.array(data).reshape(2,3,2)

r, g, b = m1[:, :, 0], m1[:, :, 1], m1[:, :, 1]

print("[m1] = %s" % m1)
print("[r,g,b] = %s, %s, %s" % (r, g, b))
