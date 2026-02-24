def count_words(text):
    words = text.split()
    return len(words)
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count
def reverse_text(text):
    return text[::-1]
def is_palindrome(text):
    clean_text = text.replace(" ","").lower()
    return clean_text == clean_text[::-1]    
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for ch in text:
        if ch not in vowels:
            result += ch
    return result  
def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
          if len(word)  > len(longest):
               longest = word
    return longest 
def analyze_text(text):
    print("\n===== TEXT ANALYSIS====")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))      
    if is_palindrome(text):
        print("Palindrome: Yes") 
    else:
     print("Palindrome: No")
    print("Without vowels:", remove_vowels(text))
    longest = longest_word(text)
    print(f"Longest word: {longest}({len(longest)}letters)")
    freq = word_frequency(text)
    print("Word Frequency(text)")
    print("Word Frequency:", end=" ")
    for word, count in freq.items():
         print(f"{word}: {count}",end=",")
         print()
text = input("Enter text: ")
analyze_text(text)        

