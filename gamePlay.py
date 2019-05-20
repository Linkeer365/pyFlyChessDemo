import chessBoard
import grid
import player
import plane
import positionsColorsMapping
import rawIdx2formatIdx
import rawPosition2formatPosition
import throwDice

def one_player_play(player_color):
    pr=Player(player_color)
    for throwCnt in range(2,1003):
        if pr.player_check_isHisTurn(throwCnt):
            # print(pr.player_planesOnWait)
            pr.player_throwDice()
            pr.player_touch()
            pr.player_checkFinish()
            pr.player_checkWinner()
            # pr.printData()
            # pr.player_printPlane()
            print('------')
            if pr.player_checkWinner()==1:
                print('我赢了, 大家散了吧')
                break
        else:
            continue

def four_players_play(player_colors):
    players=[]
    for pr_color in player_colors:
        players.append(player.Player(pr_color))
    for throwCnt in range(1,1003):
        print('Round-{}\tTurn-{}'.format(throwCnt//4+1,throwCnt))
        for pr in players:
            if pr.player_check_isHisTurn(throwCnt):
                pr.player_throwDice()
                pr.player_touch()
                pr.player_checkFinish()
                pr.printData()
                pr.player_printPlane()
                if pr.player_checkWinner():
                    winnerLine='玩家{}赢了, 大家散了吧'.format(pr.player_color)
                    break
            else:
                continue
        if pr.player_checkWinner():        
            print(winnerLine)
            break

    


four_players_play(['r','y','b','g'])
        

