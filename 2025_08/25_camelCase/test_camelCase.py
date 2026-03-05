import main_camelCase as mcc 

if __name__ == "__main__":
    # Test1
    if mcc.to_camel_case("hello world") == "helloWorld":
        print("Test1: PASSED")
    else:
        print("Test1: FAILED")
    
    # Test2
    if mcc.to_camel_case("HELLO WORLD") == "helloWorld":
        print("Test2: PASSED")
    else:
        print("Test2: FAILED")
    
    # Test3
    if mcc.to_camel_case("secret agent-X") == "secretAgentX":
        print("Test3: PASSED")
    else:
        print("Test3: FAILED")
    
    # Test4
    if mcc.to_camel_case("FREE cODE cAMP") == "freeCodeCamp":
        print("Test4: PASSED")
    else:
        print("Test4: FAILED")
    
    # Test5
    if mcc.to_camel_case("ye old-_-sea  faring_buccaneer_-_with a - peg__leg----and a_parrot_ _named- _squawk") == "yeOldSeaFaringBuccaneerWithAPegLegAndAParrotNamedSquawk":
        print("Test5: PASSED")
    else:
        print("Test5: FAILED")
    


