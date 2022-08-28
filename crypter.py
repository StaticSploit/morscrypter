# her harften sonra arada boşluk kalması için x kullandık

def cryptingwithmors(text):
	#aslında algoritma çok basit önce cryptedtext diye bir değişken oluşturuyoruz
	#sonra da fonksiyon kullanılırken verilen text argumanındaki harfleri teker teker 
	#okuyan bir for döngüsü yazıp harfleri teker teker mors alfabesine dönüştürüyoruz
	# tabi her seferinde harfler büyük ise bile bunu .lower() fonksiyonu ile küçültüyoruz
	cryptedtext = ""
	for letter in text:
		letter = letter.lower()
		if(letter == "a"):
			cryptedtext = cryptedtext + ".-" + " "
		if(letter == "b"):
			cryptedtext = cryptedtext + "-..." + " "
		if(letter == "c"):
			cryptedtext = cryptedtext + "-.-." + " "
		if(letter == "d"):
			cryptedtext = cryptedtext + "-.." + " "
		if(letter == "e"):
			cryptedtext = cryptedtext + "." + " "
		if(letter == "f"):
			cryptedtext = cryptedtext + "..-." + " "
		if(letter == "g"):
			cryptedtext = cryptedtext + "--." + " "
		if(letter == "h"):
			cryptedtext = cryptedtext + "...." + " "
		if(letter == "i"):
			cryptedtext = cryptedtext + ".." + " "
		if(letter == "j"):
			cryptedtext = cryptedtext + ".---" + " "
		if(letter == "k"):
			cryptedtext = cryptedtext + "-.-" + " "
		if(letter == "l"):
			cryptedtext = cryptedtext + ".-.." + " "
		if(letter == "m"):
			cryptedtext = cryptedtext + "--" + " "
		if(letter == "n"):
			cryptedtext = cryptedtext + "-." + " "
		if(letter == "o"):
			cryptedtext = cryptedtext + "---" + " "
		if(letter == "p"):
			cryptedtext = cryptedtext + ".--." + " "
		if(letter == "r"):
			cryptedtext = cryptedtext + ".-." + " "
		if(letter == "s"):
			cryptedtext = cryptedtext + "..." + " "
		if(letter == "t"):
			cryptedtext = cryptedtext + "-" + " "
		if(letter == "u"):
			cryptedtext = cryptedtext + "..-" + " "
		if(letter == "v"):
			cryptedtext = cryptedtext + "...-" + " "
		if(letter == "y"):
			cryptedtext = cryptedtext + "-.--" + " "
		if(letter == "z"):
			cryptedtext = cryptedtext + "--.." + " "

	print(cryptedtext)

def anamenu(): # ana menümüzün fonksiyonu burada eğer kullanıcı bir girerse direkt verilen metin mors alfabesi ile yazılacak eğer iki girilirse verilen dosyadan okunanlar ile işlem yapılacak
	print("hello,")
	print("do you want to enter a text(enter 1 for that) or a file name(enter 2 for that)")
	answer = input(">")
	print("\n\n")
	if(answer == "1"):
		text = input("your text >")
		cryptingwithmors(text)
	elif(answer == "2"):
		fname = input("your text file >")
		fname = open(fname, "r")
		for linex in fname:
			cryptingwithmors(linex)
		
		
		
		
		
