def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();
    print("--- Begin report of books/frankenstein.txt ---");
    print(f"{len(file_contents.split())} words found in the document");
    book_stats = count_characters(file_contents);
    for key, value in book_stats.items():
        print(f"The '{key}' character was found {value} times");
    print("--- End report ---");

def count_characters(book):
    book_stats = {};
    for c in book.lower():
        if not c.isalpha():
            continue;
        if c in book_stats:
            book_stats[c] += 1;
        else :
            book_stats[c] = 1;
    return book_stats;

main();