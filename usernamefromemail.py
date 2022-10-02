#Extract username from email id

s= input()
email= s.split('@')
username= email[0]

print("username= ",username)
print("domain= ",email[1].split('.')[0])
