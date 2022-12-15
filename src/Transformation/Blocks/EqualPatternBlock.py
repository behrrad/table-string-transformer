from Transformation.Blocks.RawPatternBlock import RawPatternBlock


class EqualPatternBlock(RawPatternBlock):
    NAME = "EQUAL"

    def __init__(self):
        super().__init__()
        self._hash = hash(self.NAME)

    def apply(self, inp):
        return inp

    @classmethod
    def extract(cls, inp, blk):
        s = set()
        s.add(EqualPatternBlock())
        return s

    def __eq__(self, other):
        return True

    def __hash__(self):
        return self._hash

    def __repr__(self):
        return 'Equal pattern block'
