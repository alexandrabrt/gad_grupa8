# my_var = 5
#
# if my_var == 6:
#     print("Set instructiuni")
# elif my_var == 5:
#     print('Egalitate')
# else:
#     print("Orice alt caz")


# my_var = 5
# msg = 'Orice alt caz'
# if my_var == 6:
#     msg = "Set instructiuni"
#     var = "Ana are mere"
# elif my_var == 5:
#     msg = 'Egalitate'
# print(msg)

# salariu = 2
# nivel_salariu = "Salariul este mic"
# if salariu > 4:
#     nivel_salariu = "Salariul este ok"
# nivel_salariu = "Salariu este ok" if salariu > 4 else "Salariul este mic"
# print(nivel_salariu)

# salariu = 99
# nivel_salariu = "Salariul este ok"
# if salariu > 100 and (salariu_net := salariu - 30) and salariu_net > 70:
#     nivel_salariu = "Salariu ok"
# elif salariu <= 100 and (salariu_net := salariu - 20) and salariu_net < 60:
#     nivel_salariu = "Salariu mic"

salariu = 100
nivel_salariu = "Salariul este ok"
if salariu > 100 and (salariu_net := salariu - 30) and salariu_net > 70:
    nivel_salariu = "Salariu ok"
elif salariu <= 100:
    nivel_salariu = "Salariu mic"

print(salariu_net)

