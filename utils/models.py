
from functools import partial
from cuid2.generator import Cuid
from charidfield import CharIDField

def cuid_default_value():
    return Cuid(length=32).generate()



CuidField = partial(
    CharIDField,
    default=cuid_default_value,
    max_length=225,
    help_text="cuid-format identifier for this entity."
)
