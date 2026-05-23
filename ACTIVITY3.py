num=int(input("Enter a number: "))
ans=0
temp=num
while temp>0:
    x=temp%10
    ans+=x**3
    temp=temp//10
if num==ans:
    print("IT IS AN ARMSTRONG NUMBER")
else:
    print("IT IS NOT AN ARMSTRONG NUMBER")