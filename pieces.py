class GamePiece:
    def __init__(self, name, symbol, row, col):
        self.name = name
        self.symbol = symbol
        self.pos = [row, col]

    def draw(self):
        print(self.symbol, end=' ')


class Pawn(GamePiece):
    def __init__(self, row, col, name="Pawn", symbol="P"):
        super().__init__(name, symbol, row, col)


class Knight(GamePiece):
    def __init__(self, row, col, name="Knight", symbol="N"):
        super().__init__(name, symbol, row, col)


class Bishop(GamePiece):
    def __init__(self, row, col, name="Bishop", symbol="B"):
        super().__init__(name, symbol, row, col)


class Rook(GamePiece):
    def __init__(self, row, col, name="Rook", symbol="R"):
        super().__init__(name, symbol, row, col)


class Queen(GamePiece):
    def __init__(self, row, col, name="Queen", symbol="Q"):
        super().__init__(name, symbol, row, col)


class King(GamePiece):
    def __init__(self, row, col, name="King", symbol="K"):
        super().__init__(name, symbol, row, col)


class Monster(GamePiece):
    def __init__(self, row, col, name="Monster", symbol="M"):
        super().__init__(name, symbol, row, col)

