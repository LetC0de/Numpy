import numpy as np
ar = np.array([1,2,3,4,5,6])
print(ar)
print(type(ar))
print(ar.dtype)
print(ar.shape)
print(ar.size)
print(ar.astype(str))


#creating a two-diamentional array

# d2=np.array([

#     [1,2,3],
#     [4,5,6],
#     [7,8,9]

# ])

# print(d2)
# print(d2.shape)


#creating initialized array

# a = np.zeros((3,3) , dtype=int )
# print(a)


# b= np.ones((3,3),dtype=int)
# print(b)

# c= np.arange(100,150,2)
# print(c)


# d= np.random.rand(2,4)
# print(d)


# print(np.linspace(10,20,3))

# print(np.full((3,3),10))


print(ar + 5)
print(ar * 2)
print(ar ** 2)


#fancy indexing --> selecting and accesing multiple elements from array by its index 

print(ar[[0,2,3]])

#boolean masking --> to filtering an array with some conditions 

print(ar[ar>2])
print(ar[ar == 3 ])

#reshaping and manipulation

reshaped=ar.reshape([2,3])
print(reshaped)


#fletening array
#1 .ravel() --> view 
#2 .fletten() --> copy 


mdarr=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])

print(mdarr.ravel())
print(mdarr.flatten())

#insert 

print(ar)
newar=np.insert(ar,2,100) #1d
print(newar)


print(mdarr)
newmd=np.insert(mdarr,3,[10,11,12],axis=None) # 2d
print(newmd)

#append

print(ar)
arr2=np.append(ar,[7,8,9])
print(arr2)

#concatenate
ar2=np.array([[1,2,3],[4,5,6]])

concat=np.concatenate((mdarr,ar2),axis=0)
print(concat)

#removing 

# print(ar)
# delar=np.delete(ar,2,axis=0) #-->1D
# print(delar)

# print(mdarr)
# delar2= np.delete(mdarr,2,axis=1)#---> 2D
# print(delar2)

#stacking (merging and combining stacks or arrays)
# print("hi")
ar5=np.array([6,7,8])
ar3=np.array([6,7,8,9])

# print(np.vstack((ar5,ar3)))
# print(np.hstack((ar5,ar3)))


#spliting

print("hii")
print(mdarr)
# print(np.split(ar3,2))
print(np.vsplit(mdarr,3))
print(np.hsplit(mdarr,3))

#discount funtion 

# prices=[100,200,300]

# discount=10

# final_price=[]

# for price in prices:
#     final_prices = price - (price*discount/100)
#     final_price.append(final_prices)
    

# print(final_price)




#with np

prices=np.array([100,200,300])
discount=10

finalprice = prices - (prices * discount/100)
print(finalprice)


#np.isnan(array)

arr=np.array([1,2,np.nan,3,np.nan,5,6])
print(np.isnan(arr))


#np.nan_to_num(array, nan=value)

print(np.nan_to_num(arr,nan=20))

#np.isinf() 10^10000 , 1/0

arr3=np.array([1,2,np.inf,3,4,-np.inf,6])
print(np.isinf(arr3))

#replace inf value 

clean=np.nan_to_num(arr3,posinf=1000,neginf=-1000)
print(clean)