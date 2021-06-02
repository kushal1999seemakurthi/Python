
def alpha_2_code(String,dic_A_2_C):
	p=dic_A_2_C[String[0]]
	for i in String[1:]:
		p+="   "+dic_A_2_C[i]
	return p


def code_2_alpha(String,dic_C_2_A):
	Alpha=[i for i in String.split("   ")]
	q=[dic_C_2_A[i] for i in Alpha]
	p=''.join(q)
	return p



Type=input()

string1=input()

print(string1)

dic_A_2_C={"A" : ". ---" ,
"B" : "--- . . ." ,
"C" : "--- . --- ." ,
"D" : "--- . ." ,
"E" : "." ,
"F" : ". . --- ." ,
"G" : "--- --- ." ,
"H" : ". . . ." ,
"I" : ". ." ,
"J" : ". --- --- ---" ,
"K" : "--- . ---" ,
"L" : ". --- . ." ,
"M" : "--- ---" ,
"N" : "--- ." ,
"O" : "--- --- ---" ,
"P" : ". --- --- ." ,
"Q" : "--- --- . ---" ,
"R" : ". --- ." ,
"S" : ". . ." ,
"T" : "---" ,
"U" : " . . ---" ,
"V" : ". . . ---" ,
"W" : ". --- ---" ,
"X" : "--- . . ---" ,
"Y" : "--- . --- ---" ,
"Z" : "--- --- . ." ,

"1" : ". --- --- --- ---" ,
"2" : ". . --- --- ---" ,
"3" : ". . . --- ---" ,
"4" : ". . . . ---" ,
"5" : ". . . . ." ,
"6" : "--- . . . ." ,
"7" : "--- --- . . ." ,
"8" : "--- --- --- . ." ,
"9" : "--- --- --- --- ." ,
"0" : "--- --- --- --- ---"
}

dic_C_2_A={value : key for (key, value) in dic_A_2_C.items()}

def CCC(string):
	Cwords=[i for i in string.split("       ")]
	C_2_W =[code_2_alpha(i,dic_C_2_A) for i in Cwords]
	sentence=' '.join(C_2_W)
	print(sentence)
	return sentence


def AAA(string):
	Awords=[i for i in string.split(" ")]
	W_2_C =[alpha_2_code(i,dic_A_2_C) for i in Awords]
	sentence='       '.join(W_2_C)
	print(sentence)
	return sentence

if( Type== "Code"):
	print("___________Code to Alpha___________")
	p=CCC(string1)
	print("___________Alpha to Code___________")
	pp=AAA(p)


if( Type== "Alpha"):
	print("___________Alpha to Code___________")
	p=AAA(string1)
	print("___________Code to Alpha___________")
	pp=CCC(p)




