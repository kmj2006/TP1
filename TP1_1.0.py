a=[]
def squared(n):

def gugudan(i):
    for x in range(1,10):
        a.append(f'{i}x{x}={i*x}')
    return a
def abs_num(k):


def sigma(n, k):

def main():
    mode= int(input()):
    if mode == 1:
        squared(n)
    elif mode == 2:
        i = int(input())
        print(gugudan(i))
    elif mode == 3:
        abs_num(k)
    elif mode == 4:
        sigma(n,k)
if __name__=="__main__":
    main()