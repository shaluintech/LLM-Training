def compare(list_a,list_b):
    a=set(list_a)
    b=set(list_b)
    common=a&b
    only_a=a-b
    combined=a|b
   
    return common ,  only_a , combined


if __name__ == "__main__":
    print(compare([1,2,3,4],[3,4,5]))

