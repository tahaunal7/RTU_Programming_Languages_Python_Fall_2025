def count_characters(text):
    return len(text.replace(" ", ""))

def count_words(text):
    return len(text.split())

def extract_numbers(text):
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers

def analyze_text(text):
    chars = count_characters(text)
    words = count_words(text)
    nums = extract_numbers(text)
    total = sum(nums) if nums else 0
    avg = total / len(nums) if nums else 0
    return chars, words, total, avg

if __name__ == "__main__":
    text = input("Enter a sentence: ")
    chars, words, total, avg = analyze_text(text)
    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg:.2f}")
