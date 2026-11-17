
def cup_of_join(*lists, sep:str='-'):
    if len(lists) == 0:
        return None

    if any(not isinstance((unexpected:=i), list) for i in lists):
        raise TypeError(f'expected a list, got: {type(unexpected)}')

    res = []
    for list_i in lists:
        res += [sep] + list_i
    return res

if __name__ == '__main__':
    print(cup_of_join([1,2,3],[4,5,6]))
    print(cup_of_join([1,2,3],[4,5,6], sep='@'))
    print(cup_of_join())