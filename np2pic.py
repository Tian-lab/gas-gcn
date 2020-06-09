import numpy as np
import matplotlib.pyplot as plt
# import scipy.misc
data = np.load('a.npy')
frame_a=data[1,1,0,:,:]
expand_a = np.zeros((250,250))
for i in range(25):
    for j in range(25):
        m = frame_a[i,j]
        for t in range(10):
            for k in range(10):
               expand_a[i*10+t,j*10+k]=m
# scipy.misc.imsave('out.jpg',expand_a)
plt.imshow(frame_a,cmap='gray')
fig = plt.gcf()
plt.show()
fig.savefig('out.jpg')