from stats import wordCount
from stats import charCount 
from stats import dictSorted
import sys 

def get_book_text(path):
   with open(path) as f:
       content = f.read() 
   return content

def main():
    if(len(sys.argv)<2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filePath = sys.argv[1]
    content = get_book_text(filePath)
    dic = charCount(content)
    listChar = dictSorted(dic)
    print( "============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount(content)} total words")
    print("--------- Character Count -------")
    for i in listChar:
        print(f"{i["name"]}: {i["num"]}")
    print("============= END ===============")

main()