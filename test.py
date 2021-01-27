'''
Simple test.
'''

from src.table import Table
from src.rat import Rat
from src import commands

QUIT = commands.CMD_QUIT
FORWARD = commands.CMD_MOVE_RAT_FORWARD
BACKWARDS = commands.CMD_MOVE_RAT_BACKWARDS
ROT_RIGHT = commands.CMD_ROTATE_RAT_RIGHT
ROT_LEFT = commands.CMD_ROTATE_RAT_LEFT

def run_test():
    table = Table(4, 4)
    rat = Rat(2, 2)
    cmd_ids = get_command_ids()

    commands.apply_commands_by_id(cmd_ids, rat, table, True)
    rat_pos_x, rat_pos_y = rat.get_position()

    print(f'Rat position: {rat_pos_x},{rat_pos_y}')
    assert(rat_pos_x == 0 and rat_pos_y == 1)


def get_command_ids():
    return [
        FORWARD,
        ROT_LEFT,
        FORWARD,
        ROT_RIGHT,
        BACKWARDS,
        ROT_RIGHT,
        BACKWARDS,
        ROT_LEFT,
        FORWARD,
        QUIT,
    ]


if __name__ == '__main__':
    run_test()
