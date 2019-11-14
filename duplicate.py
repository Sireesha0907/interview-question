def dupli(dup):
    lis=[]
    for num in dup:
        if num not in lis:
            lis.append(num)
    return lis

	
# Driver Code 
dup = [2, 2,3,5,6,7,9,0,1,1,1,4, 10, 20, 5, 2, 20, 4] 
print(dupli(dup)) 
