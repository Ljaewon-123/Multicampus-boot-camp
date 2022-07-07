array = [45,12,85,32,89,39,69,44,42,1,6,8]

tmp = 0

for i in range(len(array)):
    for j in range(i-1,-1,-1):
        # print('notnot',i,j)
        if array[j] < array[j-1]:
            tmp = array[j]
            array[j] = array[j-1]
            array[j-1] = tmp
            print(array,i,j)

print(array)