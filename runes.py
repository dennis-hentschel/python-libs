skip = 0
au = True
gr = True
asked_e = False
answer_e = ""

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
	if str(ans) == "" or str(ans) == "0": return sug
	return oth[int(ans)-1]

def e(i, input):
	global skip
	global answer_e
	global asked_e
	if input[i] != "E": return -1
	if asked_e: return str(answer_e)
	if input[i+1] in ["I", "Y", "J"]:
		sug = "ᛇ"
		oth = ["ᛖ"]
	else:
	    sug = "ᛖ"
	    oth = ["ᛇ"]
	final = ask(input, i, sug, oth)
	if final == "ᛇ" and sug == "ᛇ": skip = 1
	asked_e = True
	answer_e = final
	return final

def ae():
	global gr
	if gr: return "ᚨᛖ"
	else: return "ᚨ"

def oe():
	global gr
	if gr: return "ᛟᛖ"
	else: return "ᛟ"

def ue():
	global gr
	if gr: return "ᚢᛖ"
	else: return "ᚢ"

def q(i, input):
	if input[i] != "Q": return -1
	if input[i+1] == "U": return "ᚲ"
	else: return "ᚲᚢ"

def v(i, input):
	if input[i] != "V": return -1
	return ask(input,i,"ᚠ",["ᚢ"])

def jy(i,input):
	if input[i] =! "J" and input[i] != "Y": return -1
	if input[i] == "J": return ask(input,i,"ᛋ","ᛃ")
	else: return ask(input,i,"ᛋ","ᛃ")

def translate(input, ask_user=True, german_replacement=True):
	global au
	global answer_e
	global asked_e
	global gr
	global skip
	output = []
	au = ask_user
	gr = german_replacement
	ln = latin_numbers
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
				"J":jy(i,input),
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
				"Y":jy(i,input),
				"Z":"ᛉ",
				"Ä":ae(),
				"Ö":oe(),
				"Ü":ue(),
				"Ñ":"ᚾᛃ",
				"Ò":"ᛟ",
				"Ó":"ᛟ",
				"Ô":"ᛟ",
				"È":e(i,input),
				"É":e(i,input),
				"Ê":e(i,input),
				"Ë":e(i,input),
				"À":"ᚨ",
				"Á":"ᚨ",
				"Â":"ᚨ",
				"Ì":"ᛁ",
				"Í":"ᛁ",
				"Î":"ᛁ",
				"Ï":"ᛁ",
				"Ù":"ᚢ",
				"Ú":"ᚢ",
				"Û":"ᚢ",
				"":""
			}
			asked_e = False
			output.append(switch.get(input[i], input[i]))
		else:
			skip -= 1

	output.pop()
	print(str(output))
	final = "".join(output)
	return(final)
