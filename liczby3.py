# -*- coding: utf-8 -*-
def money(number):
    if number == None or '-' in number:
        raise ValueError("Niepoprawna wartość")
    number = ''.join(number.split())
    try:
        zlotowki, grosze = number.split(".")
    except ValueError:
        zlotowki = number
        grosze = 0
        gr_word = ""
    if int(zlotowki):
        zlotowki = to_array(zlotowki)
        zl_word = arr2words(zlotowki)
        zl_word = " ".join(filter(lambda x: x != "", zl_word))
    else:
        zl_word = ""
    if grosze:
        if len(grosze) == 1:
            grosze += "0"
        grosze = str(int(grosze))
        grosze = to_array(grosze[:2])
        gr_word = arr2words(grosze)
        gr_word = " ".join(filter(lambda x: x != "", gr_word))
        if gr_word == "jeden":
            gr_word += " grosz"
        elif gr_word.split(" ")[-1] in ["dwa", "trzy", "cztery"]:
            gr_word += " grosze"
        elif gr_word:
            gr_word += " groszy"
    else:
        gr_word = ""

    if not zl_word and not gr_word:
        return "zero złotych"

    elif zl_word:
        if zl_word == "jeden":
            zl_word += " złoty"
        elif zl_word.split(" ")[-1] in ["dwa", "trzy", "cztery"]:
            zl_word += " złote"
        else:
            zl_word += " złotych"

    return f"{zl_word} {gr_word}".strip()

def to_array(num):
    numbers = list(num)
    m = []
    t = []
    j = []

    for i in range(len(num)):
        x = len(num) - i - 1
        l = num[i] + x*"0"
        l = int(l)
        if l > 0:
            if l >= 1000:
                l = l // 1000
                if l >= 1000:
                    l = l // 1000
                    m.append(l)
                else:
                    t.append(l)
            else:
                j.append(l)
    arr_res = to_teens([m, t, j])
    return arr_res

def to_teens(arr):
    for x in arr:
        if len(x) >= 2:
            if x[-1] > 0 and x[-2] < 20:
                x[-2] += x[-1]
                del x[-1]
    return arr

def arr2words(array):
    words_arr = []
    words = {
        1: "jeden",
        2: "dwa",
        3: "trzy",
        4: "cztery",
        5: "pięć",
        6: "sześć",
        7: "siedem",
        8: "osiem",
        9: "dziewięć",
        10: "dziesięć",
        11: "jedenaście",
        12: "dwanaście",
        13: "trzynaście",
        14: "czternaście",
        15: "piętnaście",
        16: "szesnaście",
        17: "siedemnaście",
        18: "osiemnaście",
        19: "dziewiętnaście",
        20: "dwadzieścia",
        30: "trzydzieści",
        40: "czterdzieści",
        50: "pięćdziesiąt",
        60: "sześćdziesiąt",
        70: "siedemdziesiąt",
        80: "osiemdziesiąt",
        90: "dziewięćdziesiąt",
        100: "sto",
        200: "dwieście",
        300: "trzysta",
        400: "czterysta",
        500: "pięćset",
        600: "sześćset",
        700: "siedemset",
        800: "osiemset",
        900: "dziewięćset"
    }
    try:
        for arg in array:
            words_arr.append(list(map(lambda x: words[x], arg)))
    except KeyError:
        raise ValueError("Niepoprawna wartość")
    grammar(words_arr)
    return words_arr

def grammar(array):
    for i in range(len(array)):
        if array[i]:
            if array[i] == ["jeden"]:
                if array[i] is array[0]:
                    array[i] = ["milion"]
                elif array[i] is array[1]:
                    array[i] = ["tysiąć"]
            elif array[i][-1] in ["dwa", "trzy", "cztery"]:
                if array[i] is array[0]:
                    array[i].append("miliony")
                elif array[i] is array[1]:
                    array[i].append("tysiące")
            else:
                if array[i] is array[0]:
                    array[i].append("milionów")
                elif array[i] is array[1]:
                    array[i].append("tysięcy")
        array[i] = " ".join(array[i])

if __name__ == "__main__":
    import sys
    print(money(sys.argv[1]))
