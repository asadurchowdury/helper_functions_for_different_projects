def relevence_finder(lst):
    '''given a list of precision score, this function finds which documents are relevent'''
    rel_index = np.zeros(len(lst))
    for idx in range(1,len(lst)+1):
        lst[idx-1]=lst[idx-1]*idx

    uniq = list(set(lst))
    for val in uniq:
        if val!=0:
            rel_id = lst.index(val)
            rel_index[rel_id]=1
    return rel_index.tolist()