def es_vocal_if(letra: str) -> bool:
    letra = letra.lower()

    if letra == 'a':
        return True
    elif letra == 'e':
        return True
    elif letra == 'i':
        return True
    elif letra == 'o':
        return True
    elif letra == 'u':
        return True
    else:
        return False

assert es_vocal_if("a")
assert not es_vocal_if("b")
assert es_vocal_if("A")

###############################################################################

def es_vocal_if_in(letra: str) -> bool:

    letra = letra.lower()

    if letra in 'aeiou':
        return True
    return False

assert es_vocal_if_in("a")
assert not es_vocal_if_in("b")
assert es_vocal_if_in("A")

###############################################################################

def es_vocal_in(letra: str) -> bool:

    letra = letra.lower()
    return letra in 'aeiou'

assert es_vocal_in("a")
assert not es_vocal_in("b")
assert es_vocal_in("A")
