import main_jbelmud_text as mjt

if __name__ == "__main__":
    # test 1
    if mjt.jbelmu("hello world") == "hello wlord":
        print("Test 1: PASSED")
    else:
        print("Test 1: FAILED")
    
    # test 2
    if mjt.jbelmu("i love jumbled text") == "i love jbelmud text":
        print("Test 2: PASSED")
    else:
        print("Test 2: FAILED")
    
    # test 3
    if mjt.jbelmu() == "":
        print("Test 3: PASSED")
    else:
        print("Test 3: FAILED")
