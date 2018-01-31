while True:
	response = input('What is your question? ')
	
	if response.strip() == 'quit':
		exit(1)
	if response.strip()[-1] != '?':
		print('Sorry, I can only answer questions.')
		continue




