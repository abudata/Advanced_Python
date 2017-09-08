import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
# For more information about how namedtuple can be used, you can read
#https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python
class FrenchDeck:
	ranks = [str(n) for n in range(2, 11)] + list('JQKA')
	suits = 'spades diamonds clubs hearts'.split()

	def __init__(self):
		self._cards = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]

	def __len__(self):
		return len(self._cards)

	def __getitem__(self, position):
		return self._cards[position]




beer_card = Card('7', 'diamonds')
print(beer_card)

print('This is how to use the FrenchDeck class')

deck = FrenchDeck()
print(len(deck))

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

print([Card(rank, suit) for suit in suits for rank in ranks])