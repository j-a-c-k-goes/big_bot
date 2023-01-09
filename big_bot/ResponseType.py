import random
class Affirmation:
	affirmations = [
	'You are capable of achieving anything you set your mind to.',
	'You are worthy of love and respect.',
	'You are strong and capable.',
	'You are talented and capable of great things.',
	'You are deserving of happiness and success.'
	]

	uncertainties = [
	'say everything triple times. `!BIGBIGBIG`',
	'everythin is fine, go !big',
	'`did you know?` you can type `BIGBIGBIG` to activate !bigbot',
	]
	def __init__(self):
		pass
	def positive(self):
		return random.choice(self.affirmations)
	def uncertain(self):
		return random.choice(self.uncertainties)
	def forgetting_punctuation(self):
		return('`warning: if you are trying to activate !bigbot, yuo have to include the "!"` ')
