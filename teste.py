rows, cols = (5, 15)
arr = [[0 for i in range(cols)] for j in range(rows)]
 
# again in this new array lets change
# the first element of the first row
# to 1 and print the array
arr[0][0] = 1
arr[1][5] = 2
for row in arr:
    print(row)

for yaxis in range(6):
    print(yaxis)
