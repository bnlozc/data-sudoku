# pylint: disable=missing-docstring

EXPECTED_NUMBERS = set(range(1,10))

def is_valid_group(numbers):
    return set(numbers) == EXPECTED_NUMBERS


def sudoku_validator(grid):
    for row in grid:
        if not is_valid_group(row):
            return False

    for column_index in range(9):
        column = []
        for row_index in range(9):
            column.append(grid[row_index][column_index])

        if not is_valid_group(column):
            return False

    for box_row in range(0, 9, 3):
        for box_column in range(0, 9, 3):
            box = []

            for row_index in range(box_row, box_row +3):
                for column_index in range(box_column, box_column +3):
                    box.append(grid[row_index][column_index])

            if not is_valid_group(box):
                return False
    return True
