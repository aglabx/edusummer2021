# https://www.codewars.com/kata/5266876b8f4bf2da9b000362
# Who likes it?

def likes(array):
    if len(array) <= 1:
        return "%s likes this" % (array[0] if len(array) == 1 else "no one")
    else:
        if 2 <= len(array) <= 3:
            array.insert(-1, 'and')
            if len(array) == 3:
                return "%s like this" % ' '.join(array)
            else:
                return "%s like this" % (', '.join(array[0:2]) + ' ' + ' '.join(array[2:]))
        else:
            cnt = len(array) - 2
            return "%s and %s others like this" % (', '.join(array[0:2]), cnt)
