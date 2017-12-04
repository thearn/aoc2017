"""Day 2: 'title' https://adventofcode.com/2016/day/2."""

import pytest
import numpy as np

main_inp = """UDRLRRRUULUUDULRULUDRDRURLLDUUDURLUUUDRRRLUUDRUUDDDRRRLRURLLLDDDRDDRUDDULUULDDUDRUUUDLRLLRLDUDUUUUDLDULLLDRLRLRULDDDDDLULURUDURDDLLRDLUDRRULDURDDLUDLLRRUDRUDDDLLURULRDDDRDRRLLUUDDLLLLRLRUULRDRURRRLLLLDULDDLRRRRUDRDULLLDDRRRDLRLRRRLDRULDUDDLDLUULRDDULRDRURRURLDULRUUDUUURDRLDDDURLDURLDUDURRLLLLRDDLDRUURURRRRDRRDLUULLURRDLLLDLDUUUDRDRULULRULUUDDULDUURRLRLRRDULDULDRUUDLLUDLLLLUDDULDLLDLLURLLLRUDRDLRUDLULDLLLUDRLRLUDLDRDURDDULDURLLRRRDUUDLRDDRUUDLUURLDRRRRRLDDUUDRURUDLLLRRULLRLDRUURRRRRLRLLUDDRLUDRRDUDUUUDRUDULRRULRDRRRDDRLUUUDRLLURURRLLDUDRUURDLRURLLRDUDUUDLLLUULLRULRLDLRDDDU
DRRRDRUDRLDUUDLLLRLULLLUURLLRLDRLURDRDRDRLDUUULDRDDLDDDURURUDRUUURDRDURLRLUDRRRDURDRRRDULLRDRRLUUUURLRUULRRDUDDDDUURLDULUDLLLRULUDUURRDUULRRDDURLURRUDRDRLDLRLLULULURLRDLRRRUUURDDUUURDRDRUURUDLULDRDDULLLLLRLRLLUDDLULLUDDLRLRDLDULURDUDULRDDRLUDUUDUDRLLDRRLLDULLRLDURUDRLRRRDULUUUULRRLUDDDLDUUDULLUUURDRLLULRLDLLUUDLLUULUULUDLRRDDRLUUULDDRULDRLURUURDLURDDRULLLLDUDULUDURRDRLDDRRLRURLLRLLLLDURDLUULDLDDLULLLRDRRRDLLLUUDDDLDRRLUUUUUULDRULLLDUDLDLURLDUDULRRRULDLRRDRUUUUUURRDRUURLDDURDUURURULULLURLLLLUURDUDRRLRRLRLRRRRRULLDLLLRURRDULLDLLULLRDUULDUDUDULDURLRDLDRUUURLLDLLUUDURURUD
UDUUUUURUDLLLRRRDRDRUDDRLLDRRLDRLLUURRULUULULRLLRUDDRLDRLUURDUDLURUULLLULLRRRULRLURRDDULLULULRUDDDUURDRLUDUURRRRUUULLRULLLDLURUDLDDLLRRRULDLLUURDRRRDRDURURLRUDLDLURDDRLLLUUDRUULLDLLLLUUDRRURLDDUDULUDLDURDLURUURDUUUURDLLLRUUURDUUUDLDUDDLUDDUDUDUDLDUDUUULDULUURDDLRRRULLUDRRDLUDULDURUURULLLLUDDDLURURLRLRDLRULRLULURRLLRDUDUDRULLRULRUDLURUDLLDUDLRDRLRDURURRULLDDLRLDDRLRDRRDLRDDLLLLDUURRULLRLLDDLDLURLRLLDULRURRRRDULRLRURURRULULDUURRDLURRDDLDLLLRULRLLURLRLLDDLRUDDDULDLDLRLURRULRRLULUDLDUDUDDLLUURDDDLULURRULDRRDDDUUURLLDRDURUDRUDLLDRUD
ULRDULURRDDLULLDDLDDDRLDUURDLLDRRRDLLURDRUDDLDURUDRULRULRULULUULLLLDRLRLDRLLLLLRLRRLRLRRRDDULRRLUDLURLLRLLURDDRRDRUUUDLDLDRRRUDLRUDDRURRDUUUDUUULRLDDRDRDRULRLLDLDDLLRLUDLLLLUURLDLRUDRLRDRDRLRULRDDURRLRUDLRLRLDRUDURLRDLDULLUUULDRLRDDRDUDLLRUDDUDURRRRDLDURRUURDUULLDLRDUDDLUDDDRRRULRLULDRLDDRUURURLRRRURDURDRULLUUDURUDRDRLDLURDDDUDDURUDLRULULURRUULDRLDULRRRRDUULLRRRRLUDLRDDRLRUDLURRRDRDRLLLULLUULRDULRDLDUURRDULLRULRLRRURDDLDLLRUUDLRLDLRUUDLDDLLULDLUURRRLRDULRLRLDRLDUDURRRLLRUUDLUURRDLDDULDLULUUUUDRRULLLLLLUULDRULDLRUDDDRDRDDURUURLURRDLDDRUURULLULUUUDDLRDULDDLULDUDRU
LRLRLRLLLRRLUULDDUUUURDULLLRURLDLDRURRRUUDDDULURDRRDURLRLUDLLULDRULLRRRDUUDDRDRULLDDULLLUURDLRLRUURRRLRDLDUDLLRLLURLRLLLDDDULUDUDRDLRRLUDDLRDDURRDRDUUULLUURURLRRDUURLRDLLUDURLRDRLURUURDRLULLUUUURRDDULDDDRULURUULLUDDDDLRURDLLDRURDUDRRLRLDLRRDDRRDDRUDRDLUDDDLUDLUDLRUDDUDRUDLLRURDLRUULRUURULUURLRDULDLDLLRDRDUDDDULRLDDDRDUDDRRRLRRLLRRRUUURRLDLLDRRDLULUUURUDLULDULLLDLULRLRDLDDDDDDDLRDRDUDLDLRLUDRRDRRDRUURDUDLDDLUDDDDDDRUURURUURLURLDULUDDLDDLRUUUULRDRLUDLDDLLLRLLDRRULULRLRDURRRLDDRDDRLU"""

# Part 1 ---------------------------------


def day_2_2016_part_1(seq):
    """Part 1."""
    lines = seq.split("\n")
    keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    paths = {'R' : np.array([0, 1]),
             'L' : np.array([0, -1]),
             'U' : np.array([-1, 0]),
             'D' : np.array([1, 0]),
             }
    position = np.array([1, 1])
    digits = ''
    for line in lines:
        for direction in line:
            position += paths[direction]
            position = np.clip(position, 0, 2)
        row, col = position
        digits += keypad[row][col]
    return int(digits)


# Part 2 --------------------------------


def day_2_2016_part_2(seq):
    """Part 2."""
    lines = seq.split("\n")
    keypad = [[None, None, '1', None, None],
              [None, '2', '3', '4', None],
              ['5', '6', '7', '8', '9'],
              [None, 'A', 'B', 'C', None],
              [None, None, 'D', None, None]]
    paths = {'R' : np.array([0, 1]),
             'L' : np.array([0, -1]),
             'U' : np.array([-1, 0]),
             'D' : np.array([1, 0]),
             }
    position = np.array([2, 0])
    digits = ''
    for line in lines:
        for direction in line:
            new_position = position + paths[direction]
            new_position = np.clip(new_position, 0, 4)
            row, col = new_position
            if keypad[row][col] is not None:
                position = new_position
        digits += keypad[row][col]
    return digits


# Tests ---------------------------------

test1 = """ULL
RRDDD
LURDL
UUUUD"""

@pytest.mark.parametrize('method, inp, expected', [
    (day_2_2016_part_1, test1, 1985),
    (day_2_2016_part_2, test1, '5DB3'),
])
def test_day_2_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    print('day_2_2016_part_1 solution:', day_2_2016_part_1(main_inp))
    print('day_2_2016_part_2 solution:', day_2_2016_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
