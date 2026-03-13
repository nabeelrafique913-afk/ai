import numpy as np

brokered_by, status, price, bed, bath = np.genfromtxt('nabeel/kagglerealstate.csv', delimiter=',',usecols=(0,1,2,3,4),unpack=True,dtype=None,skip_header=1)

print(price)

# statics operation


print("kagglerealstate.csv:mean",np.mean(bed))
print("kagglerealstate.csv:avg",np.average(bed))
print("kagglerealstate.csv:std",np.std(bed))
print("kagglerealstate.csv:mod",np.median(bed))
print("kagglerealstate.csv:pecentile -25",np.percentile(bed,25))
print("kagglerealstate.csv:pecentile -5",np.percentile(bed,5))

print("kaggle,min:",np.min(bed))
print("kaggle,mix:",np.max(bed))

# math operation power

print("kaggle.square:",np.square(bed))
cleaned_bed=bed[~np.isnan(bed)]
print("kaggle.sqrt:",np.sqrt(bed))
print("kaggle,abs:",np.abs(bed))
print("kaggle,power:",np.power(np.abs(bed),np.abs(bath)))


# arthamatics operations

addition= bed +  price
subtraction=  bed - price
multiplication= bed  * price
division= bed / price

print("kaggle,add:", addition)
print("kaggle,sub:",subtraction)
print("kaggle,mul:",multiplication)
print("kaggle,div:",division)

#Trigonometric Functions

pricePie = (price/np.pi) +1
# Calculate sine, cosine, and tangent
sine_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("pricepie sin:",np.sin(pricePie))
print("cos:",np.cos(pricePie))
print("tan:",np.tan(pricePie))


# Calculate the natural logarithm and base-10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("array:",log_array)
print("10 array:",log10_array)

#Example: Hyperbolic Sine
# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)

print("sin h:",sinh_values)

#Hyperbolic Cosine Using cosh() Function
# Calculate the hyperbolic cosine of each element
cosh_values = np.cosh(pricePie)

print("cos h:",cosh_values)

#Example: Hyperbolic Tangent
# Calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)

print("tan h:",tanh_values)

# Calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)

print("asin:",asinh_values)

#Example: Inverse Hyperbolic Cosine
# Calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)

print("acos:",acosh_values)

#Zameen.com price Plus bed - 2 dimentional arrary
D2pricebed = np.array([price,
                  bed])

print("D2:",D2pricebed)

# check the dimension of array1
print("array find price and bed:",D2pricebed.ndim)

# Output: 2

# return total number of elements in array1

print("size p aand b:",D2pricebed.size)

# return a tuple that gives size of array in each dimension

print("shape:",D2pricebed.shape)

# check the data type of array1
print("dtype:",D2pricebed.dtype)

# Splicing array
D2pricebedSlice=  D2pricebed[:1,:10]
print("slice:",D2pricebedSlice)

D2pricebedSlice2=  D2pricebed[:1, 4:15:4]
print("slice2:",D2pricebedSlice2)

# Indexing array

D2pricebeditemonly=D2pricebed[0,1]
print("item:",D2pricebeditemonly)
D2pricebed2ItemOnly=  D2pricebedSlice2[0, 2]
print("2item:",D2pricebed2ItemOnly)
