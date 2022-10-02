test_list= [[3,4,5],[5,6,7],[45,67,23]]
n= int(input("Enter the element u want to search:"))
res= any(n in sub for sub in test_list)

if(res):
    print("Element is present")
else:
    print("element is not present")
       
