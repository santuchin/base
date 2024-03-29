from . import natural

def encode(number: tuple[int, int], digits) -> tuple:

    num, den = number

    base = len(digits)
    
    nat, mod = divmod(num, den)

    ratper = digits[0:0]
    mods = []
    
    while mod:
    
        mods.append(mod)

        div, mod = divmod(mod * base, den)
        ratper += digits[div:div + 1]

        if mod in mods:
            
            index = mods.index(mod)
        
            rat = ratper[:index]
            per = ratper[index:]

            return (natural.encode(nat, digits), rat, per)

    rat = ratper
    per = digits[0:0]

    return (natural.encode(nat, digits), rat, per)

def decode(number: tuple, digits) -> tuple[int, int]:
    
    nat, rat, per = number

    base = len(digits)

    ratlen = len(rat)

    ratnum = natural.decode(rat, digits) if ratlen else 0
    pernum = natural.decode(per, digits)

    if pernum:

        perden = base ** len(per) - 1
        ratden = base ** ratlen
    
    else:
        perden = 1
        ratnum = base ** ratlen else 1

    num = ratnum * perden + pernum
    den = ratden * perden

    return (natural.decode(nat, digits) * den + num, den)

def period(number: tuple[int, int], base: int) -> bool:
    
    num, den = number

    mod = num % base

    mods = []

    while mod:
        
        mods.append(mod)

        mod = mod * base % den
        
        if mod in mods:
            return True

    return False

