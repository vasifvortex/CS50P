from um import count

def test_count():
    assert count("um") == 1
    assert count("mum") == 0
    assert count(" um ") == 1
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2
