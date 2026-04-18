#Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

#Examples
#"Hi!" --> "H!!"
#"!Hi! Hi!" --> "!H!! H!!"
#"aeiou" --> "!!!!!"
#"ABCDE" --> "!BCD!"

def replace_exclamation(s):
    vowels = "aeiouAEIOU"
    result = ""
    
    for ch in s:
        if ch in vowels:
            result += "!"
        else:
            result += ch
            
    return result
