def getBirthPosition(player_color):
    ''' 1 red;
        2 yellow;
        3 blue;
        4 green;
    '''
    indices_colors=enumerate(['r','y','b','g'],1)
    for idx,color in indices_colors:
        if color==player_color:
            multiplex_factor=idx # 比如说红1黄2, 那么说明, 红方出生位置就是1号位置, 而黄方出生在过1/4圈的地方, 也就是13+1=14格位置
            break
    birthPosition=(multiplex_factor-1)*13+1
    return birthPosition

if __name__=='__main__':
    for color in ['r','y','b','g']:
        print(color,'->',getBirthPosition(color))


