#!/usr/bin/python3
'''Contains a method that determines if a given data set represents
a valid UTF-8 ecnoding
'''


def validUTF8(data: list) -> bool:
    '''Checks if a given data set is a valid UTF-8
    '''
    cnt = 0
    for num in data:
        if type(num) == int:
            if not cnt:
                base = 128
                while base & num:
                    cnt += 1
                    base >>= 1
                if not cnt:
                    continue
                if cnt == 1 or cnt > 4:
                    return False
            else:
                if num >> 6 != 0b10:
                    return False
        else:
            return False
    return cnt == 0
