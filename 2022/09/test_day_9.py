from day9 import move_tail

def test_move_tail():
    assert move_tail((0, 0), (0, 0)) == (0, 0)
    assert move_tail((0, 1), (0, 0)) == (0, 0)
    assert move_tail((1, 1), (0, 0)) == (0, 0)
    assert move_tail((1, 0), (0, 0)) == (0, 0)
    assert move_tail((1, -1), (0, 0)) == (0, 0)
    assert move_tail((0, -1), (0, 0)) == (0, 0)
    assert move_tail((-1, -1), (0, 0)) == (0, 0)
    assert move_tail((-1, 0), (0, 0)) == (0, 0)
    assert move_tail((-1, 1), (0, 0)) == (0, 0)


    assert move_tail((0, 2), (0, 0)) == (0, 1)
    assert move_tail((0, -2), (0, 0)) == (0, -1)
    assert move_tail((2, 0), (0, 0)) == (1, 0)
    assert move_tail((-2, 0), (0, 0)) == (-1, 0)
    assert move_tail((1, 2), (0, 0)) == (1, 1)
    assert move_tail((-1, -2), (0, 0)) == (-1, -1)
    assert move_tail((2, 1), (0, 0)) == (1, 1)
    assert move_tail((-2, -1), (0, 0)) == (-1, -1)
    assert move_tail((-1, 2), (0, 0)) == (-1, 1)
    assert move_tail((1, -2), (0, 0)) == (1, -1)
    assert move_tail((2, -1), (0, 0)) == (1, -1)
    assert move_tail((-2, 1), (0, 0)) == (-1, 1)
