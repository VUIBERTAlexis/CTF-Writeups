import os
import subprocess

def call_fonction():
process = subprocess.Popen("nc challenges.hackday.fr 50393", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

for i in range(3):
	next_line = process.stdout.readline()
	charset = str(next_line.split(" ")[2].replace("\\n", ""))
	print(next_line, end='')
	next_line = process.stdout.readline()
	size = int(next_line.split(" ")[2])
	print(next_line, end='')


	good_letters = ''
	#trouver les bonnes lettres
	for letter in charset:
		process.stdin.write(letter * size)
		process.stdin.flush()
		print(">>> " + letter * size)

		next_line = process.stdout.readline()
		number_of_letter_in_pass = next_line.split(" ")[1]
		good_letters = good_letters + letter * int(number_of_letter_in_pass)
		print(next_line, end='')

	black_letter = list(set(charset) - set(good_letters))[0]
	#trouver le bon code

	SOLUTION = ''
	for indice in range(size):
		for letter in good_letters:
			temp = [black_letter] * size
			temp[indice] = letter
			word_to_test = "".join(temp)
			process.stdin.write(word_to_test)
			process.stdin.flush()
			print(">>> " + word_to_test)

			next_line = process.stdout.readline()
			if(next_line.split(" ")[1] == "1"):
				SOLUTION = SOLUTION + letter
				break
			print(next_line, end='')

	process.stdin.write(SOLUTION)
	process.stdin.flush()


	next_line = process.stdout.readline()
	print(next_line, end='')
	next_line = process.stdout.readline()
	print(next_line, end='')

next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')
next_line = process.stdout.readline()
print(next_line, end='')

call_fonction()
