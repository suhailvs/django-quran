# 28 Arabic letters
LETTERS_ONLY = "AbtvjHxd*rzs$SDTZEgfqklmnhwy"
_letters_only = [i for i in range(39, 75) if i not in {41, 59, 60, 61, 62, 63, 64, 73}]

# Remaining Arabic letters
_other_buckwalter = """'>&<}p_YFNKaui~o^#`{:@"[;,.!-+%]"""
_other = (
    [33, 35, 36, 37, 38, 41, 64, 73]
    + list(range(75, 85))
    + [112, 113, 220, 223, 224, 226, 227, 229, 230, 232]
    + list(range(234, 238))
)

# Combined mappings
_buckwalter = LETTERS_ONLY + _other_buckwalter
_unicode = [chr(0x0600 + i) for i in _letters_only + _other]

# Create mapping dictionaries
_unicode_to_buckwalter = dict(zip(_unicode, _buckwalter))
_buckwalter_to_unicode = {bw: u for u, bw in _unicode_to_buckwalter.items()}


def decode(word: str) -> str:
    """Decodes a Buckwalter-transliterated string into Arabic Unicode."""
    return "".join(_buckwalter_to_unicode[l] for l in word)


def encode(word: str) -> str:
    """Encodes an Arabic Unicode string into Buckwalter transliteration."""
    return "".join(_unicode_to_buckwalter[l] for l in word)