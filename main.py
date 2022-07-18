MORSE_CODE_DICT = {
    '.-': 'a',
    '-...': 'b',
    '-.-.': 'c',
    '-..': 'd',
    '.': 'e',
    '..-.': 'f',
    '--.': 'g',
    '....': 'h',
    '..': 'i',
    '.---': 'j',
    '-.-': 'k',
    '.-..': 'l',
    '--': 'm',
    '-.': 'n',
    '---': 'o',
    '.--.': 'p',
    '--.-': 'q',
    '.-.': 'r',
    '...': 's',
    '-': 't',
    '..-': 'u',
    '...-': 'v',
    '.--': 'w',
    '-..-': 'x',
    '-.--': 'y',
    '--..': 'z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '.-.-.-': '.',
    '--..--': ',',
    '..--..': '?',
    '.----.': "'",
    '-..-.': '/',
    '---...': ':',
    '-.-.-.': ';',
    '-....-': '-',
    '-...-': '=',
    '/': ' '
}
SWITCHED_MORSE_CODE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def morse_code_encoder(text):

    words = text.split(' ')
    encoded_words = [' '.join([SWITCHED_MORSE_CODE_DICT[char] for char in word.lower()]) for word in words]
    encoded_text = '/'.join(encoded_words)

    return encoded_text


def morse_code_decoder(text):

    words = text.split('/')
    decoded_words = [''.join([MORSE_CODE_DICT[char] for char in word.split(' ')]) for word in words]
    decoded_text = ' '.join(decoded_words)

    return decoded_text


run_program = True
while run_program:
    user_input = input('Input text to convert to morse code: \n')
    print(morse_code_encoder(user_input))
    keep_going = ''
    while keep_going not in ['y', 'n']:
        keep_going = input('Covert more text? (y/n)\n')

    if keep_going == 'n':
        run_program = False


