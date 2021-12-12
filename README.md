# python-libs
A few python libraries

<runes.py>:
	A library with which you can translate any string into Elder Futhark(old germanic runes).
	Just import it into your project and call the "translate" function with the string of your
	text as the first argument.
	You can also set "german_replacement"(True: ä,ö,ü -> ae,oe,ue, False: ä,ö,ü -> a,o,u) and
	"ask_user"(True: User will be asked every time there is more than one possible translation,
	False: The best option is going to be selected automatically).
	The "translate" function returns a string.

<colour_tools.py>:
	A library which can invert colours(rgb tuple, hex string) and convert them from rgb tuples to
	hex strings or the other way.
