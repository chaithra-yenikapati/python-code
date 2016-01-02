__author__ = 'Chaithra'

from placeholders import *

# instead of returning a list of tuples like zip, generate it incrementally (refer to the generators and iterators lessons)
# a tuple at a time. Use exception control flow to write elegant code.
def generator_zip(seq1, seq2, *more_seqs):
    str1 = iter(seq1)
    str2 = iter(seq2)
    result = []
    for x in more_seqs:
        result.append(iter(x))
    while True:
        try:
            sequen = []
            sequen.append(next(str1))
            sequen.append(next(str2))
            for x in result:
                sequen.append(next(x))
            yield tuple(sequen)
        except StopIteration as se:
            raise StopIteration






def check_generator(gen, max_count, tuple_length):
    for x in range(max_count):
        result = next(gen)
        assert len(result) == tuple_length, "invalid length"
        for element in result:
            assert x == element, "unexpected value"

    try:
        next(gen)
        assert False, "generator did not finish as expected"
    except StopIteration as se:
        pass

def test_generator_zip():
    gen = generator_zip(range(5), range(3), range(4), range(5))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 3, 4)

    gen = generator_zip(range(5), range(3), range(2))
    assert type(gen).__name__ == 'generator'
    check_generator(gen, 2, 3)

    gen = generator_zip(range(1,5), "abc", [1,2])
    assert [(1,'a', 1), (2, 'b', 2)] == list(gen)

    gen = generator_zip((1,2), "abcd")
    assert [(1,'a'), (2, 'b')] == list(gen)

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___