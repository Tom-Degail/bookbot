from stats import wordCount
from stats import charCount
 
def get_book_text(path):
   with open(path) as f:
       content = f.read() 
   return content

def main():
    content = get_book_text("./books/frankenstein.txt")
    print(f"Found {wordCount(content)} total words")
    dict = charCount(content)
    print(dict)
main()