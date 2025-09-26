from pyscript import document

class MorseTranslator:
    def __init__(self):
        self.MORSE_CODE = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
            '7': '--...', '8': '---..', '9': '----.', ' ': '/',
            '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
            '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
            '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
            '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.'
        }
        
        self.REVERSE_MORSE = {v: k for k, v in self.MORSE_CODE.items()}
    
    def text_to_morse(self, text):
        """Convert text to Morse code"""
        morse = []
        for char in text.upper():
            if char in self.MORSE_CODE:
                morse.append(self.MORSE_CODE[char])
            else:
                morse.append(char)
        return ' '.join(morse)

translator = MorseTranslator()

def translate_english(event):
    input_text = document.querySelector("#english")
    english = input_text.value
    output_div = document.querySelector("#output")
    output_div.innerText = translator.text_to_morse(english)  # Fixed method name
