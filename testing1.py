# built in python testing

def good():
    assert 1 == 1

def bad():
    assert 1 != 1

def main():
    good()
    bad()

main()