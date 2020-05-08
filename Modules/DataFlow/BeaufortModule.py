from .pycipher.beaufort import Beaufort

properties = {
    'name': 'Beaufort',
    'categories': '密码',
    'input': {0: 'input'},
    'output': {0: 'output'},
    'properties': {
        'switch': ['encrypt', 'decrypt'],
        'key': str
    }
}
defaults = {
    'switch': 'encrypt',
    'key': 'REVERIERTQL'
}

def main(inp, settings):
    coder = Beaufort(settings['key'])
    if settings['switch'] == 'encrypt':
        return {0: coder.encipher(inp[0])}
    else:
        return {0: coder.decipher(inp[0])}