def moshabehat(l1 , l2):
    r = 0
    for i in range(min(len(l1),len(l2))):
        if l1[i] == l2[i]:
            r+=1
    r = r/len(l1)
    return r