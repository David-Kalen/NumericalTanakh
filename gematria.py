def value(x):
    ret = 0

    if x == 'א':
        ret = 1
    elif x == 'ב':
        ret = 2
    elif x == 'ג':
        ret = 3
    elif x == 'ד':
        ret = 4
    elif x == 'ה':
        ret = 5
    elif x == 'ו':
        ret = 6
    elif x == 'ז':
        ret = 7
    elif x == 'ח':
        ret = 8
    elif x == 'ט':
        ret = 9
    elif x == 'י':
        ret = 10
    elif x == 'כ' or x == 'ך':
        ret = 20
    elif x == 'ל':
        ret = 30
    elif x == 'מ' or x == 'ם':
        ret = 40
    elif x == 'נ' or x == 'ן':
        ret = 50
    elif x == 'ס':
        ret = 60
    elif x == 'ע':
        ret = 70
    elif x == 'פ' or x == 'ף':
        ret = 80
    elif x == 'צ' or x == 'ץ':
        ret = 90
    elif x == 'ק':
        ret = 100
    elif x == 'ר':
        ret = 200
    elif x == 'ש':
        ret = 300
    elif x == 'ת':
        ret = 400

    return ret


def 