#Pig Latin
# pig_latin = input('"Enter the any word." : ')
# vowel = "a", "e", "i", "o", "u"
# length = len(pig_latin)
# for vowel_word in vowel:
#     if pig_latin[0] == vowel_word:
#         print(pig_latin + "way")
#         exit()
#     else:
#         print(pig_latin[1:length]+pig_latin[0]+"ay")
#         exit()


#another way
pig_latin = input('"Enter the any word." : ')
vowel = "a", "e", "i", "o", "u"
first_p = pig_latin[0].lower()
length = len(pig_latin)
for vowel_word in vowel:
    if first_p == vowel_word:
        print(pig_latin + "way")
        exit()
    else:
        print(pig_latin[1:length] + pig_latin[0] + 'ay')
        exit()
