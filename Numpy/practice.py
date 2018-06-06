# -*- coding: utf-8 -*- 

import numpy as np

print "hello world!"

print(np.__version__)
np.show_config()

Z= np.zeros(10)
print Z

Z = np.arange(10,50)
print(Z)

nz = np.nonzero([1,2,0,0,4,0])
print(nz)

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)


