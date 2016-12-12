all_prefixes = ('arc', 'inv', 'inverse')

all_sin = ('sin', 'sine')
all_cos = ('cos', 'cosine')
all_tan = ('tan', 'tg', 'tangent')
all_csc = ('csc', 'cosec', 'cosecant')
all_sec = ('sec', 'secant')
all_cot = ('cot', 'cotan', 'cotg', 'ctg', 'ctn', 'cotangent')

all_asin = tuple([x+y for x in all_prefixes for y in all_sin])
all_acos = tuple([x+y for x in all_prefixes for y in all_cos])
all_atan = tuple([x+y for x in all_prefixes for y in all_tan])
all_acsc = tuple([x+y for x in all_prefixes for y in all_csc])
all_asec = tuple([x+y for x in all_prefixes for y in all_sec])
all_acot = tuple([x+y for x in all_prefixes for y in all_cot])

all_sinh = tuple([y+'h' for y in all_sin])
all_cosh = tuple([y+'h' for y in all_cos])
all_tanh = tuple([y+'h' for y in all_tan])
all_csch = tuple([y+'h' for y in all_csc])
all_sech = tuple([y+'h' for y in all_sec])
all_coth = tuple([y+'h' for y in all_cot])

all_asinh = tuple([y+'h' for y in all_asin])
all_acosh = tuple([y+'h' for y in all_acos])
all_atanh = tuple([y+'h' for y in all_atan])
all_acsch = tuple([y+'h' for y in all_acsc])
all_asech = tuple([y+'h' for y in all_asec])
all_acoth = tuple([y+'h'for y in all_acot])

all_functions = {
    all_sin: 'sin',
    all_cos: 'cos',
    all_tan: 'tan',
    all_csc: 'csc',
    all_sec: 'sec',
    all_cot: 'cot',
    all_asin: 'asin',
    all_acos: 'acos',
    all_atan: 'atan',
    all_acsc: 'acsc',
    all_asec: 'asec',
    all_acot: 'acot',
    all_sinh: 'sinh',
    all_cosh: 'cosh',
    all_tanh: 'tanh',
    all_csch: 'csch',
    all_sech: 'sech',
    all_coth: 'coth',
    all_asinh: 'asinh',
    all_acosh: 'acosh',
    all_atanh: 'atanh',
    all_acsch: 'acsch',
    all_asech: 'asech',
    all_acoth: 'acoth'
}