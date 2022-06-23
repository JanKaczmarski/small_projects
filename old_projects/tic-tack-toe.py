def draw_a_board(size_of_board):

    j = 0
    i = 0
    for i in range(size_of_board):
        print('---', end=' ')
        if i == size_of_board - 1:
            print()
    while (j < size_of_board):
        for i in range(size_of_board + 1):
            print('|', end='   ')
            if i == size_of_board:
                print()
                for i in range(size_of_board):
                    print('---', end=' ')
                    if i == size_of_board - 1:
                        print()
        j += 1

draw_a_board(3)


winner_is_2 = [[1, 1, 1],
               [1, 2, 0],
               [0, 1, 0]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]


def who_won(result_list):
    # Jeśli chociaż jeden element z górnego rzędu równa się 2 wykona się pierwszy if. Napraw to.

    if result_list[0][0] == result_list[1][0] and result_list[0][0] == result_list[2][0] and result_list[1][0] == result_list[2][0] and result_list[0][0] == 'x':
        return "Player 2 won"
    elif result_list[0][1] == result_list[1][1] and result_list[0][1] == result_list[2][1] and result_list[1][1] == result_list[2][1] and result_list[1][1] == 'x':
        return "Player 2 won"
    elif result_list[0][2] == result_list[1][2] and result_list[0][2] == result_list[2][2] and result_list[1][2] == result_list[2][2] and result_list[2][2] == 'x':
        return "Player 2 won"
    elif result_list[0][0] == result_list[1][1] and result_list[0][0] == result_list[2][2] and result_list[1][1] == result_list[2][2] and result_list[2][2] == 'x':
        return "Player 2 won"
    elif result_list[0][2] == result_list[1][1] and result_list[0][2] == result_list[2][0] and result_list[1][1] == result_list[2][0] and result_list[2][0] == 'x':
        return "Player 2 won"
    elif result_list[0][0] == result_list[0][1] and result_list[0][2] == result_list[0][0] and result_list[0][1] == result_list[0][2] and result_list[0][0] == 'x':
        return "Player 2 won"
    elif result_list[1][0] == result_list[1][1] and result_list[1][2] == result_list[1][0] and result_list[1][1] == result_list[1][2] and result_list[1][0] == 'x':
        return "Player 2 won"
    elif result_list[2][2] == result_list[2][0] and result_list[2][0] == result_list[2][1] and result_list[2][1] == result_list[2][2] and result_list[2][0] == 'x':
        return "Player 2 won"
    
    elif result_list[0][0] == result_list[1][0] and result_list[0][0] == result_list[2][0] and result_list[1][0] == result_list[2][0] and result_list[2][0] == 'o':
        return "Player 1 won"
    elif result_list[0][1] == result_list[1][1] and result_list[0][1] == result_list[2][1] and result_list[1][1] == result_list[2][1] and result_list[2][1] == 'o':
        return "Player 2 won"
    elif result_list[0][2] == result_list[1][2] and result_list[0][2] == result_list[2][2] and result_list[1][2] == result_list[2][2] and result_list[2][2] == 'o':
        return "Player 2 won"
    elif result_list[0][0] == result_list[1][1] and result_list[0][0] == result_list[2][2] and result_list[1][1] == result_list[2][2] and result_list[2][2] == 'o':
        return "Player 2 won"
    elif result_list[0][2] == result_list[1][1] and result_list[0][2] == result_list[2][0] and result_list[1][1] == result_list[2][0] and result_list[2][0] == 'o':
        return "Player 2 won"
    elif result_list[0][0] == result_list[0][1] and result_list[0][2] == result_list[0][0] and result_list[0][1] == result_list[0][2] and result_list[0][0] == 'o':
        return "Player 2 won"
    elif result_list[1][0] == result_list[1][1] and result_list[1][2] == result_list[1][0] and result_list[1][1] == result_list[1][2] and result_list[1][0] == 'o':
        return "Player 2 won"
    elif result_list[2][2] == result_list[2][0] and result_list[2][0] == result_list[2][1] and result_list[2][1] == result_list[2][2] and result_list[2][0] == 'o':
        return "Player 2 won"
    else:
        return "No winner"


players_coordinates = "1 2"
players_coordinates_list = players_coordinates.split()
print(players_coordinates_list)
empty_board = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]
players_numbers = [1, 2]
i = 0

while True:
    
    if i % 2 == 0:
        players_coordinates = input("Player 1, Choose coordinates. For example: 1 2: ")
        players_coordinates_list = players_coordinates.split()
        empty_board[int(players_coordinates_list[0]) - 1][int(players_coordinates_list[1]) - 1] = 'o'
        print(empty_board)
        i += 1
        if who_won(empty_board) == "No winner":
            continue
        elif who_won(empty_board) == "Player 1 won" or who_won(empty_board) == "Player 2 won":
            who_won(empty_board)
    elif i % 2 != 0:
        players_coordinates = input("Player 2, Choose coordinates. For example: 1 2: ")
        players_coordinates_list = players_coordinates.split()
        empty_board[int(players_coordinates_list[0]) - 1][int(players_coordinates_list[1]) - 1] = 'x'
        print(empty_board)
        i += 1
        if who_won(empty_board) == "No winner":
            continue
        if who_won(empty_board) == "Player 1 won" or who_won(empty_board) == "Player 2 won":
            who_won(empty_board)
