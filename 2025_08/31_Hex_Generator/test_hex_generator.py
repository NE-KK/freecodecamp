import main_hex_generator as mhg

if __name__ == "__main__":
    # test 1
    if mhg.generate_hex("yellow") == "Invalid color":
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # test 2
    if len(mhg.generate_hex("red")) == 6:
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

