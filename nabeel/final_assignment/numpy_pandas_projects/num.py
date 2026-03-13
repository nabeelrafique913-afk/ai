import numpy as np

ids, xyz , long , lat = np.genfromtxt('nabeel/kagglerealstate.csv', delimiter=',', usecols=(1,2,3,4), unpack=True, dtype=None,skip_header=1)


print("kagglerealstate.csv : " , np.mean(xyz))
print("kagglerealstate.csv : " , np.average(xyz))
print("kagglerealstate.csv : " ,np.std(xyz))
print("kagglerealstate,csv : " ,np.square(xyz))
