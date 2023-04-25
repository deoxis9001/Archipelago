import string
import typing


def generate_group(cls: type, template: string.Template,
                   locations: typing.Optional[typing.Iterable[str]] = None):
    if locations is None:
        locations = cls.locations
    return cls(*(template.substitute(location=l) for l in locations))


class JewelPieces(typing.NamedTuple):
    ne: str
    se: str
    sw: str
    nw: str

    locations = tuple("Top Right/Bottom Right/Bottom Left/Top Left".split("/"))

class Crowns(typing.NamedTuple):
    bronze: str
    silver: str
    gold: str
    
    locations = tuple("Bronze Silver Gold".split())
