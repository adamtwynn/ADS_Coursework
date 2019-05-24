def count_ephemeral(n1,n2,k):
    #Store k powers and change the list depending on the value of k
    if k == 2:
        powers_lst = [0,1,4,9,16,25,36,49,64,81]
    elif k == 3: 
        powers_lst = [0,1,8,27,64,125,216,343,512,729]
    elif k == 4:
        powers_lst = [0,1,16,81,256,625,1296,2401,4096,6561] 
    keph = 0
    #create two sets to store k-ephemeral numbers and k-eternal numbers
    k_ep_set = set('1')
    k_et_set = set()

    #for each integer n1<=i<n2
    for i in range(n1,n2):
        #convert to string so that it can be iterated through
        num = str(n1)
        sequence = [num]
        
        while True: 
            kchild = 0

            #for each digit
            for x in num:
                x = int(x)
                #calculate kchild/next value in sequence
                kchild = kchild + powers_lst[x]
                
            kchild = str(kchild)

            #if value is in the k eternal set
            if kchild in k_et_set:
                #add the current sequence to the k eternal set
                k_et_set.update(sequence)
                #increment n1
                n1 = n1+1
                break

            #if value is in the k ephemeral set
            #or if value is 1 ('1' is already in the set)
            if kchild in k_ep_set:
                #increment keph (this is returned by the function)
                keph = keph+1
                #add current sequene to the k ephemeral set as all values in the sequence would eventually reach 1
                k_ep_set.update(sequence)
                #increment n1
                n1 = n1+1
                break

            #checks for duplicates
            if kchild in sequence:
                #if there is a duplicate, add to k eternal set
                k_et_set.update(sequence)
                #increment n1
                n1 = n1+1
                break

            #otherwise, add to sequence and loop     
            sequence.append(kchild)
            num = kchild
            
    return keph

#completed in 24 to 28 seconds for n1 = 1, n2 = 10000000, k = 4
