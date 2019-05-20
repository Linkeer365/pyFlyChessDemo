# import rawIdx2formatIdx # 这个主要处理"位置格式化"
# import rawPosition2formatPosition # 这个主要处理 "走步格式化"
import chessBoard

def getMapping_positionsAndColors():
    # for outer part
    positions_colors=dict()
    cb=chessBoard.ChessBoard()
    for each1 in cb.grids:
        for each2 in each1.__dict__:
            if 'color' in each2:
                one_color=each1.__dict__[each2]
            if 'formatIdx' in each2:
                if not 'in' in each1.__dict__[each2]: # 内圈没有跳转问题
                    one_position=each1.__dict__[each2]
        positions_colors[one_position]=one_color
    print(positions_colors)
    return positions_colors
if __name__=='__main__':
    getMapping_positionsAndColors()
    
    

    