# Python News Article Text Analysis Assessment
file = open("news_article.txt", "r", encoding="utf-8")
text = file.read()
file.close()

def count_specific_word(text, search_word):
    if text == "" or search_word == "":
        return 0

    words = text.lower().split()
    count = 0

    for word in words:
        word = word.strip(".,!?")
        if word == search_word.lower():
            count += 1

    return count

def identify_most_common_word(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word = word.strip(".,!?")
        if word:  # Only count non-empty words
            word_count[word] = word_count.get(word, 0) + 1
    return max(word_count, key=word_count.get) if word_count else ""

def calculate_average_word_length(text):
    words = text.lower().split()
    if not words:
        return 0
    total_length = sum(len(word.strip(".,!?")) for word in words)
    return total_length / len(words)

def count_paragraphs(text):
    paragraphs = text.split("\n\n")
    return len([p for p in paragraphs if p.strip()])

def count_sentences(text):
    sentences = text.replace("!", ".").replace("?", ".").split(".")
    return len([s for s in sentences if s.strip()])

def main():
    while True:
        print("\n--- News Article Analysis ---")
        word = input("Enter a word to count (or type exit to stop): ")
        if word.lower() == "exit":
            break
        else:
            print("Word count:", count_specific_word(text, word))
            print("Most common word:", identify_most_common_word(text))
            print("Average word length:", calculate_average_word_length(text))
            print("Paragraphs:", count_paragraphs(text))
            print("Sentences:", count_sentences(text))


if __name__ == "__main__":
    main()