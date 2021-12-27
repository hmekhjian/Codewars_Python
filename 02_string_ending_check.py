def solution(string, ending):
    length = len(ending)
    if string[-length:] == ending:
        return True
    else:
        return False


print(solution("abc", "bc"))  # returns true
print(solution("abc", "d"))  # returns false


