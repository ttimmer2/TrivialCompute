import copy

POSITIONS = [
    (0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0),
    (0,1),                      (4,1),                      (8,1),
    (0,2),                      (4,2),                      (8,2),
    (0,3),                      (4,3),                      (8,3),
    (0,4), (1,4), (2,4), (3,4), (4,4), (5,4), (6,4), (7,4), (8,4),
    (0,5),                      (4,5),                      (8,5),
    (0,6),                      (4,6),                      (8,6),
    (0,7),                      (4,7),                      (8,7),
    (0,8), (1,8), (2,8), (3,8), (4,8), (5,8), (6,8), (7,8), (8,8)
]


INTERSECTIONS = [4, 18, 22, 26, 40 ]   # the spots where a mover has directional choices

# represents the indices of the Roll Again squares on POSITIONS
ROLL_AGAIN = [0,8,36,44]

# represents the index of the HOME square on POSITIONS
HOME = [22]

# represents the indices of the HeadQuarter squares in POSITIONS
HQ = [4,18,26,40]

# represents the indices of the different category spaces
C0 = [4,9,11,21,25,27,29,31,38,42]
C1 = [18,1,5,10,14,24,28,32,37,41]
C2 = [40,2,6,13,15,17,19,23,33,35]
C3 = [26,3,7,12,16,20,30,34,39,43]


# For each boardsquare, shows a list of boardsquares you can move to.
CONNECTIONS = { 0: [1, 9],
                1: [0, 2],
                2: [1, 3],
                3: [2, 4],
                4: [3, 5, 10],
                5: [4, 6],
                6: [5, 7],
                7: [6, 8],
                8: [7, 11],
                9: [0, 12],
                10: [4, 13],
                11: [8, 14],
                12: [9, 15],
                13: [10, 16],
                14: [11, 17],
                15: [12, 18],
                16: [13, 22],
                17: [14, 26],
                18: [15, 19, 27],
                19: [18, 20],
                20: [19, 21],
                21: [20, 22],
                22: [16, 21, 23, 28],
                23: [22, 24],
                24: [23, 25],
                25: [24, 26],
                26: [17, 25, 29],
                27: [18, 30],
                28: [22, 31],
                29: [26, 32],
                30: [27, 33],
                31: [28, 34],
                32: [29, 35],
                33: [30, 36],
                34: [31, 40],
                35: [32, 44],
                36: [33, 37],
                37: [36, 38],
                38: [37, 39],
                39: [38, 40],
                40: [34, 39, 41],
                41: [40, 42],
                42: [41, 43],
                43: [42, 44],
                44: [35, 43]
                }


def get_valid_spots(start, roll, visited=[], final=[]):
    visited.append(start)   # add starting position to visited positions
    if roll-1 < 0:
        final.append(start) # if the roll can't be decremented, then you are in the final spot.
    for node in CONNECTIONS[start]:
        if roll-1 >= 0:
            if not node in visited: # don't revisit nodes
                get_valid_spots(node, roll-1, visited,final) # call again with decremented roll. Preserve visited and final nodes
    return final


        
if __name__ == "__main__":
    roll = 8
    p = get_valid_spots(43,roll)
    for pos in p:
        print(POSITIONS[pos])
