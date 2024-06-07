def minion_game(string):
    string_upper = string.upper()
    n = len(string_upper)

    starts_vowel = 0
    starts_consonants = 0

    vowels = ['A','E', 'I', 'O', 'U']
    
    if (n <= 0 or n >= 10**6):
        print('Insert a valid input')
        return
        
    for i in range(n):

        if (string_upper[i] in vowels):
            starts_vowel += len(string_upper[i:n])

        else:
            starts_consonants += len(string_upper[i:n])

    if (starts_consonants > starts_vowel):
        print(f'Kevin {starts_consonants}')

    else:
        print(f'Stuart {starts_vowel}')


s = input()
minion_game(s)