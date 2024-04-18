import os 
import subprocess


#créer le txt contenant 100 lignes  3 avec guessing_number de rentrer

def create_var(guessing_number):
	result_list = []
	for i in range(0,50):
		process = subprocess.Popen("nc challenges.hackday.fr 50395", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)	
		# Envoyer des données d'entrée
		process.stdin.write(guessing_number)
		process.stdin.flush()
		# Récupérer la sortie et les erreurs
		sortie, erreur = process.communicate()
		result_list.append(sortie.split("\n")[2])
	return result_list

#fonction qui prend en parametre une liste de code chiffrer et qui renvoie le claire:
def list_to_decode(list_encoded):
	decode_msg = ''
	for index in range(0,len(list_encoded[0])):
		letters_list = []
		for words in list_encoded:
			letters_list.append(words[index])
		final_letter = sorted(list(set(letters_list)))
		letter = final_letter[1]
		decode_msg = decode_msg + str(letter)
	return decode_msg
	
print(list_to_decode(create_var("42")))

#fonction qui brutfort tout les nombre 
def main():
	wait_var = "wait"
	n = 0
	while(wait_var == "wait"):
		if(list_to_decode(create_var(str(n))) == "No no no, this is not the good number !"):
			n = n + 1
			print("NOPE: " + str(n))
		else:
			wait_var = "done"
	print("TROUVé pour n=" + str(n))

main()
