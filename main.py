file = open("D:\\.Repo\\Kanji_to_Hantu\\hantu&nghia.txt", mode = "r", encoding="utf8")
datas = file.read().split("\n")
hantu, nghia = [], []

for i in range(len(datas)):
    data = datas[i].split(" ")
    hantu.append(data[0])
    nghia.append(data[1])

file2 = open("D:\\.Repo\\Kanji_to_Hantu\\ghep.txt", mode = "r", encoding="utf8")
datas2 = file2.read().split("\n")

file3 = open("D:\\.Repo\\Kanji_to_Hantu\\tuvung.txt", mode = "r", encoding="utf8")
datas3 = file3.read().split("\n")

file4 = open("D:\\.Repo\\Kanji_to_Hantu\\z_end.txt", mode = "w", encoding="utf8")

for i in range(len(datas3)):
    tu = datas3[i]
    nghia_cua_tu = []
    for ki_tu in tu:
        if ki_tu in hantu:
            nghia_cua_tu.append(nghia[hantu.index(ki_tu)])
    file4.write(datas2[i] + " " + (" ").join(nghia_cua_tu) + "\n")
