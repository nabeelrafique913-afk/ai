import numpy as np

company , evolution , city , country = np.genfromtxt('nabeel/usstate.csv', delimiter=',', usecols=(0,2,4,5),unpack=True,dtype=None,skip_header=1)


col_index=2
evolution=np.char.replace(evolution,'$','')
evolution=evolution.astype(float)
print(evolution)

print('mean:',np.mean(evolution))