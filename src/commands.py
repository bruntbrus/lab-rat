'''
Commands for rat on table.
'''

# Command ID:s
CMD_QUIT = 0
CMD_MOVE_RAT_FORWARD = 1
CMD_MOVE_RAT_BACKWARDS = 2
CMD_ROTATE_RAT_RIGHT = 3
CMD_ROTATE_RAT_LEFT = 4

def get_command(cmd_id):
    '''
    Returns command function by ID.
    '''
    return _COMMANDS[cmd_id]


def apply_command(cmd, rat, table, verbose=False):
    '''
    Applies command function to rat and table.
    '''
    if verbose:
        print(cmd.__doc__.strip())

    return cmd(rat, table)


def apply_commands_by_id(cmd_ids, rat, table, verbose=False):
    '''
    Applies command functions by sequence of command ID:s.
    '''
    for cmd_id in cmd_ids:
        cmd = get_command(cmd_id)

        if not apply_command(cmd, rat, table, verbose):
            break


def _cmd_quit(rat, table):
    '''
    Command: Quit
    '''
    return False


def _cmd_move_rat_forward(rat, table):
    '''
    Command: Move rat forward
    '''
    rat.move_forward()
    return _check_rat(rat, table)


def _cmd_move_rat_backwards(rat, table):
    '''
    Command: Move rat backwards
    '''
    rat.move_backwards()
    return _check_rat(rat, table)


def _cmd_rotate_rat_right(rat, table):
    '''
    Command: Rotate rat right
    '''
    rat.rotate_right_90()
    return True


def _cmd_rotate_rat_left(rat, table):
    '''
    Command: Rotate rat left
    '''
    rat.rotate_left_90()
    return True


def _is_rat_on_table(rat, table):
    '''
    Returns True if rat is on table, else returns False.
    '''
    x, y = rat.get_position()
    return x >= 0 and y >= 0 and x < table.get_width() and y <= table.get_height()


def _check_rat(rat, table):
    '''
    Returns True if rat is on table, else kills rat and returns False.
    '''
    if not _is_rat_on_table(rat, table):
        _kill_rat(rat)
        return False

    return True


def _kill_rat(rat):
    '''
    Kills rat (sets position to -1, -1).
    '''
    rat.set_position(-1, -1)


# Command functions in specific order.
_COMMANDS = [
    _cmd_quit,
    _cmd_move_rat_forward,
    _cmd_move_rat_backwards,
    _cmd_rotate_rat_right,
    _cmd_rotate_rat_left,
]
