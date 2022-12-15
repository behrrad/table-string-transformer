import itertools

from Transformation.Pattern import *
from Transformation.Blocks.LiteralPatternBlock import LiteralPatternBlock
from Transformation.Blocks.PositionPatternBlock import PositionPatternBlock
from Transformation.Blocks.TokenPatternBlock import TokenPatternBlock


# PATTERNS_TO_EXTRACT = [PositionPatternBlock, TokenPatternBlock]  # not including literal
def extract_patterns(rows, patterns, patterns_to_extract, verbose=True):
    all_patterns_list = []
    # cnt, nnn = 0, len(patterns)
    for pattern in patterns:
        # cnt += 1
        # print(f"Extracting pattern for placeholder {cnt}/{nnn}")
        candidates = []
        for blk in pattern.blocks:
            if blk.type == BasicPatternBlock.TYPE_STR:
                candidates.append([LiteralPatternBlock(blk.text)])
            elif blk.type == BasicPatternBlock.TYPE_TOKEN:
                tmp = set()

                for pat in patterns_to_extract:
                    x = pat.extract(pattern.inp, blk)
                    # print(x)
                    # print('!' * 4)
                    tmp.update(x)
                candidates.append(list(tmp))
                # print(tmp)
                # print(pattern.inp)
                # print(pattern.goal)
                # print(blk)
                # print(blk.text[0])
                # print("****")
            else:
                raise Exception('App must not enter here')

        pp = list(itertools.product(*candidates))
        res = []
        for p in pp:
            res.append(Pattern(p))

        all_patterns_list += res

    if verbose:
        print(f"{len(all_patterns_list)} Patterns Extended.")

    # print("**NOT** Removing duplicates...")
    all_patterns = all_patterns_list
    # print("Removing duplicates...")
    # all_patterns = set(all_patterns_list)

    if verbose:
        print(f"{len(all_patterns)} Patterns Remained.")
    return all_patterns
