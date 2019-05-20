import rawIdx2formatIdx 
import rawPosition2formatPosition
import birthPositionGenerator
import positionsColorsMapping
# 飞机类

# 飞机颜色, 第几架飞机

# 飞机坐标(依据内外圈确定)[初始化: 出生坐标]



# 飞机是否处于可飞行状态

class Plane:
    def __init__(self,plane_color,plane_idx):
        self.plane_color=plane_color
        self.plane_idx=plane_idx
        self.plane_birth_position=birthPositionGenerator.getBirthPosition(plane_color)
        self.plane_canFly=-1
        self.plane_isCrashed=0
        self.plane_rawWalks=0 # 这个是1呀!!! 妈的我搞了大半天才意识到这个[出生时的格子是1, 步数是0]
        self.plane_finish_state=-1
        self.plane_formatPosition=-1
        self.plane_stand_grid_color=-1
        # self.plane_formatPosition=rawPosition2formatPosition.raw2formatPosition()
        # self.plane_formatPosition=rawPosition2formatPosition.raw2formatPosition(plane_rawWalks,)
        # if self.plane_canFly==1: # 1表示能飞; -1表示不能飞
        #     print('State:Can fly.')
        # elif self.plane_canFly==-1:
        #     print('State: Cannot fly.')

# 注意这里越级了, plane_move本意是叫他动他不得不动, 判定逻辑应该写在外面
# 这样写也可以其实^_^

    def plane_move(self,diceNum): # 状态码: 1表示成功;-1表示失败
        if self.plane_canFly==1:
            print('{}{}飞机移动{}格.'.format(self.plane_color,self.plane_idx,diceNum))
            self.plane_rawWalks+=diceNum
            return 1
        else:
            print('{}{}飞机未起飞,不能动.'.format(self.plane_color,self.plane_idx))
            return -1 # 这个是为了在player里面判断加不加入planesOnFly用的
    def plane_takeOff(self,diceNum):
        if diceNum!=6:
            print('不是6不起飞')
            return -1 # 这个是为了在player里面判断加不加入planesOnFly用的
        elif self.plane_canFly==1:
            print('{}{}飞机已经在飞了'.format(self.plane_color,self.plane_idx))
        else:
            print('{}{}飞机起飞.'.format(self.plane_color,self.plane_idx))
            self.plane_canFly=1
            return 1
    def plane_crash(self):
        if self.plane_isCrashed==1:
            self.plane_rawWalks=0
            self.plane_canFly=-1
    def plane_jump(self,gap=4):
        self.plane_rawWalks+=gap
        print('起跳完成!')
    def plane_getFormatPosition(self):
        self.plane_formatPosition=rawPosition2formatPosition.raw2formatPosition(self.plane_rawWalks,self.plane_birth_position,self.plane_color)
        return self.plane_formatPosition
    def plane_getGridColor(self):
        positions_colors=positionsColorsMapping.getMapping_positionsAndColors()
        if 'out' in self.plane_formatPosition:# 一个道理, 内圈无所谓颜色, 直接在类里面放弃内道
            self.plane_stand_grid_color=positions_colors[self.plane_formatPosition]
            return self.plane_stand_grid_color
    def plane_checkFinish(self):
        if self.plane_formatPosition=='in_0_'+self.plane_color:
            print('Plane finished.')
            self.plane_finish_state=1
            self.plane_rawWalks=-1
            return True
        else:
            return False
    def printData(self):
        print(self.__dict__)

if __name__=='__main__':
    pn=Plane('r',3)
    pn.printData()
    
        

# 越级

    # def plane_move(self,diceNum): #掷色子点数
    #     if self.plane_canFly==1:
    #         self.plane_position+=diceNum
    #     else:
    #         print('This plane {}:{} cannot move.'.format(self.plane_color,self.plane_idx))
    # def plane_occupy(self,grid):
    #     if self.plane_canFly==1
    #         grid.occupiedBy(self)
    #     else:
    #         print('This plane {}:{} cannot occupy.'.format(self.plane_color,self.plane_idx))
    
    


