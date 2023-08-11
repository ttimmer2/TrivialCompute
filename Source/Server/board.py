import copy

class Board(object):
    _self = None

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

    def __new__(cls):
        """
        Create the backend interface object if no instance exists.
        else return previous object
        """
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self



    def get_valid_spots(self, start, roll, visited=[], final=[]):
        visited.append(start)   # add starting position to visited positions
        if roll-1 < 0:
            final.append(start) # if the roll can't be decremented, then you are in the final spot.
        for node in Board.CONNECTIONS[start]:
            if roll-1 >= 0:
                if not node in visited: # don't revisit nodes
                    self.get_valid_spots(node, roll-1, visited,final) # call again with decremented roll. Preserve visited and final nodes
        return final


        
if __name__ == "__main__":
    b = Board()
    q = Board()
    print(b==q)
    roll = 6
    p = b.get_valid_spots(43,roll)
    for pos in p:
        print(Board.POSITIONS[pos])
