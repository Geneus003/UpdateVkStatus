# This function will generate string


def do_it(data):
    if len(data) == 0:
        return "Отдыхаю"

    strochka = "Прямо сейчас он "

    for i in range(len(data)):
        if strochka == "Прямо сейчас он ":
            strochka += data[i][0].lower()
            strochka += data[i][1:len(data[i])]
            continue

        if i == len(data) - 1:
            strochka += ", и "
            strochka += data[i][0].lower()
            strochka += data[i][1:len(data[i])]
            continue

        strochka += ", "
        strochka += data[i][0].lower()
        strochka += data[i][1:len(data[i])]

    strochka += ". Напишите ему)"

    return strochka
