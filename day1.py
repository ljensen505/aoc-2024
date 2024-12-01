from pprint import pprint
from utils import read_lines

filename = __file__.split(".")[0]

lines = read_lines(filename, testing=True)
pprint(lines)
