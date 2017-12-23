
# def solution(A, B, C, D):
#    SQ_A = solution_A(A,B,C,D)
#    SQ_B = solution_B(A,B,C,D)
#    SQ_C = solution_C(A,B,C,D)
#    maxx = max(SQ_A,SQ_B,SQ_C)
#    print('A: {}, B: {}, C: {} ,A == max {}'.format(SQ_A,SQ_B,SQ_C, SQ_A == maxx))
#    return maxx

# def solution_B(A, B, C, D):
#    # write your code in Python 3.6
#    P1_Y, P1_X, P2_Y, P2_X = sorted([A,B,C,D])
#    SQ_V =  (P2_Y-P1_Y)**2+(P2_X-P1_X)**2
#    return SQ_V

# def solution_A(A, B, C, D):
#    P1_Y, P1_X, P2_X, P2_Y = sorted([A,B,C,D])
#    SQ_V =  (P2_Y-P1_Y)**2+(P2_X-P1_X)**2
#    return SQ_V

# def solution_C(A, B, C, D):
#    P1_Y, P2_Y, P1_X, P2_X = sorted([A,B,C,D])
#    SQ_V =  (P2_Y-P1_Y)**2+(P2_X-P1_X)**2
#    return SQ_V


def solution(A, B, C, D):
    P1_Y, P1_X, P2_X, P2_Y = sorted([A ,B ,C ,D])
    SQ_V =  (P2_Y -P1_Y )** 2 +(P2_X -P1_X )**2
    return SQ_V

print(solution(1,1,2,3))