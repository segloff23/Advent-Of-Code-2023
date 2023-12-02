


def withMap(source):
    return list(map(int, source))

def withList(source):
    return [int(i) for i in source]


N = 100000
source = [str(i) for i in range(N)]

for i in range(100):
    withMap(source)
    withList(source)
