import rawIdx2formatIdx
# 格子类型: 两种格子(外圈格子和内圈格子), 
# 格子颜色, 格子坐标(依据内外圈确定) // 不用内外圈, 写一个内外圈判定即可
# 格子被几个飞机占有(飞机个数), 被几种飞机占有(飞机颜色)

# 创造性想法:因为内圈是独立的并且有回退情况, 所以不如用ring_buffer
class Grid:
    def __init__(self,grid_color,grid_rawIdx):
        # 传参, 格子颜色, 格子坐标
        self.grid_color=grid_color
        self.grid_rawIdx=grid_rawIdx
        # 生成空元组的"占据状态栏", 空列表的"占据历史"
        self.grid_occupy_state=()
        self.grid_occupy_history=[]
        self.grid_formatIdx=rawIdx2formatIdx.raw2formatIdx(grid_rawIdx)
        
        # self.grid_type=grid_type
        # if grid_type=='outside':
        #     self.gridIdxBound=52 # 外圈最多52格子
        # elif grid_type=='inside':
        #     self.gridIdxBound=7 # 内圈最多7格子
    
# 这段occupied问题在于越权了, grid不应该左右plane的行为, 
# 应该由更高层级进行行为设计

    # def occupiedBy(self,plane):
    #     # 此处plane对象已经被外部确定了
    #     self.grid_occupy_state=(plane,plane.plane_color, plane.plane_idx)
    #     self.grid_occupy_history.append(self.grid_occupy_state)
    #     print('Show occupy_state:',self.grid_occupy_state)
    #     print('Show occupy_history:',self.grid_occupy_history)
    
    def printGrid(self): # 这个招数要学会
        print(self.__dict__)
    # def overlapRegulate(self,occupy_history):
    #     if len(occupy_history)>1:
    #         print('领空出现重合, 现在检查敌机:>>')
    #         if occupy_history[0][1]==occupy_history[1][1]: # 检查plane_color这项; 同色飞机, 迭子
    #             print('同色飞机:迭子')
    #         else:
    #             crashedPlane=self.grid_occupy_history.pop(0)[0]
    #             print('撞子:{}-{}被撞下来'.format(crashedPlane.plane_color,crashedPlane.plane_idx)
    def grid_getFormatIdx(self):
        return self.grid_formatIdx
#外圈和内圈思路很好, 但还是一样越权问题

    # def isOuterCircle(self):
    #     if self.grid_idx<=52:
    #         return True
    #     else:
    #         return False
    # def isInnerCircle(self):
    #     if self.grid_idx>52:
    #         return True
    #     else:
    #         return False

if __name__=='__main__':
    gd=Grid('r',58)
    gd.printGrid()

    