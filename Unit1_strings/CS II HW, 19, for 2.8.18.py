p_words = {}
p_words['sir'] = 'matey'
p_words['hotel'] = 'fleabag inn'
p_words['student'] = 'swabbie'
p_words['boy'] = 'matey'
p_words['madam'] = 'proud beauty'
p_words['professor'] = 'foul blaggart'
p_words['restaurant'] = 'galley'
p_words['your'] = 'yer'
p_words['excuse'] = 'arr'
p_words['students'] = 'swabbies'
p_words['are'] = 'be'
p_words['lawyer'] = 'foul blaggart'
p_words['the'] = "th'"
p_words['my'] = 'me'
p_words['hello'] = 'avast'
p_words['is'] = 'be'
p_words['man'] = 'matey'

to_translate = input(": ")

translated_sentence = []
translate = to_translate.split()

for aword in translate:

    if aword in p_words:
        translated_sentence.append(p_words[aword])

    else:
        translated_sentence.append(aword)

new_sentence = " ".join(translated_sentence)

print(new_sentence)
