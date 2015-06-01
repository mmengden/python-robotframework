def LetterCount(string):
    """
    Return the first word with the greatest number of repeated letters or -1 otherwise
    """
    if string == "":
        return -1
        
    if not isinstance(string, str):
        return -1
        
    string_arr = string.split()
    count = []
    
    for i, s in enumerate(string_arr):
        count.append(0)
        dbls = []
        for j in range(len(s)):
            if s[j] in dbls:
                count[i] = count[i] + 1
            dbls.append(s[j])
    max_dbl = max(count)
    max_dbl_i = count.index(max_dbl)
    
    for element in count:
        if element != 0:
            return string_arr[max_dbl_i]
    return -1
    
def main():
    first = LetterCount("Hello apple pie")
    assert (first == "Hello")
    
    second = LetterCount("")
    assert (second == -1), "Blank strings should return -1"
    
    third = LetterCount("No doubles")
    assert (third == -1)
    
    fourth = LetterCount("The Legend of Zelda: Ocarina of Time is the greatest game ever!")
    assert (fourth == "greatest"), "fourth test should be equal to greatest"
    
    fifth = LetterCount(11)
    assert (fifth == -1), "Non strings should return -1"
    
    print("Huzzah! All tests passed!")
    
if __name__ == "__main__":
    main()


