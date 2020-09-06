from .board import Board


def block():
    return Board.from_string_data(
        '    ',
        ' ## ',
        ' ## ',
        '    ',
    )


def beehive():
    return Board.from_string_data(
        '      ',
        '  ##  ',
        ' #  # ',
        '  ##  ',
        '      ',
    )


def loaf():
    return Board.from_string_data(
        '      ',
        '  ##  ',
        ' #  # ',
        '  # # ',
        '   #  ',
        '      ',
    )


def boat():
    return Board.from_string_data(
        '     ',
        ' ##  ',
        ' # # ',
        '  #  ',
        '     ',
    )


def tub(): 
    return Board.from_string_data(
        '     ',
        '  #  ',
        ' # # ',
        '  #  ',
        '     ',
    )


def blinker():
    return Board.from_string_data(
        '     ',
        '  #  ',
        '  #  ',
        '  #  ',
        '     ',
    )


def toad():
    return Board.from_string_data(
        '      ',
        '      ',
        '  ### ',
        ' ###  ',
        '      ',
        '      ',
    )


def beacon():
    return Board.from_string_data(
        '      ',
        ' ##   ',
        ' ##   ',
        '   ## ',
        '   ## ',
        '      ',
    )


def pulsar():
    return Board.from_string_data(
        '                 ',
        '                 ',
        '    ###   ###    ',
        '                 ',
        '  #    # #    #  ',
        '  #    # #    #  ',
        '  #    # #    #  ',
        '    ###   ###    ',
        '                 ',
        '    ###   ###    ',
        '  #    # #    #  ',
        '  #    # #    #  ',
        '  #    # #    #  ',
        '                 ',
        '    ###   ###    ',
        '                 ',
        '                 ',
    )


def pentadecathlon():
    return Board.from_string_data(
        '                  ',
        '                  ',
        '                  ',
        '                  ',
        '      #    #      ',
        '    ## #### ##    ',
        '      #    #      ',
        '                  ',
        '                  ',
        '                  ',
        '                  ',
    )


def glider():
    return Board.from_string_data(
        '     ',
        ' #   ',
        '  ## ',
        ' ##  ',
        '     ',
    )


def lightweight_spaceship():
    return Board.from_string_data(
        '        ',
        '  ##    ',
        ' ####   ',
        ' ## ##  ',
        '   ##   ',
        '        ',
        '        ',
    )

