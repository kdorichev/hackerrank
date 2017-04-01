if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0,N):
        line = input()
        args = line.split()
        if args[0]=='print':
            print(lst)
        elif args[0]=='insert':
            lst.insert(int(args[1]),int(args[2]))
        elif args[0]=='remove':
            lst.remove(int(args[1]))
        elif args[0]=='append':
            lst.append(int(args[1]))
        elif args[0]=='sort':
            lst.sort()
        elif args[0]=='pop':
            lst.pop()
        elif args[0]=='reverse':
            lst.reverse()
        else:
            continue
