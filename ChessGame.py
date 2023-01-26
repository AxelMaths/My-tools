

class ChessGameBoard:
    """
    A class to implement a board of the chess game 
    """
    def __init__(self,listChessSoldiers):
        self.listChessSoldiers = listChessSoldiers
    
class ChessGame:
    def __init__(self,mode="default"):
        pass
    
    @staticmethod # méthode de la classe, on peut appeler la méthode sans instancier
    def h():
        """
        Display some informations
        """
        print("To play chessGame, we need two players") 

class ChessSoldier:
    
    # class attribut, accessibles sans instanciation
    names = ("Pion","Tour","Fou", "Cavalier","Reine","Roi")
    
    def __init__(self, position_x, position_y, color):
        self.position_x = position_x
        self.position_y = position_y
        self.color = color
    
    def move(self, new_position_x, new_position_y):
        pass
    
class TowerSoldier(ChessSoldier):
    
    def __init__(self, position_x, position_y, color):
        super().__init__(position_x, position_y, color)

    def move(self, new_position_x, new_position_y):
        if self.position_x == new_position_x or self.position_y == new_position_y:
            


        



