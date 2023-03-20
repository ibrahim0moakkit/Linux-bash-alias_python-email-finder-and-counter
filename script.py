import sys

filename = sys.argv[1]

with open(filename) as fh:
    lst = list()
    temp=list()
    count=0
    my_dict = {}
    for line in fh:
        if line.startswith("From "):
            words=line.split()
            if words not in lst:
                lst.append(words[1:2])
                print(words[1:2])

    for element in lst:
        for x in element:
            if x in my_dict:
                my_dict[x]=my_dict[x]+1
            else:
                my_dict[x]=1

    largest=0
    for k,v in my_dict.items():
        if v>largest:
            largest=v
            email=k
    
    print("This email: "+email+", is the most used with: "+str(largest)+" times")
