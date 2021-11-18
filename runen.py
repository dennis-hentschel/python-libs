skip = 0
au = True

def get_word(context, pos):
	found = False
	check_pos = pos
	while not found:
		check_pos += 1
		if context[check_pos] == " ":
			found = True
			end_pos = check_pos
	check_pos = pos
	found = False
	while not found:
		check_pos -= 1
		if context[check_pos] == " ":
			found = True
			start_pos = check_pos + 1
	output = ""
	for i in range(end_pos - start_pos):
		output += context[i + start_pos]
	return (start_pos, output)

def ask(context, i, sug, oth):
	global au
	if not au: return sug
	other = ""
	for x in range(len(oth)):
		other += " or " + oth[x] + "(" + str(x+1) + ")"
	w = get_word(context, i)
	word = str(w[1])
	start_word = w[0]
	letter_pos = i - start_word + 1
	ask_txt = "Would you like to use \"" + str(sug) + "\"(0)" + str(other) + " in " + word + "[" + str(letter_pos) + "]? (" + str(sug) + ")"
	ans = input(ask_txt)
	if str(ans) == "" or str(ans) == "0": return sug
	while int(ans) > len(oth):
		ans = input("Invalid Input!\n" + ask_txt)
	return oth[ans-1]

def e(i, input):
	global skip
	if input[i] != "E": return -1
	if input[i+1] in ["I", "Y", "J"]:
		sug = "ᛇ"
		oth = ["ᛖ"]
	else:
	    sug = "ᛖ"
	    oth = ["ᛇ"]
	final = ask(input, i, sug, oth)
	if final == "ᛇ" and sug == "ᛇ": skip = 1
	return final

def q(i, input):#TODO
	return

def v(i, input):#TODO
	return

def ï(i, input):#TODO
	return

def ë(i, input):#TODO
	return

def num(i,input):#TODO
	return

def translate_l_to_r(input, ask_user=True, latin_numbers=False, german_replacement=True):
	global au
	global skip
	output = []
	au = ask_user
	input = list(input.upper())
	input.append(' ')

	for i in range(0,len(input)):
		
		if skip == 0:

			switch={
				"A":"ᚨ",
				"B":"ᛒ",
				"C":"ᚲ",
				"D":"ᛞ",
				"E":e(i,input),
				"F":"ᚠ",
				"G":"ᚷ",
				"H":"ᚺ",
				"I":"ᛁ",
				"J":"ᛃ",
				"K":"ᚲ",
				"L":"ᛚ",
				"M":"ᛗ",
				"N":"ᚾ",
				"O":"ᛟ",
				"P":"ᛈ",
				"Q":q(i,input),
				"R":"ᚱ",
				"S":"ᛊ",
				"T":"ᛏ",
				"U":"ᚢ",
				"V":v(i,input),
				"W":"ᚹ",
				"X":"ᚲᛊ",
				"Y":"ᛃ",
				"Z":"ᛉ",
				"Ä":"ᚨᛖ",#TODO
				"Ö":"ᛟᛖ",#TODO
				"Ü":"ᚢᛖ",#TODO
				"Ñ":"ᚾᛃ",
				"Ò":"ᛟ",
				"Ó":"ᛟ",
				"Ô":"ᛟ",
				"È":"ᛖ",
				"É":"ᛖ",
				"Ê":"ᛖ",
				"Ë":ë(i,input),
				"À":"ᚨ",
				"Á":"ᚨ",
				"Â":"ᚨ",
				"Ì":"ᛁ",
				"Í":"ᛁ",
				"Î":"ᛁ",
				"Ï":ï(i,input),
				"Ù":"ᚢ",
				"Ú":"ᚢ",
				"Û":"ᚢ",
				"":""#TODO
			}
			output.append(switch.get(input[i], input[i]))
		else:
			skip -= 1

	output.pop()
	final = "".join(output)
	return(final)
