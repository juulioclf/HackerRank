def minion_game(string):
    n = len(string)
    if (n <= 0 or n > 10000000):
        print('Insert a valid input')
        return False

    starts_vowel = 0
    starts_consonants = 0

    vowels = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(n):

        if (string[i] in vowels):
            starts_vowel += n - i

        else:
            starts_consonants += n - i

    if (starts_consonants > starts_vowel):
        print(f'Stuart {starts_consonants}')

    if (starts_consonants == starts_vowel):
        print('Draw')

    if (starts_consonants < starts_vowel):
        print(f'Kevin {starts_vowel}')

if __name__ == '__main__':
    s = input()
    minion_game(s)