def converseVowel(text):
    vowels = [] 
    for t in text.lower():
        if t in 'aeiou':  
            vowels.append(t)
    return vowels

phrase = str(input('Digite uma frase: '))
vowels = converseVowel(phrase)  
print(f'A frase "{phrase}" tem {len(vowels)} vogais: {vowels}')
