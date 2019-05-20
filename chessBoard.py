import grid

class ChessBoard:
    def __init__(self):
        self.grids=[grid.Grid(grid_color=['r','y','b','g'][(each_idx%4)-1],grid_rawIdx=each_idx) for each_idx in range(1,100)]
    def printData(self):
        for each in self.grids:
            print(each.__dict__)
if __name__=='__main__':
    cb=ChessBoard()
    cb.printData()