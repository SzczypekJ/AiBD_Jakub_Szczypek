from app import hello

def test_hello():
    got = hello("Aleksandra")
    want = "Hello Aleksandra"

    assert got == want