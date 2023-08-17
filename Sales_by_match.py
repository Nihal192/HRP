def sockMerchant(n, ar):
    color_count={}
    pair_count=0
    for color in ar:
        if color in color_count:
            color_count[color]+=1
        else:
            color_count[color]=1
    for count in color_count.values():
        pair_count+= count//2
    return pair_count
        
            
