# -*- coding: utf-8 -*-
def to_array(liczba):
    liczba = ''.join(liczba.split())
    cyfry = list(liczba)
    j = []
    t = []
    m = []
    for i in range(len(liczba)):
        x = len(liczba) - i - 1
        l = liczba[i] + x*"0"
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

    array_result = [m,t,j]
    return array_result


def arr2string(array_result):
    words_array = []
    for x in array_result:
        fix_teens(x)
        if x == []:
            words_array.append("")
        elif x == [1]:
            if x is array_result[0]:
                words_array.append(["milion"])
            elif x is array_result[1]:
                words_array.append(["tysiąc"])
            else:
                words_array.append(with_words(x))
        else:
            words_array.append(with_words(x))

    for x in range(len(array_result)):
        if array_result[x] == []:
            continue
        # Milions
        elif array_result[x] is array_result[0]:
            if array_result[x][-1] >= 2 and array_result[x][-1] <= 4:
                words_array[x].append("miliony")
            elif array_result[x][-1] > 1:
                words_array[x].append("milionów")
        # Thousands
        elif array_result[x] is array_result[1]:
            if array_result[x][-1] >= 2 and array_result[x][-1] <= 4:
                words_array[x].append("tysiące")
            elif len(array_result[x]) > 1 or array_result[x][-1] > 1:
                words_array[x].append("tysięcy")
        words_array[x] = " ".join(words_array[x])

    words = " ".join(filter(lambda x: x != "", words_array))
    return words

def fix_teens(a):
    if len(a) > 1 and a[-1] < 10:
        if a[-2] <= 10:
            a[-2] = a[-1] + a[-2]
            del a[-1]
    return a

def with_words(number_array):
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
        return list(map(lambda n: words[n],number_array))
    except KeyError as e:
        raise ValueError(f"Niepoprawna liczba {e}")

def money(amount):
    if amount == None:
        raise ValueError("Wartość 'None' nie jest liczbą!")
    amount = ''.join(amount.split())
    if "-" in amount:
        raise ValueError("Podana wartość jest niepoprawna!")
    try:
        zlotowki, grosze = amount.split('.')
        if grosze == "":
            grosze = 0
    except ValueError:
        zlotowki = str(amount)
        grosze = 0
    if int(grosze) != 0:
        if len(grosze) == 1:
            grosze = grosze + "0"
        grosze = str(int(grosze))
        gr = arr2string(to_array(grosze[0:2]))
        if gr == "jeden":
            gr = gr + " grosz"
        elif gr.split(' ')[-1] in ['dwa', 'trzy', 'cztery']:
            gr = gr + " grosze"
        else:
            gr = gr + " groszy"
    else:
        gr = ""

    if int(zlotowki) != 0:
        zl = arr2string(to_array(zlotowki))
        if zl == "jeden":
            zl = zl + " złoty"
        elif zl.split(' ')[-1] in ['dwa', 'trzy', 'cztery']:
            zl = zl + " złote"
        else:
            zl = zl + " złotych"
    else:
        if gr == "":
            zl = "zero złotych"
        else:
            zl = ""

    return f"{zl} {gr}".strip()

if __name__ == "__main__":
    import sys
    print(money(sys.argv[1]))
