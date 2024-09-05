def count_strings_with_identical_ends(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0].lower() == s[-1].lower():  # Added .lower() to handle case sensitivity
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
