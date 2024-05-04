# # # # # # # # # a = input('Uzb paytaxti ? ')

# # # # # # # # # if a.lower() !='tashkent':
# # # # # # # # #     print('juwap qate!')
# # # # # # # # # if a.lower() == 'tashkent':
# # # # # # # # #     print('juwap duris!')

# # # # # # # # avtolar = ['audi','gm','bmw','kia']
# # # # # # # # for avto in avtolar:
# # # # # # # #     if avto == 'bmw':
# # # # # # # #         print(avto.upper())
# # # # # # # #     elif avto == 'kia':
# # # # # # # #         print(avto.upper())
# # # # # # # #     else:
# # # # # # # #         print(avto.title())


# # # # # # # jas = int(input('jasiniz  neshede ?' ))

# # # # # # # if jas <= 14:
# # # # # # #     print('Sizge bilet biypul!!!')
# # # # # # # elif jas >= 50:
# # # # # # #     print('Szige bilet bahasi 3000')
# # # # # # # elif jas > 14:
# # # # # # #     print('sizge bilet bahasi 5000')

# # # # # # login = input('login ?')

# # # # # # if len(login) <= 8:
# # # # # #     print('login 8 den kem bolmawi kk !')


# # # # # # ! yaki

# # # # # kun = input('Bugin qaysi kun ? ')
# # # # # gradus = float(input('hawa rayi qanday ? '))


# # # # # if kun.lower() == 'yekshenbi' and  gradus >= 30 :
# # # # #     print('Bugin aylanatin kun eken ! ')
# # # # # elif kun.lower() == 'yekshenbi' and gradus <30:
# # # # #     print('uyde tinish otiratin kun eken')


# # # # baha = 15000
# # # # chay = True
# # # # salat = False

# # # # if chay and salat:
# # # #     baha = baha + 10000
# # # # elif chay or salat:
# # # #     baha = baha + 5000

# # # # print(f'uliwma {baha} swm')


# # # baha = 15000 # usi waqitqa deyin aldi
# # # chay = True
# # # salat = True
# # # nan = True
# # # kampot = True
# # # assorti = True

# # # if chay:
# # #     print('chay aldi ')
# # #     baha = baha + 3000
# # # if salat:
# # #     print('Salat aldi')
# # #     baha = baha + 5000
# # # if nan :
# # #     print('nan aldi')
# # #     baha = baha + 2000
# # # if kampot:
# # #     print('kampot aldi')
# # #     baha = baha + 1000
# # # if assorti:
# # #     print('assorti aldi')
# # #     baha = baha + 150000

# # # print(f'uliwma {baha} swm')


# # # # ! in op

# # # menu = ['chay', 'nan', 'kompot','somsa']
# # # a = 'chay' in menu

# # # print(a)


# # # menu = ['palaw', 'manti',' gamburger']
# # # awqat = input('ne jeysiz?')

# # # if awqat.lower() in menu:
# # #     print('Zakaz aldim ')
# # # else:
# # #     print('bizlerde bunday awqat joq')


# # menu = ["palaw", "manti", " gamburger"]
# # awqat = input('ne jiysiz ?')

# # if awqat.lower() not in menu:
# #     print('bunday awqat joq !')
# # else:
# #     print('Zakaz aldim')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# menu = ['palaw','somsa', 'shashlik']
# zakazlar = ['palaw', 'manti','somsa']

# for awqat in zakazlar:
#     if awqat in menu:
#         print(f'Menuda {awqat} bar')
#     else:
#         print(f'Menuda {awqat} joq')





