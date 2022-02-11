# # Полигоны
# import pygame as pg
# from cmath import sqrt, inf
# from random import randint
#
# #
# # def nearest_point(x, y, coordinates):
# #     min_coord, near_point = inf, coordinates[0]
# #     for coord in coordinates:
# #         length = sqrt(pow(x - coord[0], 2) + pow(y - coord[1], 2)).real
# #         if length < min_coord:
# #             min_coord, near_point = length, coord
# #     return near_point
# #
# #
# # coordinates = open(r"C:\Users\Dima\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\scratch.txt", "r").read()
# # coordinates = [(round(float(pair.split()[0])*111, 2), round(float(pair.split()[1])*111, 2)) for pair in coordinates.replace(",", ".").split("\n")]
# #
# # coordinates_T = list(zip(*coordinates))
# # minx, maxx = int(min(coordinates_T[0])), int(max(coordinates_T[0])) + 1
# # miny, maxy = int(min(coordinates_T[1])), int(max(coordinates_T[1])) + 1
# # poligons = {coord: [] for coord in coordinates}
# # print(minx, maxx, miny, maxy)
# # for i in range(minx, maxx, 2):
# #     for j in range(miny, maxy, 2):
# #         poligons[nearest_point(i, j, coordinates)].append((i, j))
# #
# # open(r"C:\Users\Dima\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\result_poligons_for_drawing.txt", "w").write(str(poligons))
#
#
# pg.init()
# running = True
# pg.display.set_caption('Полигоны')
# display = pg.display.set_mode((1400, 700))
#
# poligons = eval(open(r"C:\Users\Dima\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\result_poligons_for_drawing.txt", "r").read())
# flag = True
# while running:
#     if flag:
#         for point in poligons.keys():
#             COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
#             for pair in poligons[point]:
#                 pg.draw.rect(display, COLOR, (pair[0]//10, pair[1]//100, 1, 1))
#             break
#         pg.display.flip()
#         flag = False
#
#     print(flag)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             running = False


links = """1 https://youtu.be/3LlBAE-w09o
2 https://youtu.be/cAlCeJR1x2w
3 https://youtu.be/9sVlVKndLKk
4 https://youtu.be/VZ2U3HCQge0
5 https://youtu.be/_rXDdDLEUVA
6 https://youtu.be/SdQPnUFqi_E
7 https://youtu.be/XHrniFCX-jk
8 https://youtu.be/rRoZTShEw0Y
9 https://youtu.be/1v9jEDp3m8M
10 https://youtu.be/aQRGp8FJ4os
11 https://youtu.be/ry8ZloPKJL4
12 https://youtu.be/PXcE1xmAId8
13 https://youtu.be/bvePJdKo7aA
14 https://youtu.be/-sQqQjuCnIY
15 https://youtu.be/aMJsBIi0M9E
16 https://youtu.be/0KdclEC1CRs
17 https://youtu.be/x5ZKy_-7my0
18 https://youtu.be/Nj6_euWaS7Y
19 https://youtu.be/umRCRdRe8Nc
20 https://youtu.be/ykfnSfDHZms
21 https://youtu.be/AmfGHz26kQg
22 https://youtu.be/kEJzX5szQQI
23 https://youtu.be/h8O6JVqlBvA
24 https://youtu.be/p-VMU4_tqjs
25 https://youtu.be/7oy-ahMGxWc
26 https://youtu.be/rVpu38Z7VPw
27 https://youtu.be/zdJz--yAjns
28 https://youtu.be/hH098llAAfo
29 https://youtu.be/liUlsm0DNvU
30 https://youtu.be/6pjF3AmD_84
31 https://youtu.be/frexrGw3fbY
32 https://youtu.be/HRb8toHJV8Q
33 https://youtu.be/1D-sBzKCmjI
34 https://youtu.be/ofg4YXKQ08w
35 https://youtu.be/o7egWnHibgs
36 https://youtu.be/FQkBqm5U_aQ
37 https://youtu.be/Vlp_wiFshXo
38 https://youtu.be/zxcaoBQ7Fko
39 https://youtu.be/cHbI4a1uauw
40 https://youtu.be/84cAq7fyfcE
41 https://youtu.be/J3zmXJtcuIU
42 https://youtu.be/VJYSbZsSOqo
43 https://youtu.be/3OuUDVkFauY
44 https://youtu.be/ef5IWFRvic4
45 https://youtu.be/XySQCTI12ro
46 https://youtu.be/fFS7fkHBrGE
47 https://youtu.be/p5994Da_cZY
48 https://youtu.be/utCyT5-a5nw
50 https://youtu.be/-UwloMCjcSI
51 https://youtu.be/_wKWvmGMXfc
52 https://youtu.be/ccCV9L-ENLA
53 https://youtu.be/c84zejD6TDc
54 https://youtu.be/nfj4dCd9Qak
55 https://youtu.be/KQz7YXy57SE
56 https://youtu.be/owh_kk79ROA
59 https://youtu.be/9TTA2kTV3Ig
60 https://youtu.be/bype7WF3lwQ
63 https://youtu.be/zCKVet_2y60
66 https://youtu.be/PTMO2MGyxNM
67 https://youtu.be/SN53lLj_wJ8
68 https://youtu.be/VLSgYbDQ1TM
69 https://youtu.be/aFDZe19GlfU
70 https://youtu.be/YWp56plHBlo
71 https://www.youtube.com/watch?v=jnm1RjlczVI
72 https://youtu.be/04hqzx6xI_s
73 https://youtu.be/fF5DJEsyRYw
74 https://youtu.be/qwagi4k7L9E
75 https://youtu.be/4x2AjgwxyOY
76 https://youtu.be/kRVDq3jYJh4
77 https://youtu.be/RBQdKfMjHCw
78 https://youtu.be/HFXMIP0QdO8
79 https://youtu.be/Qanm4o_O7hY
80 https://youtu.be/7d-RKWFUsr8
81 https://youtu.be/kfmyNvO5crY
85 https://youtu.be/CbYxmrnpJSg
86 https://youtu.be/pDtqTfx6JEQ
87 https://youtu.be/2Mw6tCgIeQ4
88 https://youtu.be/N46ltkZVZYM
89 https://youtu.be/WhJJrPnBFWU
91 https://youtu.be/krAUql8T1Ks
92 https://youtu.be/3_zf268RZJQ
93 https://youtu.be/0xTauApwbCI
94 https://youtu.be/8FJ-0UX3_Aw https://youtu.be/iGOQw5Aq254
95 https://youtu.be/qS65cAoTG6s
96 https://youtu.be/BCZAIVGgSoM
"""

from pytube import YouTube as YT
from pathlib import Path


path = input("Введите полный путь до папки, в которую скачать видосы. Например: C:\\Users\\Dima\\Desktop\\BachataChallenge\n")

Path(path).mkdir(parents=True, exist_ok=True)

for i, link in enumerate(links.replace(" ", "\n").split("\n")[1::2]):
	print(f"Ссылка №{i+1} {link}", end="\t")
	yt = YT(link)
	try:
		yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(path)
		print(f"№{i+1} ссылка скачалась : {link}")
	except:
		print(f"№{i+1} ссылка НЕ скачалась : {link}")
