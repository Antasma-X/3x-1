import matplotlib.pyplot as plt
no= int(input("Enter number:"))




list= [no]
while no!=1:
    if no%2==0:
        no=int(no/2)
        list.append(no)
    else:
        no=3*no+1
        list.append(no)

print(list)

plt.plot(list)
plt.show()









