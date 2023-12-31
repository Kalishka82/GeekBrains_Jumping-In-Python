#  Задание No2
# 📌 В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых.
# 📌 Не учитывать знаки препинания и регистр символов.
# 📌 За основу взять любую статью из википедии или из документации к языку.

import string


text = """
У кумушки-лисы зубушки остры, рыльце тоненькое, ушки на макушке, хвостик на отлёте, шубка тёпленькая.
Хорошо кума принаряжена: шерсть пушистая, золотистая; на груди жилет, а на шее белый галстучек.
Ходит лиса тихохонько, к земле пригибается, будто кланяется; свой пушистый хвост носит бережно, смотрит ласково, 
улыбается, зубки белые показывает.
Роет норы, умница, глубокие; много ходов в них и выходов, кладовые есть, есть и спаленки, мягкой травушкой полы 
выстланы.
Всем бы лисонька хороша была хозяюшка, да разбойница-лиса — хитрая: любит курочек, любит уточек, свернёт шею гусю 
жирному, не помилует и кролика.
Однажды Солнце и сердитый северный Ветер затеяли спор о том, кто из них сильнее. Долго спорили они и, наконец, 
решились померяться силами над путешественником, который в это самое время ехал верхом по большой дороге.
- Посмотри, - сказал Ветер, - как я налечу на него: мигом сорву с него плащ.
Сказал, - и начал дуть, что было мочи. Но чем более старался Ветер, тем крепче закутывался путешественник в свой плащ: 
он ворчал на непогоду, но ехал всё дальше и дальше. Ветер сердился, свирепел, осыпал бедного путника дождем и снегом; 
проклиная Ветер, путешественник надел свой плащ в рукава и подвязался поясом. Тут уж Ветер и сам убедился, что ему 
плаща не сдернуть.
Солнце, видя бессилие своего соперника, улыбнулось, выглянуло из-за облаков, обогрело, осушило землю, а вместе с тем 
и бедного полузамерзшего путешественника. Почувствовав теплоту солнечных лучей, он приободрился, благословил Солнце, 
сам снял свой плащ, свернул его и привязал к седлу.
- Видишь ли, - сказало тогда кроткое Солнце сердитому Ветру, - лаской и добротой можно сделать гораздо более, чем 
гневом.
У меня была мордашка… Её звали Булькой. Она была вся чёрная, только кончики передних лап были белые.
У всех мордашек нижняя челюсть длиннее верхней и верхние зубы заходят за нижние; но у Бульки нижняя челюсть так 
выдавалась вперёд, что палец можно было заложить между нижними и верхними зубами. Лицо у Бульки было широкое; глаза 
большие, чёрные и блестящие; и зубы и клыки белые всегда торчали наружу. Он был похож на арапа. Булька был смирный и 
не кусался, но он был очень силён и цепок. Когда он, бывало, уцепится за что-нибудь, то стиснет зубы и повиснет, 
как тряпка, и его, как клещука, нельзя никак оторвать.
Один раз его пускали на медведя, и он вцепился медведю в ухо и повис, как пиявка. Медведь бил его лапами, прижимал 
к себе, кидал из стороны в сторону, но не мог оторвать и повалился на голову, чтобы раздавить Бульку; но Булька до 
тех пор на нём держался, пока его не отлили холодной водой.
Я взял его щенком и сам выкормил. Когда я ехал служить на Кавказ, я не хотел брать его и ушёл от него потихоньку, а 
его велел запереть. На первой станции я хотел уже садиться на другую перекладную, как вдруг увидал, что по дороге 
катится что-то чёрное и блестящее. Это был Булька в своём медном ошейнике. Он летел во весь дух к станции. Он бросился 
ко мне, лизнул мою руку и растянулся в тени под телегой. Язык его высунулся на целую ладонь. Он то втягивал его назад, 
глотая слюни, то опять высовывал на целую ладонь. Он торопился, не поспевал дышать, бока его так и прыгали. 
Он поворачивался с боку на бок и постукивал хвостом о землю.
Я узнал потом, что он после меня пробил раму и выскочил из окна и прямо, по моему следу, поскакал по дороге и 
проскакал так вёрст двадцать в самый жар.
Набродили, наследили звери на снегу. Не сразу поймёшь, что тут было.
Налево под кустом начинается заячий след. От задних лап следок вытянутый, длинный; от передних — круглый, маленький.
Пошёл заячий след по полю. По одну сторону его — другой след, побольше; в снегу от когтей дырки — лисий след. А по другую сторону заячьего следа ещё след: тоже лисий, только назад ведёт. Заячий дал круг по полю; лисий — тоже. Заячий в сторону — лисий за ним.
Оба следа кончаются посреди поля.
А вот в стороне — опять заячий след. Пропадает, дальше идёт... Идёт, идёт, идёт — и вдруг оборвался — как под землю ушёл! А где пропал, там снег примят, и по сторонам будто кто пальцами мазнул.
Куда лиса делась? Куда заяц пропал? Разберём по складам. Стоит куст. С него кора содрана. Под кустом натоптано, наслежено. Следы заячьи. Тут заяц жировал: с куста кору глодал. Встанет на задние лапы, отдерёт зубами кусок, сжуёт, переступит лапами, рядом ещё кусок сдерёт.
Наелся и спать захотел. Пошёл искать, где спрятаться.
А вот — лисий след, рядом с заячьим. Было так: ушёл заяц спать. Час проходит, другой. Идёт полем лиса. Глядь, заячий след на снегу! Лиса нос к земле. Принюхалась — след свежий!
Побежала по следу. Лиса хитра, и заяц не прост: умел свой след запутать. Скакал, скакал по полю, завернул, выкружил большую петлю, свой же след пересёк — ив сторону.
След пока ещё ровный, неторопливый: спокойно шёл заяц, беды за собой не чуял.
Лиса бежала, бежала — видит: поперёк следа свежий след. Не догадалась, что заяц петлю сделал.
Свернула вбок — по свежему следу; бежит, бежит — и стала: оборвался след! Куда теперь?
А дело простое: это новая заячья хитрость — двойка.
Заяц сделал петлю, пересёк свой след, прошёл немного вперёд, а потом обернулся — и назад по своему следу.
Аккуратно шёл — лапка в лапку.
Лиса постояла, постояла — и назад. Опять к перекрестку подошла. Всю петлю выследила.
Идёт, идёт, видит — обманул её заяц, никуда след не ведёт!
Фыркнула она и ушла в лес по своим делам.
А было вот как: заяц двойку сделал — прошёл назад по своему следу.
До петли не дошёл — и махнул через сугроб — в сторону.
Через куст перескочил и залёг под кучу хвороста.
Тут и лежал, пока лиса его по следу искала.
А когда лиса ушла, — как прыснет из-под хвороста — ив чащу!
Прыжки широкие — лапки к лапкам: гонный след.
Мчит без оглядки. Пень по дороге. Заяц мимо. А на пне... А на пне сидел большой филин.
Увидал зайца, снялся, так за ним и стелет. Настиг и цап в спину всеми когтями!
Ткнулся заяц в снег, а филин насел, крыльями по снегу бьёт, от земли отрывает.
Где заяц упал, там снег примят. Где филин крыльями хлопал, там знаки на снегу от перьев, будто от пальцев.
Улетел заяц в лес. Оттого и следа дальше нет.
"""

MOST_FREQ = 10
punct = f'—{string.punctuation}'
print(punct)
for item in punct:
    text = text.replace(item, ' ')
words_list = text.lower().split()

qty_dict = {}
for item in words_list:
    key = qty_dict.setdefault(words_list.count(item), set([]))
    key.add(item)
print(qty_dict)

qty_set = sorted(qty_dict.keys(), reverse=True)

the_most_freq = []
for i in range(MOST_FREQ):
    the_most_freq.append(qty_dict.get(qty_set[i]))
print(the_most_freq)
