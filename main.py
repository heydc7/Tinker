def permute(ip, op):
 
    #  base case
    if len(ip) == 0:
        print(op, end="\n")
        return
 
    #  pick lower and uppercase
    ch = ip[0].lower()
    ch2 = ip[0].upper()
    ip = ip[1:]
    permute(ip, op+ch)
    permute(ip, op+ch2)

s = input("Enter your string: ")
permute(s, "")