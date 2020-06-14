str="string"
def substring(str):
    if len(str)==0:
        return
    print(str[0])
    str=str[1:(len(str))]
    substring(str)
substring(str)
