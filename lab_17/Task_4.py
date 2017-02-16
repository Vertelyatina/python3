def do_queens_beat_each_other(queens):
    '''Returns the conclusion if at least two queens beat each other.'''
    x = [queen[0] for queen in queens]
    y = [queen[1] for queen in queens]
    sums = [sum(queen) for queen in queens]
    diffs = [queen[1] - queen[0] for queen in queens]

    # If they are at the same line, they do
    if len(x) != len(set(x)) or len(y) != len(set(y)):
        return 'YES'
    # If they are at the same diagonals, they do
    elif len(sums) != len(set(sums)) or len(diffs) != len(set(diffs)):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    queens = []
    for i in range(8):
        queens.append([int(c) for c in input().split()])
    print(do_queens_beat_each_other(queens))
