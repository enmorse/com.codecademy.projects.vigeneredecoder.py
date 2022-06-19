alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?!' "


def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    final_keyword = ''

    for i in range(len(coded_message)):
        if coded_message[i] in punctuation:
            final_keyword += coded_message[i]
        else:
            final_keyword += keyword[letter_pointer]
            letter_pointer = (letter_pointer + 1) % len(keyword)

    translated_message = ''

    for i in range(len(coded_message)):
        if not coded_message[i] in punctuation:
            letter_value = alphabet.find(coded_message[i]) - \
                           alphabet.find(final_keyword[i])
            translated_message += alphabet[letter_value % 26]
        else:
            translated_message += coded_message[i]

    return translated_message


message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! " \
          "cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))
