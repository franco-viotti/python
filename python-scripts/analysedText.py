import string

fmtText = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

'''
!Now this is a real comment.
'''
fmtText = fmtText.lower()
fmtText = fmtText.translate(str.maketrans('', '', string.punctuation))

def freqAll(fmtText):    
    split_list = fmtText.split()
    aux_list = []
    aux_list.append(split_list[0])
    for i in split_list:
        print("i is:",i)
        print(type(i))
        print(aux_list)
        print(type(aux_list))
        print(type(split_list))
        for j in aux_list:
            print("j is:", j)
            print("i is:", i)
            if i != j:
                aux_list.append(i)
    print(split_list)
    print(aux_list)
freqAll(fmtText)
