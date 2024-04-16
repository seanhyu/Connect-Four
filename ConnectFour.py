class connectFour():
    def __init__(self,rows,cols):
        self.board = [[" "]*cols for _ in range(rows)]
        self.cols = [0] * cols
        self.rows = rows

    def boardMover(self, col, player):

        marker = "X" if player else "O"
        row = self.cols[col]
        self.cols[col] += 1
        self.board[row][col] = marker
        return self.resultChecker( row, col)

    def userInput(self,player):

        answered = False
        while not answered:
            try:
                userCol = input("Enter the column number you would like to place your piece in: ")
                col = int(userCol)
            except:
                print("Invalid input, try again!")
            else:
                if 0 <= col < len(self.cols) and self.cols[col] < self.rows:
                    answered = True
                else:
                    print("Invalid column, try again!")
        return self.boardMover(col,player)


    def resultChecker(self,row,col):
        marker = self.board[row][col]
        def valid(row,col):
            return 0 <= row < self.rows and 0 <= col < len(self.cols)
        def dfs(x,y,dx,dy):
            if not valid(x,y) or self.board[x][y] != marker:
                return 0
            return dfs(x+dx,y+dy,dx,dy) + 1

        for dx,dy in [(0,1),(1,0),(1,1),(1,-1)]:
            streak = dfs(row+dx,col+dy,dx,dy) + 1 + dfs(row-dx,col-dy,-dx,-dy)
            if streak >= 4:
                return True
        return False

    def boardPrinter(self):
        for row in reversed(self.board):
            print(row)
    def main(self):
        player = 1
        winner = False
        while (sum(self.cols)) < (self.rows * len(self.cols)):
            if player:
                print("Player One's Turn!")
                self.boardPrinter()
                result = self.userInput(player)
                if result:
                    print("Player 1 wins!")
                    winner = True
                    break
                else:
                    player = 0
            else:
                print("Player Two's Turn!")
                self.boardPrinter()
                result = self.userInput(player)
                if result:
                    print("Player 2 wins!")
                    winner = True
                    break
                else:
                    player = 1

        if not winner:
            print("You guys tied!")

        print("Game finished!")

        self.boardPrinter()
def getUserInput(type):

    answered = False
    while not answered:
        userNum = input("Enter the number of " + type + " that you want: ")
        try:
            num = int(userNum)
        except:
            print("Invalid input!")
        else:
            if num < 4:
                print("Invalid number!")
            else:
                answered = True
    return num

print("Welcome to Connect 4!")
rows = getUserInput("rows")
cols = getUserInput("columns")
game = connectFour(rows,cols)
game.main()





