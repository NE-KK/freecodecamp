import main_unnatural_prime as mup


if __name__ == "__main__":
    if not mup.is_unnatural_prime(1):
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    if not mup.is_unnatural_prime(-1):
        print("Test2: PASSED")
    else:
        print("Test2: FAILED")

    if mup.is_unnatural_prime(19):
        print("Test3: PASSED")
    else:
        print("Test3: FAILED")

    if mup.is_unnatural_prime(-23):
        print("Test4: PASSED")
    else:
        print("Test4: FAILED")

    if not mup.is_unnatural_prime(0):
        print("Test5: PASSED")
    else:
        print("Test5: FAILED")

    if mup.is_unnatural_prime(97):
        print("Test6: PASSED")
    else:
        print("Test6: FAILED")

    if mup.is_unnatural_prime(61):
        print("Test7: PASSED")
    else:
        print("Test7: FAILED")

    if not mup.is_unnatural_prime(99):
        print("Test8: PASSED")
    else:
        print("Test8: FAILED")

    if not mup.is_unnatural_prime(-44):
        print("Test9: PASSED")
    else:
        print("Test9: FAILED")


