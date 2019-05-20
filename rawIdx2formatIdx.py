def raw2formatIdx(raw_idx):
    distance_to_endPoint=0
    if 1<=raw_idx<=52: 
        format_idx='out_'+str(raw_idx)
    else:
        format_idx='in_'
        if 53<=raw_idx<=57:
             distance_to_endPoint=58-raw_idx
        elif raw_idx>=58:
            # 对不起, 这个算法老是想不出, 不得已出此下策,对不起!!
            # ring_buffer
            # 这里一共10个数, 那么整除9肯定可以reach
            distances=[0,1,2,3,4,5,4,3,2,1]*(58+(raw_idx-58)//9)
            distance_to_endPoint=distances[raw_idx-58]
        format_idx+=str(distance_to_endPoint)
    return format_idx

if __name__=='__main__':
    for i in range(12,100):
        print(i,'->',raw2formatIdx(i))