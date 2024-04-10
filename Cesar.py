# -*- coding: utf-8 -*-
# autor Evgeniy N
alf = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м",
       "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " ",
       "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
       "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
user_text = input("Введите свое сообщение для шифровки (только русские буквы в любом регистре): ")
user_list = []
user_index = []
for i in range(len(user_text)):
    user_list.append(user_text[i])

for k in range(len(user_list)):
    if user_list[k] in alf:
        user_index.append(alf.index(user_list[k]))

mod_ind = 0
user_mod_index = []
user_lis_mod = []
user_mess = ''
for kl in range(len(user_list)):
    # Задаем смещение вправо по алфовиту
    mod_ind = user_index[kl] + 6
    if user_index[kl] > 60:
        mod_ind = user_index[kl] + 6 - 66
        user_mod_index.append(mod_ind)
    else:
        user_mod_index.append(mod_ind)
    user_lis_mod.append(alf[user_mod_index[kl]])
    user_mess = user_mess + alf[user_mod_index[kl]]

print(user_mess)

user_txt_dsh = input("Введите сообщение для дешифровки (только русские буквы в любом регистре): ")
user_list_dsh = []
user_index_dsh = []
for ik in range(len(user_txt_dsh)):
    user_list_dsh.append(user_txt_dsh[ik])

for ks in range(len(user_list_dsh)):
    if user_list_dsh[ks] in alf:
        user_index_dsh.append(alf.index(user_list_dsh[ks]))

mod_ind_dsh = 0
user_mod_index_dsh = []
user_list_mod_dsh = []
user_mess_dsh = ''
for kk in range(len(user_list_dsh)):
    # Задаем смещение влево по алфовиту
    mod_ind_dsh = user_index_dsh[kk] - 6
    if user_index_dsh[kk] < 7:
        mod_ind_dsh = 66 - user_index_dsh[kk] + 6
    user_mod_index_dsh.append(mod_ind_dsh)
    user_list_mod_dsh.append(alf[user_mod_index_dsh[kk]])
    user_mess_dsh = user_mess_dsh + alf[user_mod_index_dsh[kk]]

print(user_mess_dsh)
