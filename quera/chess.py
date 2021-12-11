king, queen, rook, bishop, knight, pawn = 1, 1, 2, 2, 2, 8
x = input()
WrongPieces = x.split()
CorrectPieces = []

CorrectPieces.append(king-int(WrongPieces[0]))
CorrectPieces.append(queen-int(WrongPieces[1]))
CorrectPieces.append(rook-int(WrongPieces[2]))
CorrectPieces.append(bishop-int(WrongPieces[3]))
CorrectPieces.append(knight-int(WrongPieces[4]))
CorrectPieces.append(pawn-int(WrongPieces[5]))
for i in CorrectPieces:
    print(i, end=' ')



