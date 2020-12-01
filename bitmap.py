# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bitmap.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/28 21:22:46 by anolivei          #+#    #+#              #
#    Updated: 2020/12/01 02:03:01 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import Counter

def bitmap(A, M):
    print (A)
    print (M)
    ret =  dict(sum(map(Counter, M), Counter()))
    print (ret)
    res = [ret[i] for i in A if i in ret]
    print (res)

if __name__ == '__main__':
    A = ([0, 1, 2])
    M = ([[0, 0, 5 , 7, 8, 9],[1, 1, 8, 9, 2, 3]])
    bitmap(A, M)
