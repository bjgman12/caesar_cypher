from cryptography import __version__
from cryptography.crypto import crack,encrypt_alph,decrypt_alph


def test_version():
    assert __version__ == '0.1.0'


def test_crack():
    actual = crack('Pa dhz aol dvyza vm aptlz. Pa dhz aol ilza vm aptlz')
    expected = 'It was the worst of times. It was the best of times'
    assert actual == expected

def test_encrypt():
    actual = encrypt_alph('It was the worst of times. It was the best of times',7)
    expected = 'Pa dhz aol dvyza vm aptlz. Pa dhz aol ilza vm aptlz'
    assert actual == expected

def test_decrypt():
    actual = decrypt_alph('Pa dhz aol dvyza vm aptlz. Pa dhz aol ilza vm aptlz',7)
    expected = 'It was the worst of times. It was the best of times'
    assert actual == expected