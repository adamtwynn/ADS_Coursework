def hash_quadratic(keys):
    table = ["-"]*19
    #initialize table
    n=0
    for x in keys:
        #for each key in the original list
        pos = (6*keys[n]+3)%19
        #calculate the position in the hash table using the hash function
        pos2 = pos
        j=1
        while True:
            if table[pos] == "-":
                #if the bucket is empty
                table[pos] = keys[n]
                #add key
                break
            else:
                pos = (pos2 + j**2)%19
                #if bucket isn't empty +1, +2, +4, +9 etc (quadratic probing).
                j = j+1
                if j == 20:
                #after 20 attempts, stop as all possibilities have been looked at
                    break
        n = n+1
        #look at next key
    return table

def hash_double(keys):
    table = ["-"]*19
    #initialize table
    n=0
    for x in keys:
         #for each key in the original list
        j=1
        pos = (6*keys[n]+3)%19
        #calculate the position in the hash table using the hash function
        while True:
            if table[pos] == "-":
                #if the bucket is empty
                table[pos] = keys[n]
                #add key
                break
            else:
                pos = (pos + (11-(keys[n]%11)))%19
                #if bucket isn't empty apply secondary hash function
                j = j+1
                if j == 20:
                #stop after 20 iterations as all buckets will have been looked at
                    break
        n = n+1
        #look at next key
    return table

