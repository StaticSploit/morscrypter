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
			cryptedtext = cryptedtext + ".-" + "x"
		if(letter == "b"):
			cryptedtext = cryptedtext + "-..." + "x"
		if(letter == "c"):
			cryptedtext = cryptedtext + "-.-." + "x"
		if(letter == "d"):
			cryptedtext = cryptedtext + "-.." + "x"
		if(letter == "e"):
			cryptedtext = cryptedtext + "." + "x"
		if(letter == "f"):
			cryptedtext = cryptedtext + "..-." + "x"
		if(letter == "g"):
			cryptedtext = cryptedtext + "--." + "x"
		if(letter == "h"):
			cryptedtext = cryptedtext + "...." + "x"
		if(letter == "i"):
			cryptedtext = cryptedtext + ".." + "x"
		if(letter == "j"):
			cryptedtext = cryptedtext + ".---" + "x"
		if(letter == "k"):
			cryptedtext = cryptedtext + "-.-" + "x"
		if(letter == "l"):
			cryptedtext = cryptedtext + ".-.." + "x"
		if(letter == "m"):
			cryptedtext = cryptedtext + "--" + "x"
		if(letter == "n"):
			cryptedtext = cryptedtext + "-." + "x"
		if(letter == "o"):
			cryptedtext = cryptedtext + "---" + "x"
		if(letter == "p"):
			cryptedtext = cryptedtext + ".--." + "x"
		if(letter == "r"):
			cryptedtext = cryptedtext + ".-." + "x"
		if(letter == "s"):
			cryptedtext = cryptedtext + "..." + "x"
		if(letter == "t"):
			cryptedtext = cryptedtext + "-" + "x"
		if(letter == "u"):
			cryptedtext = cryptedtext + "..-" + "x"
		if(letter == "v"):
			cryptedtext = cryptedtext + "...-" + "x"
		if(letter == "y"):
			cryptedtext = cryptedtext + "-.--" + "x"
		if(letter == "z"):
			cryptedtext = cryptedtext + "--.." + "x"

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
		
		
		
		
		
