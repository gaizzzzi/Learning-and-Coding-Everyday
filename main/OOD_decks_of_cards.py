# 54 cards
# design class represent all 54 cards
# design class dealer to deal cards to player 1 and player 2
class card:
	def __init__(self, num, color):
		self.num = num
		self.color = color

class deck:
	def __init__(self):
		self.storage = []
		for color in ["spade", "heart", "club", "diamond"]:
			for i in range(1, 14):
				self.storage.append(card(i, color))
		self.storage.extend([card(14, "joker"), card(15, "joker")])

class player:
	def __init__(self, name, cards):
      	self.name = name
      	self.cards = cards

class dealer(player):
	def __init__(self, name, cards):
      	self.name = name
        self.cards = cards

	def shutil_deck(self):
		randomsampling(self.cards)
	
	def deal_card(self):
		return self.cards.pop()

class game:
	def __init__(self):
		self.dealer = dealer("lwb", deck().storage)
		self.player1 = player("player1", [])
		self.player2 = player("player2", [])
        self.result = None
    def compare(card0, card1):
      	...
        ...
        ...
        
	def run(self):
		while (self.result is None or self.result == "DRAW" or self.dealer.cards):
            # deal stage
            self.player1.cards.append(self.dealer.deal_card())
            self.player2.cards.append(self.dealer.deal_card())
            # check results
            curr_res = compare(self.player1.cards[-1], self.player2.cards[-1])
            if curr_res > 0:
                self.result = "player1 WIN"
            elif curr_res < 0:
          	    self.result = "player2 WIN"
            else:
          	    self.result = "DRAW"
          
          
          
          
          
          
          
          
          
          