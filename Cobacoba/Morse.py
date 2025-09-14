kodeMorse = {
"a" : ".-/", 
"b" : "-.../", 
"c" : "-.-./", 
"d" : "-../", 
"e" : "./", 
"f" : "..-./", 
"g" : "--./", 
"h" : "..../", 
"j" : ".---/", 
"i" : "../", 
"k" : "-.-/", 
"l" : ".-../", 
"m" : "--/", 
"n" : "-./", 
"o" : "---/", 
"p" : ".--./", 
"q" : "--.-/", 
"r" : ".-./", 
"s" : ".../", 
"t" : "-/", 
"u" : "..-/", 
"v" : "...-/", 
"w" : ".--/", 
"x" : "-..-/", 
"y" : "-.--/", 
"z" : "--../", 
" " : "//", 
"." : ".-.-.-/", 
"," : "--..--/", 
":" :"---.../", 
"-" : "-....-/", 
"/" : "-..-./",
"?" : "..--../",
'"' : '.-..-./'
}
while True:
 inputUser = input("Masukkan teks : ")
 encrypted = ""

 for char in inputUser:
   lowerChar = char.lower()
   if lowerChar in kodeMorse:
     encrypted += kodeMorse[lowerChar]
   else:
    encrypted += char
    
 print("Kode Morse : ", encrypted)
