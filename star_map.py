from star import Star
from constellation import Constellation, Random_Constellation
import random

#create lots of star objects                                ### list_of_stars
#use those star objets to make constellation objects        
#create lots of constellation objects                       ### list_of_constellations

class Map:
    def __init__(self, field_x, field_y):
        self.field_x = field_x
        self.field_y = field_y
        self.field_buffer = 50 #gap between display edge and circle
        self.field_inner_buffer = 5 #gap between circle and outer stars, bigger number --> bigger gap
        self.r = self.field_x / 2 - self.field_inner_buffer #raduis
        self.Xcenter = self.Ycenter = self.field_x / 2 + self.field_buffer

    ### given an (x,y) point it will return True/False if the point is in the circle drawn
    def is_in_circle(self, x, y, is_box=False):
        if is_box:
            pass
        else:
            return (x - self.Xcenter) ** 2 + (y - self.Ycenter) ** 2 <= self.r ** 2


    def coerce_to_center(self, x, y):
        newx, newy = x + self.Xcenter, y + self.Ycenter
        if self.is_in_circle(newx, newy):
            return (x, y)
        else:
            return (0, 0)



## STARS ## makes a list of Star objects and adds them to a list
    def place_stars(self, settings):
        self.number_of_stars = settings.number_of_stars
        self.list_of_stars = []
        stars_added = 0

        while stars_added < self.number_of_stars:
            x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
            if self.is_in_circle(x, y):
                self.list_of_stars.append(Star(x, y, settings))
                stars_added += 1


## CONSTELLATIONS ## makes constellation objects and edits their center/size to fit them where they need to go
    def place_constellations(self, constellation_size, settings):
        self.constellation_size = constellation_size #side length of the 5x5 grid
        self.list_of_constellations = []
        if settings.text_input:
            
            ### adds the point/line data for that letter to the list of constellations
            string_length = len(settings.text_input.upper())
            string_index = 0
            self.letter_spacing = constellation_size // 4
            for char in settings.text_input.upper():
                temp_letter_constellation = Constellation(self.constellation_size, (200,200), settings)
                temp_letter_constellation.grid_points.append(LETTER_CONSTELLATIONS.get(char)[0])
                temp_letter_constellation.grid_lines.append(LETTER_CONSTELLATIONS.get(char)[1])
                centerX = (self.constellation_size + self.letter_spacing) * (string_index - (string_length - 1) / 2) + self.Xcenter + settings.text_location[0]
                centerY = self.Ycenter - settings.text_location[1]
                temp_letter_constellation.center = (centerX, centerY)
                string_index += 1
                self.list_of_constellations.append(temp_letter_constellation)
            if settings.show_constellations:
                pass
        else:

            for i in range(settings.number_of_constellations):
                
                constellation_pick = random.randint(0, len(OTHER_CONSTELLATIONS) - 1)
                x, y = random.randint(self.field_buffer, self.field_buffer + self.field_x), random.randint(self.field_buffer, self.field_buffer + self.field_y)
                if is_in_circle(x,y) and no_overlap(x,y)
                    temp_other_constellation = Random_Constellation(self.constellation_size, (400,400), settings, orientation=random.randint(0,3), is_inverted=random.randint(0,1))
                    temp_other_constellation.grid_points.append(OTHER_CONSTELLATIONS.get(constellation_pick)[0])
                    temp_other_constellation.grid_lines.append(OTHER_CONSTELLATIONS.get(constellation_pick)[1])

                self.list_of_constellations.append(temp_other_constellation)


LETTER_CONSTELLATIONS = {
    'A':([3,12,14,21,25],[(3,12),(3,14),(12,14),(12,21),(14,25)]),
    'B':([1,3,9,11,13,19,21,23],[(1,3),(1,11),(11,21),(21,23),(11,13),(3,9),(9,13),(13,19),(19,23)]),
    'C':([2,4,6,16,22,24],[(2,4),(2,6),(6,16),(16,22),(22,24)]),
    'D':([1,3,9,19,21,23],[(1,21),(1,3),(3,9),(9,19),(19,23),(21,23)]),
    'E':([2,4,12,14,22,24],[(2,12),(12,22),(2,4),(12,14),(22,24)]),
    'F':([2,4,12,14,22],[(2,12),(12,22),(2,4),(12,14)]),
    'G':([2,4,6,10,16,18,20,22,24],[(2,4),(2,6),(4,10),(6,16),(16,22),(18,20),(20,24),(22,24)]),
    'H':([2,4,12,14,22,24],[(2,12),(12,22),(4,14),(14,24),(12,14)]),
    'I':([2,3,4,13,22,23,24],[(2,3),(3,4),(3,13),(13,23),(22,23),(23,24)]),
    'J':([1,3,4,16,18,22],[(1,3),(3,4),(3,18),(18,22),(22,16)]),
    'K':([2,4,12,22,24],[(2,12),(4,12),(12,22),(12,24)]),
    'L':([2,12,22,24],[(2,12),(12,22),(22,24)]),
    'M':([2,4,21,23,25],[(2,21),(2,23),(4,23),(4,25)]),
    'N':([1,4,21,24],[(1,21),(1,24),(24,4)]),
    'O':([2,4,6,10,16,20,22,24],[(2,4),(2,6),(4,10),(6,16),(10,20),(16,22),(20,24),(22,24)]),
    'P':([2,3,9,12,13,22],[(2,12),(12,22),(2,3),(3,9),(9,13),(12,13)]),
    'Q':([2,4,6,10,16,19,20,22,24,25],[(2,4),(2,6),(4,10),(6,16),(10,20),(16,22),(19,25),(20,24),(22,24)]),
    'R':([1,3,9,11,13,21,23],[(1,3),(1,11),(3,9),(9,13),(11,13),(11,21),(11,23)]),
    'S':([2,4,6,12,14,20,22,24],[(2,4),(2,6),(6,12),(12,14),(14,20),(20,24),(22,24)]),
    'T':([1,3,5,23],[(1,3),(3,5),(3,23)]),
    'U':([1,5,16,20,22,24],[(1,16),(5,20),(16,22),(20,24),(22,24)]),
    'V':([1,5,23],[(1,23),(5,23)]),
    'W':([1,8,5,22,24],[(1,22),(8,22),(8,24),(5,24)]),
    'X':([1,4,21,24],[(1,24),(4,21)]),
    'Y':([2,4,13,23],[(2,13),(4,13),(13,23)]),
    'Z':([2,4,22,24],[(2,4),(4,22),(22,24)]),
    ' ':([],[])
}


def test_random_constellations():
    output = [[],[]]
    for point_index in range(random.randint(4,9)):
        output[0].append(random.randint(1,26))

    for point in output[0]:
        point_pair = output[0][random.randint(0, len(output[0])-1)]
        output[1].append((point, point_pair))
    return output

OTHER_CONSTELLATIONS = {
    0:([3,5,11,15,21,23],[(11,23),(23,5),(21,3),(3,15)]),
    1:([1,3,4,11,13,14,23,25],[(1,3),(3,4),(3,13),(13,23),(11,13),(23,14),(14,25)]),
    2:([1,5,12,21,25],[(1,5),(1,12),(5,12),(5,21),(5,25),(21,25)]),
    3:([1,3,12,25],[(1,12),(12,3),(3,25)]),
    4:([1,3,5,13,22,24],[(1,13),(3,13),(5,13),(22,13),(24,13)]),
    5:([[23, 5, 22, 14, 1, 26, 25], [(23, 22), (5, 14), (22, 22), (14, 1), (1, 14), (26, 1), (25, 14)]]),
    6:([[21, 2, 19, 4, 11, 9], [(21, 9), (2, 9), (19, 19), (4, 2), (11, 2), (9, 11)]]),
    7:([[1, 25, 19, 11, 7, 20, 7, 3, 20], [(1, 3), (25, 20), (19, 20), (11, 7), (7, 3), (20, 20), (7, 3), (3, 20), (20, 20)]]),
    8:([[19, 21, 3, 10, 12, 25, 22, 12], [(19, 3), (21, 12), (3, 12), (10, 12), (12, 22), (25, 10), (22, 21), (12, 10)]]),
    9:([[16, 1, 10, 17, 3, 19], [(16, 17), (1, 10), (10, 17), (17, 19), (3, 17), (19, 3)]]),
    10:([[22, 17, 25, 26, 24, 9, 14, 26, 14], [(22, 17), (17, 26), (25, 9), (26, 24), (24, 25), (9, 26), (14, 14), (26, 26), (14, 9)]]),
    11:([[22, 8, 9, 26, 21, 25, 17], [(22, 8), (8, 9), (9, 8), (26, 22), (21, 22), (25, 21), (17, 9)]]),
    12:([[22, 24, 18, 20, 9, 7, 6], [(22, 20), (24, 9), (18, 7), (20, 24), (9, 18), (7, 7), (6, 7)]]),
    13:([[12, 12, 9, 12, 1, 14, 20, 12], [(12, 1), (12, 20), (9, 1), (12, 12), (1, 12), (14, 1), (20, 9), (12, 12)]]),
    14:([[22, 6, 20, 16, 24, 22, 18, 16], [(22, 6), (6, 24), (20, 22), (16, 6), (24, 24), (22, 6), (18, 16), (16, 16)]]),
    15:([[25, 15, 24, 22, 23], [(25, 15), (15, 22), (24, 15), (22, 25), (23, 24)]]),
    16:([[12, 21, 19, 22, 13, 25, 20], [(12, 12), (21, 22), (19, 25), (22, 25), (13, 22), (25, 12), (20, 19)]]),
    17:([[26, 23, 1, 18], [(26, 18), (23, 1), (1, 26), (18, 23)]]),
    18:([[1, 22, 14, 4, 6, 4, 22, 1, 11], [(1, 4), (22, 14), (14, 14), (4, 1), (6, 14), (4, 14), (22, 14), (1, 1), (11, 4)]]),
    19:([[23, 20, 12, 21, 1, 13], [(23, 21), (20, 20), (12, 23), (21, 12), (1, 23), (13, 23)]]),
    20:([[22, 18, 11, 7, 21, 19, 19], [(22, 22), (18, 19), (11, 22), (7, 11), (21, 21), (19, 19), (19, 21)]]),
    21:([[16, 9, 8, 18, 23, 16, 12, 22], [(16, 16), (9, 18), (8, 22), (18, 23), (23, 23), (16, 16), (12, 12), (22, 16)]]),
    22:([[21, 1, 8, 4, 7, 3, 13, 12, 22], [(21, 22), (1, 3), (8, 1), (4, 4), (7, 3), (3, 12), (13, 3), (12, 12), (22, 1)]]),
    23:([[5, 3, 7, 10, 22, 2, 3], [(5, 10), (3, 7), (7, 3), (10, 5), (22, 10), (2, 10), (3, 22)]]),
    24:([[11, 11, 23, 16, 22, 5], [(11, 16), (11, 5), (23, 11), (16, 11), (22, 11), (5, 16)]]),
    25:([[12, 6, 21, 13], [(12, 13), (6, 12), (21, 6), (13, 21)]]),
    26:([[25, 6, 14, 19, 14, 12, 11, 6], [(25, 14), (6, 14), (14, 14), (19, 14), (14, 14), (12, 6), (11, 6), (6, 19)]]),
    27:([[10, 3, 14, 23, 11, 7, 10], [(10, 7), (3, 10), (14, 7), (23, 10), (11, 7), (7, 14), (10, 10)]]),
    28:([[24, 19, 19, 21, 10, 13, 13, 11, 1], [(24, 19), (19, 13), (19, 10), (21, 13), (10, 1), (13, 19), (13, 10), (11, 11), (1, 13)]]),
    29:([[20, 24, 13, 22, 5], [(20, 22), (24, 5), (13, 20), (22, 24), (5, 5)]]),
    30:([[26, 3, 25, 26, 25, 25, 20, 16], [(26, 20), (3, 25), (25, 20), (26, 26), (25, 16), (25, 25), (20, 3), (16, 25)]]),
    31:([[4, 14, 3, 25, 17, 3, 12, 18, 3], [(4, 14), (14, 3), (3, 14), (25, 25), (17, 18), (3, 12), (12, 17), (18, 3), (3, 14)]]),
    32:([[25, 4, 15, 14, 16], [(25, 16), (4, 16), (15, 25), (14, 16), (16, 14)]]),
    33:([[19, 5, 13, 14, 21, 5, 2], [(19, 5), (5, 5), (13, 14), (14, 5), (21, 13), (5, 5), (2, 21)]]),
    34:([[26, 2, 13, 15, 15, 19, 10], [(26, 19), (2, 10), (13, 10), (15, 13), (15, 15), (19, 26), (10, 13)]]),
    35:([[13, 24, 15, 17, 20, 4], [(13, 15), (24, 4), (15, 13), (17, 17), (20, 17), (4, 15)]]),
    36:([[25, 26, 1, 1, 23, 18, 15], [(25, 23), (26, 26), (1, 15), (1, 23), (23, 15), (18, 18), (15, 25)]])

}