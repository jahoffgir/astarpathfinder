"""
Introduction to Intelligent Systems
Year-Round Orienteering Lab 1
@author: Jahongir Amirkulov
@date: 03/06/18
"""
import sys
from PIL import Image

OPEN_LAND = "#F89412 (248,148,18)"
ROUGH_MEADOR = "#FFC000 (255,192,0)"
EASY_MOVEMENT = "#FFFFFF (255,255,255)"
SLOW_RUN = "#02D03C (2,208,60)"
WALK_FOREST = "#028828 (2,136,40)"
IMPOSSIBLE_VEGETATION = "#054918 (5,73,24)"
LAKE_SWAMP_MARSH = "#0000FF (0,0,255)"
PAVED_ROAD = "#473303 (71,51,3)"
FOOT_PATH = "#000000 (0,0,0)"
OUT_OF_BOUND = "#CD0065 (205,0,101)"


def main():
    try:
        terrain_image = sys.argv[1]
        elevation_file = sys.argv[2]
        path_file = sys.argv[3]
        season = sys.argv[4]
        output_image_filename = sys.argv[5]

    except Exception:
        print("No bueno!")


if __name__ == '__main__':
    main()

