for i in range(1042000, 702648265+1):
    temp=i
    s=0
    while temp!=0:
        r=temp%10
        s=s+r**3
        temp=temp//10
    if s==i:
        print("The first armstrong number is", i)
        break
