import main_character_battle as mcb

if __name__ == "__main__":
    # Test1
    if mcb.battle("Hello", "World") == "We lost":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    # Test2
    if mcb.battle("pizza", "salad") == "We won":
        print("Test2: PASSED")
    else:
        print("Test2: FAILED")

    # Test3
    if mcb.battle("C@T5", "D0G$") == "We won":
        print("Test3: PASSED")
    else:
        print("Test3: FAILED")

    # Test4
    if mcb.battle("kn!ght", "orc") == "Opponent retreated":
        print("Test4: PASSED")
    else:
        print("Test4: FAILED")

    # Test5
    if mcb.battle("PC", "Mac") == "We retreated":
        print("Test5: PASSED")
    else:
        print("Test5: FAILED")

    # Test6
    if mcb.battle("Wizards", "Dragons") == "It was a tie":
        print("Test6: PASSED")
    else:
        print("Test6: FAILED")

    # Test7
    if mcb.battle("Mr. Smith", "Dr. Jones") == "It was a tie":
        print("Test7: PASSED")
    else:
        print("Test7: FAILED")
