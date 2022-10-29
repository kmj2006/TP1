def squared(n):

def gugudan(i):

def abs_num(k):
    print(abs(k))
    return
def sigma(n, k):

def main():
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