# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    #write your code here
    _segment = namedtuple('_segment', 'start end length needed')

    _segments = list(map(lambda x: _segment(x[0], x[1], x[1] - x[0], True), segments))
    # print(sorted(_segments, key=lambda seg: seg.length))
    # _segments = sorted(_segments, key=lambda seg: seg.length, reverse=True)
    _segments = sorted(_segments, key=lambda seg: seg.start)

    _tmp_segments = _segments

    for i in range(len(_segments) - 1):
        for j in range(1, len(_segments) - i):
            if _segments[i + j].start <= _segments[i].end <= _segments[i + j].end and _segments[i].needed:
            # if _segments[i + j].start <= _segments[i].end <= _segments[i + j].end:
                _tmp_segments[i + j] = _tmp_segments[i + j]._replace(needed=False)
                # print(_tmp_segments)
    # print(_segments)

    for k in range(len(_tmp_segments)):
        if _tmp_segments[k].needed:
            points.append(_tmp_segments[k].end)

    return sorted(points)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    # print('n')
    # print(n)
    # print("data")
    # print(data)

    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
