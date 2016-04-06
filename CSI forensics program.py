dna_text = open("dna.txt").read()
# print len(dna_text)

gender_female = "TGAAGGACCTTC"
gender_male = "TGCAGGAACTTC"

race_white = "AAAACCTCA"
race_black = "CGACTACAG"
race_asian = "CGCGGGCCG"

haircolor_black = "CCAGCAATCGC"
haircolor_brown = "GCCAGTGCCG"
haircolor_carrot = "TTAGCTATCGC"

facial_shape_square = "GCCACGG"
facial_shape_round = "ACCACAA"
facial_shape_oval = "AGGCCTCA"

eyecolor_blue = "TTGTGGTGGC"
eyecolor_green = "GGGAGGTGGC"
eyecolor_brown = "AAGTAGTGAC"

# print answer -1 means not found!

if dna_text.find(gender_female) > -1:
    print ("gender is female!")
else:
    print ("gender is male!")
#

if dna_text.find(race_white) > -1:
    print ("race is white!")
elif dna_text.find(race_black) > -1:
    print ("race is black!")
else:
    print ("race is asian!")
#

if dna_text.find(haircolor_black) > -1:
    print ("haircolor is black!")
elif dna_text.find(haircolor_brown) > -1:
    print ("haircolor is brown!")
else:
    print ("haircolor is carrot!")
#

if dna_text.find(eyecolor_blue) > -1:
    print ("eyecolor is blue!")
elif dna_text.find(eyecolor_green) > -1:
    print ("eyecolor is green!")
else:
    print ("eyecolor is brown!")
#

if dna_text.find(facial_shape_square) > -1:
    print ("facial shape is square!")
elif dna_text.find(facial_shape_round) > -1:
    print ("facial shape is round!")
else:
    print ("facial shape is oval!")
#

"""
not working

if dna_text.find(gender_male) & dna_text.find(race_white) & dna_text.find(haircolor_carrot) & dna_text.find(eyecolor_brown) & dna_text.find(facial_shape_round):
    print ("Ziga is the criminal!")
elif dna_text.find(gender_male) & dna_text.find(race_white) & dna_text.find(haircolor_black) & dna_text.find(eyecolor_blue) & dna_text.find(facial_shape_oval):
    print ("Matej is the criminal!")
elif dna_text.find(gender_male) & dna_text.find(race_white) & dna_text.find(haircolor_brown) & dna_text.find(eyecolor_green) & dna_text.find(facial_shape_square):
    print ("Miha is the criminal!")
else:
    print ("Criminal not found!")

"""

# MIHA = CRIMINAL = facial_shape_square, race_white, gender_male, haircolor_brown, eyecolor_green
