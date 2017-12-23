def solution(S):
    if (len(S) == 0):
        return 0
    TOB = len([x for x in S if x == '('])
    TCB = len([x for x in S if x == ')'])
    ob, cb = 0, 0
    result = len(S)

    for i, e in enumerate(S):
        if ob == TCB - cb:
            result = i
            break
        if e == '(':
            ob += 1
        if e == ')':
            cb += 1
    #   assert result == slow_solution(S)
    return result

# def slow_solution(S):
#
#    for i in range(len(S)):
#        ob = len([x for x in S[:i] if x == '('])
#        cb = len([x for x in S[i:] if x == ')'])
#        if (ob == cb):
#            print(i, S[:i], S[i:], ob == cb)
#            return i
#    ob = len([x for x in S if x == '('])
#    cb = 0
#
#    print(len(S), S, ob == cb)
#    return len(S)

print(solution('(())'))