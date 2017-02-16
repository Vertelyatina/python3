if __name__ == '__main__':

    n = int(input())
    grasshoppers = [int(jump_length) for jump_length in list(input().split())]
    time = int(input())

    for i in range(time):
        if grasshoppers[-1] < n-1:
        # Concatenate the list of waiting grasshoppers
            grasshoppers = grasshoppers[:n-1-grasshoppers[-1]]\
                           + [grasshoppers[-1]]\
                           + grasshoppers[n-1-grasshoppers[-1]:-1]
        else:
        # It is the first grasshopper
            grasshoppers = [grasshoppers[-1]] + grasshoppers[:-1]

    print(*grasshoppers)
