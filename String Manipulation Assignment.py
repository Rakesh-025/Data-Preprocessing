### STRING MANIPULATION ###

String = ("Growth")

##  A. accessing the letter “G” from “Growth”

String[0]

## B.  finding the length of the string

len(String)

### C. Count how many times “G” is in the string

String.count("G")

### 2.Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”
# Code for the following:
#a)Count the number of characters in the string.

Num = "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."
print(Num.count(''))

#3.Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
#Code for the following tasks:
###  a)get one char of the word

Name = "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
print(Name[0])
### b)get the first three char
    
print(Name[0:3])

###  c)get the last three char

print(Name[-3:])

#  4.create a string "stay positive and optimistic". Now write a code to split on whitespace.
# Write a code to find if:
s = "stay positive and optimistic"
#  a)The string starts with “H”

s.startswith("H")

### b)The string ends with “d”
    
s.endswith("d")
    
### c)The string ends with “c” 
s.endswith("c") 


#### 5.Write a code to print " 🪐 " one hundred and eight times. (only in python) #####
print(" 🪐 "*108)

#### 6 question R ###33


####7.Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of” ####
rk =  "Grow Gratitude"
rk.replace("Grow","Growth")


####8.A story was printed in a pdf, which isn’t making any sense. i.e.:
#".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"

#You have noticed that the story is printed in a reversed order. Rectify the same and write a code to print the same story in a correct order.
rj = ".elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht ,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"
print(rj[::-1])
