'''
Simulate a rat moving around on a table.
'''

import sys
import struct

from src.table import Table
from src.rat import Rat
from src.commands import apply_commands_by_id

# Settings
INT_BYTE_LENGTH = 4 # Assuming 32-bit integers
DEBUG = False # Simple debugging

def main(input, output):
    '''
    Main function.
    '''
    numbers = make_number_gen(input)

    table_width, table_height = next(numbers), next(numbers)
    rat_pos_x, rat_pos_y = next(numbers), next(numbers)

    table = Table(table_width, table_height)
    rat = Rat(rat_pos_x, rat_pos_y)

    apply_commands_by_id(numbers, rat, table, DEBUG)
    write_rat_position(rat, output)


def make_number_gen(input):
    '''
    Returns number generator function that reads from input.
    '''
    num = read_int(input)

    while num != None:
        yield num
        num = read_int(input)


def read_int(input):
    '''
    Returns integer read from input.
    '''
    bytes = input.buffer.read(INT_BYTE_LENGTH)
    return bytes_to_int(bytes) if len(bytes) == INT_BYTE_LENGTH else None


def write_int(output, value):
    '''
    Writes integer to output.
    '''
    bytes = int_to_bytes(value)
    output.buffer.write(bytes)


def bytes_to_int(bytes):
    '''
    Returns integer converted from bytes.
    '''
    return struct.unpack_from('i', bytes)[0]


def int_to_bytes(value):
    '''
    Returns bytes converted from integer.
    '''
    return int(value).to_bytes(INT_BYTE_LENGTH, sys.byteorder)


def write_rat_position(rat, output):
    '''
    Writes rat position to output.
    '''
    rat_pos_x, rat_pos_y = rat.get_position()

    if DEBUG:
        output.write(f'Rat position: {rat_pos_x},{rat_pos_y}')
    else:
        write_int(output, rat_pos_x)
        write_int(output, rat_pos_y)


if __name__ == '__main__':
    # Kick-off!
    main(sys.stdin, sys.stdout)
