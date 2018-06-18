from number import Number

sb = Number()

def new_game(d):
	try:
		max1 = int(d.get('max1', [''])[0])
	except:
		return {'code' : 'error', 'msg' : 'max is not given'}

	sb.newGame(max1)

	return {'code': 'success'}


def guess(d):
	try:
		guess = d.get('guess', [''])[0]
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	ss = sb.guess(guess)
	trials = sb.getGuessCount()

	return {'code': 'success', 'Answer':ss, 'trials': trials}
