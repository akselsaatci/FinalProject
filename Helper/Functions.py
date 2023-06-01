def enum_itere_et(enumList):
    #Enumları dolaşıp içindekileri tupple olarak döner
    result = []
    for data in enumList:
        result.append((data.name,data.value))
    return result

def inputu_enumda_valide_et(enumList, input):
    #Enumdaki değerlerden biriyle eşleşiyorsa True döner
    for data in enumList:
        if data.value == input:
            return True
    return False