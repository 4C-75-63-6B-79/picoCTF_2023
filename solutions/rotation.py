# rotates a single letter
def rotAlpha(alpha, key, start):
	return chr(start + ((ord(alpha) - start + key)%26))

# rotates and returns the entire word as string
def rotateWord(word, key):
	rotatedWord = ''
	for i in word:
		if 65 <= ord(i) <= 90:
			rotatedWord += rotAlpha(i, key, 65)
		elif 97 <= ord(i) <= 122:
			rotatedWord += rotAlpha(i, key, 97)
		else:
			rotatedWord += i
	return(rotatedWord)
	
	
def printAllCipher(word):
	for i in range(26):
		print("key:", i, rotateWord(word, i))

word = ''
print('Enter 0 to end the program.')

# loops take input until user enter 0
while not (word == '0'):
	word = input('Enter word to be deciphered: ')
	if(word == '0'):
		print('program exit');
		break
	printAllCipher(word)