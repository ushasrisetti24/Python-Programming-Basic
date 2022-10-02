def bonAppetit(bill, k, b):
    sum=0
    charge1=0
    charge2=0
    charge=0
    for i in bill:
        sum+= i
          
         
    charge1= sum//2
    charge2= (sum-bill[k])//2
    charge= charge1-charge2
    if(charge2==b):
        print("Bon Appetit")
    else:
        print(b-charge2)
        
first_multiple_input = input().rstrip().split()

n= int(first_multiple_input[0])
k = int(first_multiple_input[1])
bill = list(map(int, input().rstrip().split()))
b = int(input().strip())
bonAppetit(bill, k, b)

 
