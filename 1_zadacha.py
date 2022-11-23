def solution(s):
    return [''.join(i) for i in zip(s[::2], s[1::2] + '_')]
