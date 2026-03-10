import numpy as np

address, latitude , name , postalcode = np.genfromtxt('nabeel/fooddata.csv', delimiter=',',invalid_raise=False, usecols=(2,4,5,7),unpack=True,dtype=("U100","f8","f8","U100"),skip_header=1)

print(address)
print(latitude)
print(name)
print(postalcode)

cleaned_latitude=latitude[~np.isnan(latitude)]

str = address
print(str.count("u"))

# statics operation

print('mean:',np.nanmean(latitude))
# print('mean:',np.nanaverage(latitude))
print('std:',np.nanstd(latitude))
print('median:',np.nanmedian(latitude))
print('percentile:',np.nanpercentile(latitude,25))
print('percentile 5:',np.nanpercentile(latitude,5))

print('min:',np.nanmin(latitude))
print('max:',np.nanmax(latitude))

# math operation 

print('squ:',np.square(latitude))
print('sqrt:',np.sqrt(latitude))
print('abs:',np.abs(latitude))
print('power:',np.power(latitude,postalcode))

