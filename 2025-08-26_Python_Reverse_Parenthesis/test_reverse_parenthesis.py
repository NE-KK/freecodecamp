import main_reverse_parenthesis as mrp


if __name__ == "__main__":
    # Test 1
    if mrp.decode("(f(b(dc)e)a)") == "abcdef":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    # Test 2
    if mrp.decode("((is?)(a(t d)h)e(n y( uo)r)aC)") == "Can you read this?":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    # Test 3
    if mrp.decode("f(Ce(re))o((e(aC)m)d)p") == "freeCodeCamp":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")
