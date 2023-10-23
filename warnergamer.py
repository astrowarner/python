class Player(object):
    def__init__(self, ip, name):
        self.ip = ip 
        self.name = name 
        self.score = 0 
        
    def update_score(self, x):
        self.score += x 
    def guess(self, string):
        pass
    def disconnect(self):
        pass
    def get_ip(self):
        return self.ip 
    def get_name(self):
        return self.name 
    def get_score(self):
        return self.score 
    
    
    
class Board(object): #grid based/ pixel system 
    ROWS = COLS = 720 #for every row there is a clumn 
    def __init__(self):
        self.data = self._create_empty_board()
    def update(self, x, y, color):
        self.data[x][y] = color 
    def clear (self):
        
    def _create_empty_board(self):
        return [(255,255,255) for _ in range (self.ROWS)]
    def fill(self, x, y):
        
    def get_board(self):
        return self.data 
    
class Chat(object):
    def __intit__(self):
        self.content = []
        
    def update_chat(self, msg):
        self.content.append(msg)
    def get_chat(self):
        return self.content 
    
    def __len__(self):
        return len(self.content)
    
    def__str(self):
        return "".join(self.content)
    
    def __repr(self);
    return str(self)


class Round(object):
    def __intit__(self, word, player_drawing, players):
        self.word = word 
        self.player_drawing = player_drawing 
        self.player_guessed = []
        self.skips = 0 
        self.player_scores = {player:0 for player in players}
        self.time - 75 
        
    def guess(self, player, wrd):
        correct = wrd == self.word 
        if correct: 
            self.player_guessed.append(player)
        return wrd == self.wrd 
    
    def player_left(self, player):
        if player in self.player_scores
            del player_scores[player]
        if player in player_guessed:
            self.player_guessed.remove(player)
        if player == self.plaer_drawinf:
            self.end_round()
                
    def end_round(self):
        pass  
        
        
        
    
    
    
    
        
        
        