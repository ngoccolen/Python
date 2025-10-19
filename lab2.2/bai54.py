def format_word_list(words):
    if not words:
        return ""
    elif len(words) == 1:
        return words[0]
    elif len(words) == 2:
        return f"{words[0]} and {words[1]}"
    else:
        return ", ".join(words[:-1]) + " and " + words[-1]
def main():
    words = []
    print("Nhập các từ (bỏ trống để dừng):")
    while True:
        word = input("Từ: ").strip()
        if word == "":
            break
        words.append(word)

    formatted = format_word_list(words)
    print("\nKết quả:")
    print(formatted)
if __name__ == "__main__":
    main()
