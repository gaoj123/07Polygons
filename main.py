from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()



#RUNS MR. DW'S SCRIPT
parse_file( 'script', edges, transform, screen, color )

#parse_file( 'script2', edges, transform, screen, color )
edges = []

#RUNS MY WREATH SCRIPT
parse_file( 'wreath', edges, transform, screen, color )
