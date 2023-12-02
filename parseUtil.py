import re

###############################################################################

def split_to_map(chunk, delim="\n", getter=lambda x: x):
    if delim == "":
        return map(getter, chunk)
    return map(getter, chunk.split(delim))

def split_to_list(chunk, delim="\n", getter=lambda x: x):
    return list(split_to_map(chunk, delim, getter))

def split_to_tuple(chunk, delim="\n", getter=lambda x: x):
    return tuple(split_to_map(chunk, delim, getter))

def split_to_dict(chunk, delim="\n", getter=lambda x: x):
    return dict(split_to_map(chunk, delim, getter))

def split_to_set(chunk, delim="\n", getter=lambda x: x):
    return set(split_to_map(chunk, delim, getter))

###############################################################################

def to_map(data, mapper):
    return map(mapper, data)

def to_list(data, mapper):
    return list(to_map(data, mapper))

def to_tuple(data, mapper):
    return tuple(to_map(data, mapper))

def to_dict(data, mapper):
    return dict(to_map(data, mapper))

def from_pattern(pattern, builder, getter=lambda x: x, asDict=True, default=None):
    if (asDict):
        return lambda chunk: builder({ k:getter(v) for k,v in re.match(pattern, chunk).groupdict().items() })
    return lambda chunk:builder(*[getter(v) for v in re.match(pattern, chunk).groups()])

def apply_with_default(value, default, operation=lambda x: x):
    if (not value):
        return default
    return operation(value)

###############################################################################

def to_transpose(array):
    R, C = len(array), len(array[0])
    return [[array[r][c] for r in range(R)] for c in range(C)]

###############################################################################

days = {}

with open('01/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read(),
        delim="\n\n",
        getter=lambda chunk: sum(split_to_tuple(
            chunk,
            getter=int
        ))
    )
    days[1] = parsed

with open('02/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read(),
        getter=lambda chunk: split_to_tuple(
            chunk,
            delim=" "
        )
    )
    days[2] = parsed

with open('03/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read()
    )
    days[3] = parsed

with open('04/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read(),
        getter=from_pattern(
            r"(\d+)-(\d+),(\d+)-(\d+)",
            lambda a,b,c,d: ((a, b), (c, d)),
            getter=int,
            asDict=False
        )
    )
    days[4] = parsed

with open('05/problem.txt', 'r') as f:
    top, bottom = f.read().split("\n\n")

    top_parsed = to_tuple(
        to_transpose(split_to_list(
            top,
            getter=lambda chunk: [c for c in chunk[1::4]]
        )),
        lambda row: "".join(row[:-1]).strip()
    )

    bottom_parsed = split_to_list(
        bottom,
        getter=from_pattern(
            r"move (\d+) from (\d+) to (\d+)",
            lambda a,b,c: (a, b-1, c-1),
            getter=int,
            asDict=False
        )
    )

    days[5] = (top_parsed, bottom_parsed)

with open('09/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read(),
        getter=from_pattern(
            r"(\w) (\d+)",
            lambda a,b: (a, int(b)),
            asDict=False
        )
    )
    days[9] = parsed

with open('10/problem.txt', 'r') as f:
    parsed = split_to_list(
        f.read(),
        getter=from_pattern(
            r"(\w+)(( -?\d+)*)?",
            lambda a, b, _: (
                a,
                apply_with_default(
                    b.strip(),
                    tuple(),
                    operation=lambda nums: split_to_tuple(nums, delim=" ", getter=int)
                )
            ),
            asDict=False
        )
    )
    days[10] = parsed

with open('11/problem.txt', 'r') as f:
    pattern = re.compile(
r"""Monkey (?P<index>\d+):
  Starting items: (?P<items>(\d+(, \d+)*))
  Operation: new = (?P<operation>((old)|[ +*/-]|(\d+))*)
  Test: divisible by (?P<divisor>\d+)
    If true: throw to monkey (?P<ifTrue>\d+)
    If false: throw to monkey (?P<ifFalse>\d+)""")

    def buildCondition(divisor, ifTrue, ifFalse):
        return lambda x: ifTrue if x % divisor == 0 else ifFalse

    parsed = split_to_list(
        f.read(),
        delim="\n\n",
        getter=from_pattern(
            pattern,
            lambda D: (
                split_to_tuple(D["items"], delim=",", getter=int),
                eval("lambda old: " + D["operation"]),
                buildCondition(*to_map((D["divisor"], D["ifTrue"], D["ifFalse"]), int)),
                int(D["divisor"])
            )
        )
    )

    days[11] = parsed

with open('16/problem.txt', 'r') as f:
    parsed = split_to_dict(
        f.read(),
        getter=from_pattern(
            r"Valve (?P<valve>\w{2}) has flow rate=(?P<flow>\d+); tunnels? leads? to valves? (?P<neighbors>\w{2}(, \w{2})*)?",
            lambda D: (
                D["valve"],
                (int(D["flow"]), split_to_tuple(D["neighbors"], delim=", "))
            ),
        )
    )
    days[16] = parsed

with open('18/problem.txt', 'r') as f:
    parsed = split_to_set(
        f.read(),
        getter=lambda chunk: split_to_tuple(chunk, delim=",", getter=int)
    )
    days[18] = parsed

# 19 and 21