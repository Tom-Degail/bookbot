def wordCount(text):
    return len(text.split())


def charCount(text):
    textLowered = text.lower()
    dict = {} 
    for c in textLowered:
       if dict.get(c) == None:
        dict[c] = 1
       else:
        dict[c] +=1
    return dict     

            