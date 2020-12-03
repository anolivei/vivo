# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bitmap.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/28 21:22:46 by anolivei          #+#    #+#              #
#    Updated: 2020/12/02 21:42:49 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def bitmap(A, M):
    print 'The vector is:', A
    print 'The matrix is: ', M
    ret=[]
    for i in range(len(A)):
        ret.append(np.sum(M == A[i]))
    print "The frequency of vector's elements in the matrix is:", ret

if __name__ == '__main__':
    # Define your vector here
    A = np.array([0, 1, 2, 6])
    # Define your matrix here
    M = np.array([[0, 0, 5 , 7, 8, 9],[1, 1, 8, 9, 2, 3]])
    bitmap(A, M)
