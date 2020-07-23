# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:51:09 2020

@author: user
"""
board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    bag = [];
    answer = 0;
    N = range(len(board))

    # 가방 만들기
    for i in moves:
        for j in N:
            if board[j][i - 1]:
                bag.append(board[j][i - 1])
                board[j][i - 1] = 0
                print(bag)
                break
            else:
                pass

        # 가방 터뜨리기
    while True:
        for ix in range(len(bag)):  # 0~6, 하나는 pass
            if len(bag) >= 2:
                if bag[ix] == bag[ix + 1]:
                    bag = bag[:ix] + bag[ix + 2:]
                    answer += 2
                    print(bag)
                    print(answer)
                    break

                else:
                    pass

    return answer


answer = solution(board, moves)