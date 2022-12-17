from collections import namedtuple
import random

Nimply = namedtuple("Nimply", "row, num_objects")

class Nim:
    def __init__(self, num_rows: int, k: int = None) -> None:
        self._rows = [2*i + 1 for i in range(num_rows)]
        self._k = k
        self._turn = 0
        
    def fromRows(self, rows):
        self._rows = [*rows]
        return self

    def nimming(self, ply:Nimply) -> None:
        if ply is None:
            self._rows=[0 for _ in self._rows]
            return
        row, num_objects=ply
        assert num_objects>0
        assert self._rows[row] >= num_objects
        assert self._k is None or num_objects <= self._k
        self._rows[row] -= num_objects
        self._turn = 1 - self._turn
        
        if self._rows[row]==0:
            self._rows.pop(row)

    def __bool__(self):
        return sum(self._rows) > 0
    
    def __str__(self):
        return "<" + " ".join(str(_) for _ in self._rows) + ">"
    
    @property
    def rows(self) -> tuple:
        return tuple(self._rows)
    
    @property
    def k(self) -> int:
        return self._k
    
    @property
    def turn(self) -> int:
        return self._turn

    def endTest(self):
        if sum(self._rows) == 0:
            return 1
        return 0

    def board(self)->None:
        for i,row in enumerate(self._rows):
            print(i,":",end=" ")
            for j in range(row):
                print("|", end=' ')
            print("\n")
            
    def get_reward(self):
        reward = -1
        if self.endTest():
            if self._turn == 0:
                reward = 1
            else:
                reward = -2
        return reward

def nimSum(rows):
    sum=rows[0]
    for i in rows[1:]:
        sum^=i
    return sum

def checkMisere(rows):
    cnt=0
    nonOneRow=-1
    for i,row in enumerate(rows):
        if row>=2:
            cnt+=1
            nonOneRow=i
        if cnt==2:
            return -1
    return nonOneRow

def pure_random(state: Nim) -> Nimply:
    row = random.choice([r for r, c in enumerate(state.rows) if c > 0])
    num_objects = random.randint(1, state.rows[row])
    return Nimply(row, num_objects)

def dumb(state: Nim) -> Nimply:
    possible_moves = [(r, o) for r, c in enumerate(state.rows) for o in range(1, c + 1)]
    return Nimply(*max(possible_moves, key=lambda m: (-m[0], m[1])))

def expert(game):
    rows=game.rows
    totNimSum=nimSum(rows)
    if(totNimSum!=0):
        OneRow=checkMisere(rows)
        if OneRow!=-1:
            if len([_ for _ in rows if _!=0])%2==0:
                return Nimply(OneRow,rows[OneRow])
            else:
                return Nimply(OneRow, rows[OneRow]-1)
        for i,row in enumerate(rows):
            lineNimSum=nimSum([totNimSum,row])
            if(lineNimSum<row):
                return Nimply(i,row-lineNimSum)
    return pure_random(game)

def human_play(game) -> Nimply:
    while 1:
        str=input("Enter row index and number of elements to remove: ")
        rowIdx, n=str.split(" ")
        if int(rowIdx)>=len(game.rows):
            print("Invalid row!")
        elif int(n)>game.rows[int(rowIdx)]:
            print("Invalid number, convert to maximum!")
            n=game.rows[int(rowIdx)]
            return Nimply(int(rowIdx), int(n))
        else:
            return Nimply(int(rowIdx),int(n))
        
def lose_game() -> Nimply:
    return None

def sandbox(game: Nim, agent):
    print("Format: #row #amount")
    game.board()
    turn=1
    while not game.endTest():
        turn = 1 - turn
        if not turn:
            print("Your turn:")
            game.nimming(human_play(game))
        else:
            print("Agent's turn:")
            game.nimming(agent(game))
        game.board()
    if not turn:
        print("You lost")
    else:
        print("Agent lost")
        
def evaluate(gamesize: int,agent,prob:float,eval_amount:int) -> float:
    win_count = 0
    for _ in range(eval_amount):
        game = Nim(gamesize)
        turn=1   #inizia l'individuo turno 0, random turno 1
        while not game.endTest():
            turn = 1 - turn
            if not turn:
                game.nimming(agent(game))
            else:
                if random.random() < prob:
                    game.nimming(expert(game))
                else:
                    game.nimming(pure_random(game))
        if turn:   #gioco finito e ultima mossa di random
            win_count += 1
    return win_count/eval_amount