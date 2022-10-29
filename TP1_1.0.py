a=[]
def squared(n):
    print (n*n , n*n*n , n*n*n*n)

def gugudan(i):
    for x in range(1,10):
        a.append(f'{i}x{x}={i*x}')
    return a
def abs_num(k):
    print(abs(k))
    return
def sigma(n, k):
    sum=0
    for i in range(k,n+1):
        sum+=(i*i)
    print(sum)
def main():
<<<<<<< HEAD
<<<<<<< HEAD

=======
    k,n,i = map(int,input().split())
    mode = int(input()):
    if mode == 1:
        squared(n)
    elif mode == 2:
        gugudan(i)
    elif mode ==3:
        abs_num(k)
    elif mode ==4:
        sigma(n,k)

if __name__=="__main__":
    main()