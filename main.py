from requests import get
from bs4 import BeautifulSoup as BS
from pandas import DataFrame as DF


print("Параметры FROM и TO записываются следующим образом:\n "
      "Целым чсилом пишется сначала номер дня, а затем без каких-либо "
      "знаков сразу время (00 или 12). Например: \n100 - певый день "
      "месяца 00 часов или 1412 - 14 день месяца в 12 часов.")
parametrs = {
    "YEAR": int(input("Год: ")),
    "MONTH": int(input("Месяц: ")),
    "FROM": int(input("FROM: ")),
    "TO": int(input("TO: ")),
    "STNM": int(input("Станция: "))  # Station number
}
address = "http://weather.uwyo.edu/cgi-bin/sounding?region=europe&TYPE=TEXT%3ALIST&YEAR={p[YEAR]}&MONTH={p[MONTH]}&FROM={p[FROM]}&TO={p[TO]}&STNM={p[STNM]}"
full_text = get(address.format(p=parametrs)).text
soup = BS(full_text, 'lxml')


def formula(p, t, F):
    T = float(t) + 273.15
    E = 6.1 * 10 ** ((7.45 * T) / (235 + T))
    return (78.5 / T) * (float(p) + 48 * float(F) * E / T)


data = []
for stat_table in soup.find_all("pre")[::2]:
    half_day_data, i = [], -1
    for data_string in str(stat_table)[319:-7].split("\n")[1:]:
        line_data = data_string.split()
        if len(line_data) == 11:
            line_data.append(formula(*line_data[:5:2]))
            i += 1
            if i > 0:
                line_data.append((float(half_day_data[i - 1][-1]) - float(line_data[-1])) /
                                 (float(half_day_data[i - 1][1]) - float(line_data[1])))
        half_day_data.append(line_data)
    half_day_data[0].append(half_day_data[1][-1])
    data += half_day_data

DF(data).to_excel(str(soup.h2)[10:-5].replace(" ", "_") + ".xlsx")