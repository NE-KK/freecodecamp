import main_message_decoder


if __name__ == "__main__":
    # Test 1
    if main_message_decoder.decode("Xlmw mw e wigvix qiwweki.", 4) == "This is a secret message.":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")

    # Test 2
    if main_message_decoder.decode("Byffi Qilfx!", 20) == "Hello World!":
        print("Test2: PASSED")
    else:
        print("Test2: FAILED")

    # Test 3
    if main_message_decoder.decode("Zqd xnt njzx?", -1) == "Are you okay?":
        print("Test3: PASSED")
    else:
        print("Test3: FAILED")

    # Test 4
    if main_message_decoder.decode("oannLxmnLjvy", 9) == "freeCodeCamp":
        print("Test4: PASSED")
    else:
        print("Test4: FAILED")

    



    main_message_decoder.decode("Byffi Qilfx!", 20)
    main_message_decoder.decode("Zqd xnt njzx?", -1)
    main_message_decoder.decode("oannLxmnLjvy", 9)
