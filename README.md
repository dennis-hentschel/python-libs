# python-libs
A few python libraries

<runes.py>:
	A library with which you can translate any string into Elder Futhark(old germanic runes).
	Just import it into your project and call the "translate" function with the string of your
	text as the first argument.
	You can also set "german_replacement"(True: ä,ö,ü -> ᚨᛖ,ᛟᛖ,ᚢᛖ; False: ä,ö,ü -> ᚨ,ᛟ,ᚢ),
	english_replacement(True: th -> ᚦ; False: th -> ᛏᚻ)
	 and "ask_user" (True: asks whenever there is more than one possible translation; False: The best option is selected by default).
	The "translate" function returns a string.

<colour_tools.py>:
	A library which can invert colours(rgb tuple, hex string) and convert them from rgb tuples to
	hex strings or the other way.
