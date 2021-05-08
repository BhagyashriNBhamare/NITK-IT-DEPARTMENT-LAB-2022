def main():
    # w=[[1,2,3],[4,5],[]]
    w= [list() for i in range(3)]
    print(w)
    print(w[1])
    print(w[2])
    w[0].append(11)
    print(w)
    for x in w[1]:
        print('i am in loop')
        print(x)
main()