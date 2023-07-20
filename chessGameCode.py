import pygame

BoardRect = []
Selected = False
TURN = 0
selectedPiece = ""
pygame.init()
screenSize = (800, 800)
tileSize = screenSize[0]/8
clock = pygame.time.Clock()
root = pygame.display.set_mode(screenSize)
pygame.display.set_caption("___Chess___")

impImg = pygame.image.load(".\\res\\rect0.png")
board = [[(26, 26, 26), (204, 204, 204)], [(0, 0, 43), (170, 170, 255)], [(28, 36, 28), (170, 255, 170)], [
    (40, 11, 11), (255, 170, 170)], [(17, 0, 43), (204, 170, 255)], [(34, 11, 40), (238, 215, 244)]]

Colors = {"Black": (25, 25, 25), "White": (200, 200, 200)}
PieceNumber = 4
try:
    with open("perf.txt", "r") as file:
        BoardNumber = (file.readline())
        Colors["Black"] ,Colors["White"]  = board[int(BoardNumber[0])][0],board[int(BoardNumber[0])][1]
        PieceNumber = BoardNumber[1]
except:
    print("perf.txt not found !")

def printOn(message, color, x, y, size=18, Font=".\Grace.ttf"):
    font = pygame.font.Font(Font, size)
    mess = font.render(message, True, color, 2)
    root.blit(mess, (x, y))


class Pieces:
    def __init__(self, X, Y, Img, Id):
        self.Id = Id
        self.Img = Img
        self.rect = self.Img.get_rect()
        self.rect.x = X
        self.rect.y = Y

    def draw(self):
        root.blit(self.Img, (self.rect.x, self.rect.y))


class Player1:
    def __init__(self):
        ImgOfB = []
        ImgOfW = []
        for i in "RQBKHP":
            ImgOfB.append(pygame.image.load(f".\\res\\B{i}{PieceNumber}.png"))
            ImgOfW.append(pygame.image.load(f".\\res\\W{i}{PieceNumber}.png"))
        self.whitePlayer = {}
        self.blackPlayer = {}
        for i in range(8):
            self.whitePlayer[f"P{i}"] = Pieces(
                tileSize*i, tileSize*6, ImgOfW[-1], 1)
            self.blackPlayer[f"P{i}"] = Pieces(
                tileSize*i, tileSize, ImgOfB[-1], 1)
            if (i == 0) or (i == 7):
                self.blackPlayer[f"H{i}"] = Pieces(
                    tileSize*i, tileSize*0, ImgOfB[-2], 4)
                self.whitePlayer[f"H{i}"] = Pieces(
                    tileSize*i, tileSize*7, ImgOfW[-2], 4)
            if (i == 1) or (i == 6):
                self.blackPlayer[f"K{i}"] = Pieces(
                    tileSize*i, tileSize*0, ImgOfB[-3], 2)
                self.whitePlayer[f"K{i}"] = Pieces(
                    tileSize*i, tileSize*7, ImgOfW[-3], 2)
            if (i == 2) or (i == 5):
                self.blackPlayer[f"B{i}"] = Pieces(
                    tileSize*i, tileSize*0, ImgOfB[-4], 3)
                self.whitePlayer[f"B{i}"] = Pieces(
                    tileSize*i, tileSize*7, ImgOfW[-4], 3)
            if (i == 3):
                self.blackPlayer[f"Q{i}"] = Pieces(
                    tileSize*i, tileSize*0, ImgOfB[-5], 7)
                self.whitePlayer[f"Q{i}"] = Pieces(
                    tileSize*i, tileSize*7, ImgOfW[-5], 7)
            if (i == 4):
                self.blackPlayer[f"R{i}"] = Pieces(
                    tileSize*i, tileSize*0, ImgOfB[-6], 5)
                self.whitePlayer[f"R{i}"] = Pieces(
                    tileSize*i, tileSize*7, ImgOfW[-6], 5)

    def update(self):
        for i in self.whitePlayer.keys():
            self.whitePlayer[i].draw()
        for i in self.blackPlayer.keys():
            self.blackPlayer[i].draw()


class MovementOfPieces:
    def __init__(self, Piece, Board):
        self.piece = Piece
        self.board = Board
        self.legalRectsList = []

    def start(self):
        self.legalRectsList.clear()
        if self.piece.Id == 1:
            self.Pawn()
        elif self.piece.Id == 2:
            self.Knight()
        elif self.piece.Id == 3:
            self.Bishop()
        elif self.piece.Id == 4:
            self.Rook()
        elif self.piece.Id == 5:
            self.King()
        elif self.piece.Id == 7:
            self.Queen()

    def highlight(self):
        for rect in self.legalRectsList:
            root.blit(impImg, (rect.x, rect.y))

    def King(self):
        King_X = self.piece.rect.x + 50
        King_Y = self.piece.rect.y + 50
        spotToCheck = []
        for mode in range(4):
            x, y = King_X, King_Y
            if mode == 0:
                x += 100
                if (x <= 800):
                    if ((y) >= 0):
                        if self.collideChecker(x, y):
                            spotToCheck.append((x, y))
                    if ((y+100) <= 800):
                        if self.collideChecker(x, y+100):
                            spotToCheck.append((x, y+100))
                    if ((y-100) >= 0):
                        if self.collideChecker(x, y-100):
                            spotToCheck.append((x, y-100))
            elif mode == 1:
                y -= 100
                if (y > 0):
                    if ((x) <= 800):
                        if self.collideChecker(x, y):
                            spotToCheck.append((x, y))
            elif mode == 2:
                x -= 100
                if (x >= 0):
                    if ((y) >= 0):
                        if self.collideChecker(x, y):
                            spotToCheck.append((x, y))
                    if ((y+100) <= 800):
                        if self.collideChecker(x, y+100):
                            spotToCheck.append((x, y+100))
                    if ((y-100) >= 0):
                        if self.collideChecker(x, y-100):
                            spotToCheck.append((x, y-100))
            else:
                y += 100
                if (y <= 800):
                    if ((x) <= 800):
                        if self.collideChecker(x, y):
                            spotToCheck.append((x, y))

        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)

    def collideChecker(self, X, Y):
        for j in Player.blackPlayer.keys():
            if Player.blackPlayer[j].rect.collidepoint((X, Y)):
                if TURN == 1:
                    return True
                else:
                    return False
        else:
            for j in Player.whitePlayer.keys():
                if Player.whitePlayer[j].rect.collidepoint((X, Y)):
                    if TURN == 1:
                        return False
                    else:
                        return True
            else:
                return True

    def Knight(self):
        Knight_X = self.piece.rect.x + 50
        Knight_Y = self.piece.rect.y + 50
        spotToCheck = []
        for mode in range(4):
            x, y = Knight_X, Knight_Y
            if mode == 0:
                x += 200
                if (x <= 800):
                    if ((y+100) <= 800):
                        if self.collideChecker(x, y+100):
                            spotToCheck.append((x, y+100))
                    if ((y-100) >= 0):
                        if self.collideChecker(x, y-100):
                            spotToCheck.append((x, y-100))
            elif mode == 1:
                y -= 200
                if (y > 0):
                    if ((x+100) <= 800):
                        if self.collideChecker(x+100, y):
                            spotToCheck.append((x+100, y))
                    if ((x-100) >= 0):
                        if self.collideChecker(x-100, y):
                            spotToCheck.append((x-100, y))
            elif mode == 2:
                x -= 200
                if (x >= 0):
                    if ((y+100) <= 800):
                        if self.collideChecker(x, y+100):
                            spotToCheck.append((x, y+100))
                    if ((y-100) >= 0):
                        if self.collideChecker(x, y-100):
                            spotToCheck.append((x, y-100))
            else:
                y += 200
                if (y <= 800):
                    if ((x+100) <= 800):
                        if self.collideChecker(x+100, y):
                            spotToCheck.append((x+100, y))
                    if ((x-100) >= 0):
                        if self.collideChecker(x-100, y):
                            spotToCheck.append((x-100, y))

        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)

    def Bishop(self):
        BishX = self.piece.rect.x+50
        BishY = self.piece.rect.y+50
        spotToCheck = []
        for mode in range(4):
            checkLoop = True
            x, y = BishX, BishY
            while checkLoop:
                if mode == 0:
                    x -= 100
                    y -= 100
                elif mode == 1:
                    x += 100
                    y += 100
                elif mode == 2:
                    x += 100
                    y -= 100
                else:
                    x -= 100
                    y += 100
                if ((x <= 0) or (y <= 0) or (x >= 800) or (y >= 800)):
                    break
                for j in Player.blackPlayer.keys():
                    if Player.blackPlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                        else:
                            checkLoop = False
                            break
                for j in Player.whitePlayer.keys():
                    if Player.whitePlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            checkLoop = False
                            break
                        else:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                if checkLoop:
                    spotToCheck.append((x, y))
        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)

    def Rook(self):
        BishX = self.piece.rect.x+50
        BishY = self.piece.rect.y+50
        spotToCheck = []
        for mode in range(4):
            checkLoop = True
            x, y = BishX, BishY
            while checkLoop:
                if mode == 0:
                    x += 100
                elif mode == 1:
                    y -= 100
                elif mode == 2:
                    x -= 100
                else:
                    y += 100
                if ((x <= 0) or (y <= 0) or (x >= 800) or (y >= 800)):
                    break
                for j in Player.blackPlayer.keys():
                    if Player.blackPlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                        else:
                            checkLoop = False
                            break
                for j in Player.whitePlayer.keys():
                    if Player.whitePlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            checkLoop = False
                            break
                        else:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                if checkLoop:
                    spotToCheck.append((x, y))
        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)

    def Queen(self):
        Queen_X = self.piece.rect.x+50
        Queen_Y = self.piece.rect.y+50
        spotToCheck = []
        for mode in range(8):
            checkLoop = True
            x, y = Queen_X, Queen_Y
            while checkLoop:
                if mode == 0:
                    x += 100
                elif mode == 1:
                    y -= 100
                elif mode == 2:
                    x -= 100
                elif mode == 3:
                    y += 100
                elif mode == 4:
                    x -= 100
                    y -= 100
                elif mode == 5:
                    x += 100
                    y += 100
                elif mode == 6:
                    x += 100
                    y -= 100
                else:
                    x -= 100
                    y += 100
                if ((x <= 0) or (y <= 0) or (x >= 800) or (y >= 800)):
                    break
                for j in Player.blackPlayer.keys():
                    if Player.blackPlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                        else:
                            checkLoop = False
                            break
                for j in Player.whitePlayer.keys():
                    if Player.whitePlayer[j].rect.collidepoint((x, y)):
                        if TURN == 1:
                            checkLoop = False
                            break
                        else:
                            spotToCheck.append((x, y))
                            checkLoop = False
                            break
                if checkLoop:
                    spotToCheck.append((x, y))
        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)

    def Pawn(self):
        Pawn_X = self.piece.rect.x+50
        Pawn_Y = self.piece.rect.y+50
        if TURN == 1:
            if Pawn_Y < 100:
                self.piece.Id = 7
                self.piece.Img = Player.whitePlayer["Q3"].Img
                self.start()
        else:
            if Pawn_Y > 700:
                self.piece.Id = 7
                self.piece.Img = Player.blackPlayer["Q3"].Img
                self.start()

        spotToCheck = []
        if TURN == 1:  # white Pawn
            spotToCheck.append((Pawn_X, Pawn_Y-100))
            if Pawn_Y > 550:
                spotToCheck.append((Pawn_X, Pawn_Y-200))
            for key in Player.blackPlayer.keys():
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X+100, Pawn_Y-100)):
                    spotToCheck.append((Pawn_X+100, Pawn_Y-100))
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X-100, Pawn_Y-100)):
                    spotToCheck.append((Pawn_X-100, Pawn_Y-100))
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X, Pawn_Y-100)):
                    spotToCheck.remove((Pawn_X, Pawn_Y-100))
                    if (Pawn_X, Pawn_Y-200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y-200))
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X, Pawn_Y-200)):
                    if (Pawn_X, Pawn_Y-200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y-200))
            for key in Player.whitePlayer.keys():
                if Player.whitePlayer[key].rect.collidepoint((Pawn_X, Pawn_Y-100)):
                    if (Pawn_X, Pawn_Y-100) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y-100))
                    if (Pawn_X, Pawn_Y-200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y-200))
                if Player.whitePlayer[key].rect.collidepoint((Pawn_X, Pawn_Y-200)):
                    if (Pawn_X, Pawn_Y-200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y-200))
        else:
            spotToCheck.append((Pawn_X, Pawn_Y+100))
            if Pawn_Y < 200:
                spotToCheck.append((Pawn_X, Pawn_Y+200))
            for key in Player.whitePlayer.keys():
                if Player.whitePlayer[key].rect.collidepoint((Pawn_X+100, Pawn_Y+100)):
                    spotToCheck.append((Pawn_X+100, Pawn_Y+100))
                if Player.whitePlayer[key].rect.collidepoint((Pawn_X-100, Pawn_Y+100)):
                    spotToCheck.append((Pawn_X-100, Pawn_Y+100))
                if Player.whitePlayer[key].rect.collidepoint((Pawn_X, Pawn_Y+100)):
                    spotToCheck.remove((Pawn_X, Pawn_Y+100))
                    if (Pawn_X, Pawn_Y+200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y+200))
            for key in Player.blackPlayer.keys():
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X, Pawn_Y+100)):
                    if (Pawn_X, Pawn_Y+100) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y+100))
                    if (Pawn_X, Pawn_Y+200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y+200))
                if Player.blackPlayer[key].rect.collidepoint((Pawn_X, Pawn_Y+200)):
                    if (Pawn_X, Pawn_Y+200) in spotToCheck:
                        spotToCheck.remove((Pawn_X, Pawn_Y+200))

        for i in self.board:
            for j in spotToCheck:
                if i.collidepoint(j):
                    if i not in self.legalRectsList:
                        self.legalRectsList.append(i)
        


Player = Player1()
movementOfPieces = MovementOfPieces(None, None)


game_stoped = True                  # main game loop

while game_stoped:
    # background
    for i in range(8):
        for j in range(8):
            if (i % 2 == 0):
                if (j % 2 == 0):
                    Bcolor = Colors["White"]
                else:
                    Bcolor = Colors["Black"]
            else:
                if (j % 2 == 0):
                    Bcolor = Colors["Black"]
                else:
                    Bcolor = Colors["White"]
            tempRect = pygame.Rect(tileSize*j, tileSize*i, tileSize, tileSize)
            BoardRect.append(tempRect)
            pygame.draw.rect(root, Bcolor, tempRect)
    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_stoped = False
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                Selected = False
                if TURN == 1:
                    TURN == 0
                else:
                    TURN == 1
                selectedPiece.rect.x = tempx
                selectedPiece.rect.y = tempy
        if event.type == pygame.MOUSEBUTTONDOWN:
            if any(pygame.mouse.get_pressed()):
                if not Selected:
                    if TURN == 0:
                        for i in Player.whitePlayer.keys():
                            if Player.whitePlayer[i].rect.collidepoint(pygame.mouse.get_pos()):
                                selectedPiece = Player.whitePlayer[i]
                                Selected = True
                                TURN = 1
                    else:
                        for i in Player.blackPlayer.keys():
                            if Player.blackPlayer[i].rect.collidepoint(pygame.mouse.get_pos()):
                                selectedPiece = Player.blackPlayer[i]
                                Selected = True
                                TURN = 0
                    tempx = selectedPiece.rect.x
                    tempy = selectedPiece.rect.y
                    movementOfPieces.piece = selectedPiece
                    movementOfPieces.board = BoardRect
                    movementOfPieces.start()

                if Selected:
                    for i in movementOfPieces.legalRectsList:
                        if i.collidepoint(pygame.mouse.get_pos()):
                            if selectedPiece.rect.x != i.x and selectedPiece.rect.y != i.y:
                                selectedPiece.rect.x, selectedPiece.rect.y = i.x, i.y
                                Selected = False
                                if (TURN == 1):
                                    for i in Player.blackPlayer.keys():
                                        if Player.blackPlayer[i].rect.colliderect(selectedPiece.rect):
                                            Player.blackPlayer[i].rect.x = 825
                                else:
                                    for i in Player.whitePlayer.keys():
                                        if Player.whitePlayer[i].rect.colliderect(selectedPiece.rect):
                                            Player.whitePlayer[i].rect.x = 825

    # highlighted blocks
    if Selected:
        selectedPiece.rect.x, selectedPiece.rect.y = (
            pygame.mouse.get_pos()[0] - 50), (pygame.mouse.get_pos()[1] - 50)
        movementOfPieces.highlight()

    Player.update()

    pygame.display.update()
    clock.tick(60)


pygame.quit()
