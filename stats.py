def wordCount(text):
    return len(text.split())


def charCount(text):
    textLowered = text.lower()
    dict ={} 
    for c in textLowered:
       if dict.get(c) == None:
        dict[c] = 1
       else:
        dict[c] +=1
    return dict     

def dictSorted(dic):
    L = []
    for i in dic:
        L.append({"name" : i, "num" : dic.get(i)})
    L.sort(reverse = True, key= lambda item: item["num"])
    return L


dic = charCount("Bonjour je suis Tom")
print(dictSorted (dic))

            