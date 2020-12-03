# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bitmap.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/28 21:22:46 by anolivei          #+#    #+#              #
#    Updated: 2020/12/02 21:35:55 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import Counter
import numpy as np

def bitmap(A, M):
    print 'The vector is:', A
    print 'The matrix is: ', M
    ret =  dict(sum(map(Counter, M), Counter()))
    print (ret)
    res = [ret[i] for i in A if i in ret]
    print (res)
    print (A.shape)
    c = []
    print (np.sum(M == A[3]))
    i = 0
    while (i < 4):
        c.append(np.sum(M == A[i]))
        i+=1
    c=[]
    for i in range(len(A)):
        c.append(np.sum(M == A[i]))
    print (c)

if __name__ == '__main__':
    A = np.array([0, 1, 2, 6])
    M = np.array([[0, 0, 5 , 7, 8, 9],[1, 1, 8, 9, 2, 3]])
    bitmap(A, M)
