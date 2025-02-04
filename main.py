from collections import Counter 

def main(): 
  book_path = 'books/frankenstein.txt'
  text = getBookText(book_path)
  count = getLenText(text)
  stringNumber = stringCount(text)
  stringAggregate = stringCharList(stringNumber, count)
  #print(f"{count} words found in the document")
  #print(stringNumber)

def getBookText(book_path):
  with open(book_path) as f:
    return f.read()
  
def getLenText(text):
  words = text.split()
  return len(words)

def stringCount(text):
  #Could be done like this
  # textLower = text.lower()
  # return Counter(textLower)
  chars = {}
  for c in text:
    lowered = c.lower()
    if lowered in chars:
      chars[lowered] += 1
    else: 
      chars[lowered] = 1
  return(chars)

def stringCharList(stringCount, word_count):
  charList = []
  for char, count in stringCount.items():
    if(char.isalpha() == True):
      newDict = {"char": char, "num": count}
      charList.append(newDict)
  charList.sort(reverse=True, key=sort_on)
  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document\n")  # \n adds a blank line
    
  for char_dict in charList:
      print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
  print("--- End report ---")

# def stringReport(stringCharList, count):
#     print("--- Begin report of books/frankenstein.txt ---")
#     print(f"{count} words found in the document\n")  # \n adds a blank line
    
#     for char_dict in charList:
#         print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
#     print("--- End report ---")

def sort_on(dict):
  return dict["num"]

main()