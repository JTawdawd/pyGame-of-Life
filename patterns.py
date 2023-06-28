
def Gosper_Glider_Gun(grid):
    grid[4][0] = 1
    grid[4][1] = 1
    grid[5][0] = 1
    grid[5][1] = 1

    grid[2][34] = 1
    grid[2][35] = 1
    grid[3][34] = 1
    grid[3][35] = 1

    grid[12][34] = 1
    grid[12][35] = 1
    grid[12][36] = 1
    grid[13][33] = 1
    grid[13][37] = 1
    grid[14][32] = 1
    grid[14][38] = 1
    grid[15][32] = 1
    grid[15][38] = 1
    grid[16][35] = 1
    grid[17][33] = 1
    grid[17][37] = 1
    grid[18][34] = 1
    grid[18][35] = 1
    grid[18][36] = 1
    grid[19][35] = 1

    grid[22][0] = 1
    grid[23][0] = 1
    grid[24][1] = 1
    grid[24][2] = 1
    grid[24][3] = 1
    grid[25][1] = 1
    grid[26][2] = 1

    return grid

def Pulsar(grid):
    grid[2][4] = 1
    grid[2][5] = 1
    grid[2][6] = 1
    grid[2][10] = 1
    grid[2][11] = 1
    grid[2][12] = 1
    grid[4][2] = 1
    grid[4][7] = 1
    grid[4][9] = 1
    grid[4][14] = 1
    grid[5][2] = 1
    grid[5][7] = 1
    grid[5][9] = 1
    grid[5][14] = 1
    grid[6][2] = 1
    grid[6][7] = 1
    grid[6][9] = 1
    grid[6][14] = 1
    grid[7][4] = 1
    grid[7][5] = 1
    grid[7][6] = 1
    grid[7][10] = 1
    grid[7][11] = 1
    grid[7][12] = 1
    grid[9][4] = 1
    grid[9][5] = 1
    grid[9][6] = 1
    grid[9][10] = 1
    grid[9][11] = 1
    grid[9][12] = 1
    grid[10][2] = 1
    grid[10][7] = 1
    grid[10][9] = 1
    grid[10][14] = 1
    grid[11][2] = 1
    grid[11][7] = 1
    grid[11][9] = 1
    grid[11][14] = 1
    grid[12][2] = 1
    grid[12][7] = 1
    grid[12][9] = 1
    grid[12][14] = 1
    grid[14][4] = 1
    grid[14][5] = 1
    grid[14][6] = 1
    grid[14][10] = 1
    grid[14][11] = 1
    grid[14][12] = 1

    return grid
