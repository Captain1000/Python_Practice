client_list={1:"Harry",2:"Rohan",3:"Hammad"}
lock_list={1:"Exercise",2:"Diet"}
def getdate():
    import datetime
    return datetime.datetime.now()
try:
    print("Select client Name: ")
    for key,value in client_list.items():
        print("Press",key,"for",value,"\n",end="")
    client_name=int(input())
    print("Selected client: ",client_list[client_name],"\n",end="")
    print("Press 1 for log")
    print("press 2 for Retrieve")
    op=int(input())
    if op == 1:
        for key,value in lock_list.items():
            print("Press",key,"to lock",value,"\n",end="")
        lock_name=int(input())
        print("Selected job: ",lock_list[lock_name])
        f=open(client_list[client_name]+"-"+lock_list[lock_name]+".txt","a")
        k='y'
        while(k != "n"):
            print("Enter",lock_list[lock_name],"\n",end="")
            mytext=input()
            f.write("["+str(getdate())+"]:"+mytext+"\n")
            k=input("Add more?y/n:")
            continue
            f.close()
    elif op == 2:
        for key,value in lock_list.items():
            print("press",key,"to retrieve",value,"\n",end="")
        lock_name=int(input())
        f=open(client_list[client_name]+"-"+lock_list[lock_name]+".txt","rt")
        contents=f.readlines()
        for line in contents:
            print(line,end="")
        f.close()
    else:
        print("invalid input!!!")
except Exception as b:
    print("Wrong input!!!!")
