import matplotlib.pyplot as plt
import string
class CharHelper:
    def plot_ngram_frequency(ngram_counts, ngram_type):
        ngrams = list(ngram_counts.keys())
        frequencies = list(ngram_counts.values())

        plt.bar(ngrams, frequencies)
        plt.xlabel(ngram_type)
        plt.ylabel('Frequency')
        plt.title(f'Frequency {ngram_type} in Encrypted Text')
        plt.xticks(rotation=90)
        plt.show()
    
    def count_letter_freq(text):
        freq = {}
        for char in text:
            if char.isalpha():
                char = char.lower()
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
        return freq

    def count_word_freq(text):
        freq = {}
        for word in text.split():
            word = word.strip(string.punctuation)
            if word.isalpha():
                word = word.lower()
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        return freq
    
    def count_bigram_freq(text):
        freq = {}
        words = text.split()
        for i in range(len(words)-1):
            word1 = words[i].strip(string.punctuation).lower()
            word2 = words[i+1].strip(string.punctuation).lower()
            if word1.isalpha() and word2.isalpha():
                bigram = word1 + " " + word2
                if bigram in freq:
                    freq[bigram] += 1
                else:
                    freq[bigram] = 1
        return freq

    def count_trigram_freq(text):
        freq = {}
        words = text.split()
        for i in range(len(words)-2):
            word1 = words[i].strip(string.punctuation).lower()
            word2 = words[i+1].strip(string.punctuation).lower()
            word3 = words[i+2].strip(string.punctuation).lower()
            if word1.isalpha() and word2.isalpha() and word3.isalpha():
                trigram = word1 + " " + word2 + " " + word3
                if trigram in freq:
                    freq[trigram] += 1
                else:
                    freq[trigram] = 1
        return freq

    def count_special_char_freq(text):
        freq = {}
        for char in text:
            if not char.isalnum() and char not in string.whitespace:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
        return freq
    
    def main(filename):
        with open(filename, 'r') as f:
            text = f.read()
        letter_freq = CharHelper.count_letter_freq(text)
        word_freq = CharHelper.count_word_freq(text)
        bigram_freq = CharHelper.count_bigram_freq(text)
        trigram_freq = CharHelper.count_trigram_freq(text)
        special_char_freq = CharHelper.count_special_char_freq(text)

        print(f'Text {text}')
        print(f'Letter Frequency {letter_freq}')
        print(f'Word Frequency {word_freq}')
        print(f'Bigram Frequency {bigram_freq}')
        print(f'Trigram Frequency {trigram_freq}')
        print(f'Special Character Frequency {special_char_freq}')

        CharHelper.plot_ngram_frequency(letter_freq, 'Letter')
        CharHelper.plot_ngram_frequency(word_freq, 'Word')
        CharHelper.plot_ngram_frequency(bigram_freq, 'Bigram')
        CharHelper.plot_ngram_frequency(trigram_freq, 'Trigram')
        CharHelper.plot_ngram_frequency(special_char_freq, 'Special Character')
        