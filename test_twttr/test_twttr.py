from twttr import shorten


def test_shorten():
    assert shorten("vasif") == "vsf"
    assert shorten("BANKAI") == "BNK"
    assert shorten("1") == "1"
    assert shorten(".") == "."