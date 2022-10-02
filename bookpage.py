def bookpage(n,p):
    return (int(min(p/2,n/2-p/2)))

n= int(input())
p= int(input())
print(bookpage(n,p))
