import plane
import birthPositionGenerator
import throwDice
import random

import positionsColorsMapping
class Player:
    def __init__(self,player_color):
        self.player_color=player_color
        self.player_planesOnWait=[plane.Plane(plane_color=player_color,plane_idx=eachIdx) for eachIdx in range(1,5)]
        self.player_planesOnFly=[]
        self.player_planesFinish=[]
        # self.player_player_touch=0
        self.player_diceNum=0
        self.player_isHisTurn=0
        self.player_winnerState=-1
    def player_check_isHisTurn(self,throwCnt): # 比如第2手就是黄打, 第6手还是黄打
        colors=['r','y','b','g']
        if self.player_color==colors[throwCnt%4-1]:
            print('&&&&&&&&&&&')
            print('Player {} turn!'.format(self.player_color).center(50))
            print('$$$$$$$$$$$')
            self.player_isHisTurn=1
            return True
        else:
            # print('Not Player {} turn!'.format(self.player_color))
            return False
    def player_throwDice(self):
        if self.player_isHisTurn==1:
            self.player_diceNum=throwDice.getDiceNum()
    def player_jump(self):
        for plane in self.player_planesOnFly:
            if plane.plane_getGridColor()==plane.plane_color:
                plane.plane_jump()
                print('{}{}从{}起跳'.format(plane.plane_color, plane.plane_idx,plane.plane_getFormatPosition()))
    def player_regulatePosition(self): # 写入formatPosition这个data fields; 利用formatPosition得到格子颜色
        for plane in self.player_planesOnFly:
            plane.plane_getFormatPosition()
        for plane in self.player_planesOnWait:
            plane.plane_getFormatPosition()
    # def player_get_stand_grid_color(self):
    #     positions_colors=positionsColorsMapping.getMapping_positionsAndColors()
    #     for plane in self.player_planesOnFly:
    #         plane.plane_stand_grid_color=positions_colors[plane.plane_getFormatPosition()]
    #     for plane in self.player_planesOnFly:
    #         plane.plane_stand_grid_color=positions_colors[plane.plane_getFormatPosition()]
    def player_checkFinish(self):
        for plane in self.player_planesOnFly:
            if plane.plane_checkFinish():
                self.player_planesOnFly.remove(plane)
                self.player_planesFinish.append(plane)
    def player_checkWinner(self):    
        self.player_winnerState=1 if len(self.player_planesFinish)==4 else -1
        if self.player_winnerState==1:
            print('***You win. omededo!****')
            return True
    def player_touch(self):
        if self.player_isHisTurn==1:
            if bool(self.player_planesOnFly)==0 and bool(self.player_planesOnWait)!=0: #停机坪上有飞机;#一架飞机都没有起飞
                this_plane=self.player_planesOnWait[0]
                # self.player_player_touch=this_plane # player_player_touch表示玩家状态
                static_code=this_plane.plane_takeOff(self.player_diceNum)
                if static_code==1:
                    print('Suc:Plane:{}-{} takeoff.'.format(this_plane.plane_color,this_plane.plane_idx))
                    self.player_planesOnFly.append(this_plane)
                    self.player_planesOnWait.pop(0)
                # if this_plane.plane_canFly==-1:
                #     this_plane.plane_takeOff(self.player_diceNum)
                # elif this_plane.plane_canFly==1:
                #     this_plane.plane_move(self.player_diceNum)
            else: # 存在一架起飞的飞机
                if self.player_diceNum!=6 and bool(self.player_planesOnFly)!=0: # 有飞机飞, 但没抛出6
                    this_plane=random.choice(self.player_planesOnFly) # 随便选一架
                    static_code=this_plane.plane_move(self.player_diceNum)
                    if static_code==1:
                        print('Suc: Plane:{}-{} move.'.format(this_plane.plane_color,this_plane.plane_idx))
                        pass # self.player_planesOnFly.append(this_plane) 已经在飞就不用加了
                    # self.player_player_touch=this_plane
                else:
                    if bool(self.player_planesOnFly)==0 and bool(self.player_planesOnWait)==0:
                        self.player_checkWinner()
                    else:
                        flag=1
                        promptLine='Take off or move:>>'
                        while flag:
                            takeoff_or_move=input(promptLine)
                            if 'm' in takeoff_or_move: # 选了移动
                                flag=0
                                this_plane=random.choice(self.player_planesOnFly) # 随便选一架
                                static_code=this_plane.plane_move(self.player_diceNum)
                                if static_code==1:
                                    print('Suc:Plane:{}-{} move.'.format(this_plane.plane_color,this_plane.plane_idx))
                                    pass # self.player_planesOnFly.append(this_plane) 已经在飞就不用飞了
                            elif 't' in takeoff_or_move: #选了起飞
                                if len(self.player_planesOnWait)!=0: # (注意如果已经全部起飞;就不能起飞了)
                                    flag=0
                                    this_plane=self.player_planesOnWait[0] # 停机坪上
                                    # self.player_player_touch=this_plane
                                    static_code=this_plane.plane_takeOff(self.player_diceNum)
                                    if static_code==1:
                                        print('Suc:Plane:{}-{} takeoff.'.format(this_plane.plane_color,this_plane.plane_idx))
                                        self.player_planesOnFly.append(this_plane)
                                        self.player_planesOnWait.pop(0)
                                else:
                                    promptLine+='叫你皮^'
                            else:
                                promptLine+='叫你皮^'

                                
                                
                            
        self.player_regulatePosition() # 自身formatPosition位置坐标更新一下

        self.player_jump()
        # print('Now on fly:{}'.format(self.player_planesOnFly))
        # 这部分错误在于, 就算没有扔出6点一样可以放进planesOnFly
        # if not (this_plane in self.player_planesOnFly):  # 更新起飞列表
        #     self.player_planesOnFly.append(this_plane)
        #     print('Now on fly:{}'.format(self.player_planesOnFly))

    def printData(self):
        print(self.__dict__)
    
    def player_printPlane(self):
        for obj_plane in self.player_planesOnWait+self.player_planesOnFly:
            print(obj_plane.__dict__)

if __name__=='__main__':
    # for throwCnt in range(1,101):
    #     for color in ['r','y','b','g']:
    #         print('+++++++')
    #         pr=Player(color)
    #         print('第{}次掷色子!'.format(throwCnt),'现在你是{}方'.format(color))
    #         if pr.player_check_isHisTurn(throwCnt):
    #             print(pr.player_planesOnWait)
    #             pr.player_throwDice()
    #             if pr.player_diceNum==6:
    #                 pr.player_touch()
    #                 pr.printData()
    #                 pr.printPlane()
    #                 print('------')
    #             break
    #         else:
    #             continue

    pr=Player('b')
    for throwCnt in range(2,1003):
        if pr.player_check_isHisTurn(throwCnt):
            # print(pr.player_planesOnWait)
            pr.player_throwDice()
            pr.player_touch()
            # pr.player_checkFinish()
            # pr.player_checkWinner()
            pr.printData()
            pr.player_printPlane()
            print('------')
            if pr.player_checkWinner()==1:
                print('有人赢了, 大家散了吧')
                break
        else:
            continue




        



        

