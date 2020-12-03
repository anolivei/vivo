# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    bitmap_args.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anolivei <anolivei@student.42sp.org>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/28 21:22:46 by anolivei          #+#    #+#              #
#    Updated: 2020/12/02 22:31:58 by anolivei         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import sys
import json

def bitmap():
    A = np.array(json.loads(sys.argv[1]))
    M = np.array(json.loads(sys.argv[2]))
    print 'The vector is:', A
    print 'The matrix is: ', M
    ret=[]
    for i in range(len(A)):
        ret.append(np.sum(M == A[i]))
    print "The frequency of vector's elements in the matrix is:", ret

if __name__ == '__main__':
    bitmap()
