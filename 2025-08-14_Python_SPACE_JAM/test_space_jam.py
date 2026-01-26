import main_space_jam

"""
1. space_jam("freeCodeCamp") should return "F  R  E  E  C  O  D  E  C  A  M  P".
2. space_jam("   free   Code   Camp   ") should return "F  R  E  E  C  O  D  E  C  A  M  P".
3. space_jam("Hello World?!") should return "H  E  L  L  O  W  O  R  L  D  ?  !".
4. space_jam("C@t$ & D0g$") should return "C  @  T  $  &  D  0  G  $".
5. space_jam("allyourbase") should return "A  L  L  Y  O  U  R  B  A  S  E".
"""

if __name__ == "__main__":
    # print(main_space_jam.space_jam("Hello"))
    # Test 1:
    if main_space_jam.space_jam("freeCodeCamp") == "F  R  E  E  C  O  D  E  C  A  M  P":
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")

    # Test 2:
    if main_space_jam.space_jam("   free   Code   Camp   ") == "F  R  E  E  C  O  D  E  C  A  M  P":
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")

    # Test 3:
    if main_space_jam.space_jam("Hello World?!") == "H  E  L  L  O  W  O  R  L  D  ?  !":
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")

    # Test 4:
    if main_space_jam.space_jam("C@t$ & D0g$") == "C  @  T  $  &  D  0  G  $":
        print("Test 4: PASSED")
    else:
        print("Test 4: FAILED")

    # Test 5:
    if main_space_jam.space_jam("allyourbase") == "A  L  L  Y  O  U  R  B  A  S  E":
        print("Test 5: PASSED")
    else:
        print("Test 5: FAILED")
