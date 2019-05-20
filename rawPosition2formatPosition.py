from rawIdx2formatIdx import raw2formatIdx

# 概念搞清楚: 1, format_idx是指 以红方出生点为点out_1顺时针到out_52这样的变号, 这样的地标是绝对的, 
# 不根据玩家颜色不同而转移
# 2. 玩家我们用rawWalks进行走子, 为的就是实现走子与定位的逻辑分离, 达到干练目的
# 3. formatPosition指的就是format_idx下面的坐标表示
def raw2formatPosition(rawWalks,birthPosition,color):
    outer_points=[each for each in range(1,53)]*2 # 我设置2个 [1,2,^52,1,2,^52], 因为最坏出生在53+52
    slice_head=birthPosition
    slice_tail=birthPosition+rawWalks # rawWalks就是偏移量, 我们直接把他用切片切出来!!
    if 0<=rawWalks<=52: # 只要没走过52步, 一定还在外圈
        accord_formatIdx=outer_points[slice_tail-1]
        # print('Acc:',accord_formatIdx)
        formatPosition=raw2formatIdx(accord_formatIdx)
    else:
        formatPosition=raw2formatIdx(rawWalks)+'_'+color
    return formatPosition

if __name__=='__main__':
    for walk in range(0,117):
        birthPosition=27
        print(raw2formatPosition(walk,birthPosition,'y'))



