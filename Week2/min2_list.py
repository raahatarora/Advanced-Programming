# To determine the strings with minimum 2 characters and also same start and end character from a list of 15 strings

def count_strings_with_identical_ends(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count


strings = [
    'Ava',     
    'Ben',
    'Civic',   
    'David',
    'Eve',    
    'Felicity',
    'Gog',     
    'Hannah',  
    'I',
    'Jill',
    'Kayak',   
    'Liam',
    'Madam',   
    'Nina',    
    'Otto'  
]


count = count_strings_with_identical_ends(strings)
print("Count of strings with min length of 2 and identical start and end characters:", count)
