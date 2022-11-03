from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram import executor
from aiogram.dispatcher.filters import Command
from config import dp, bot
from Replykeyboard import menuAsosiy, menuStart, menuBar, menuHamburger, menuHotdog,  menuSandwich, menuLavash, menuPizza, menuIchimlik,menuSouslar, menuFri, menuDesert, menuAksiya, fillialBiz
#from geopy.geocoders import Nominatim

import logging

@dp.message_handler(Command('start'))
async def start(msg: Message):
    img = open("image/photo_2022-10-29_15-13-01.jpg", "rb")
    text = f"Assalomu Aleykum {msg.from_user.full_name}, Fast food ga Hush Kelibsiz!"
    await msg.answer_photo(img, caption=text, reply_markup=menuAsosiy)


@dp.message_handler(commands='help')
async def help(msg: Message):
    await msg.answer(f"For Help apply @lazizbek_a", reply_markup=menuAsosiy)



#menubosh
@dp.message_handler(text="🍴Katolog🍽")
async def katolog(msg: Message):
    print(logging.info(msg.from_user.id))
    print(logging.info(msg.from_user.full_name))
    print(logging.info(msg.from_user.get_profile_photos))
    print(msg.from_user.values)
    await msg.answer(f"Menu:", reply_markup=menuStart)




#boglanish
@dp.message_handler(text="☎Bog'lanish")
async def boglanish(msg: Message):
    txt = f"Bizga bog'lanish uchun shunga murajat qiling: @lazizbek_a" \
          f"\n" \
          f"\n<------------------>" \
          f"\n<------------------>" \
          f"\n" \
          f"\nTel: 99-085-23-17" \
          f"\nhttps://www.instagram.com/lazizbek__a/"
    await msg.answer(txt, reply_markup=menuAsosiy)




#Aksiya
@dp.message_handler(text="🎉Aksiyalar🎊")
async def aksiya(msg: Message):
    txt = f"Mahsulotni Tanlang!"
    await msg.answer(txt, reply_markup=menuAksiya)

# 3 ta pizza
@dp.message_handler(text="3 ta pizza 99000 ga")
async def ppz(msg: Message):
    img = open("photo/photo_2022-11-03_10-33-46.jpg", "rb")
    await msg.answer_photo(img, f"3 pitsa 99000ga\n "
                                f"\n "
                                f"\n"
                                f"35% chegirma bilan  3 ta 25 santimetrli pitsa — bu Fast food pitsasi’ning "
                                f"hatto 6 kishiga yetadigan yangi kombosi! Do‘stlarni to‘plash uchun\n"
                                f"zo'r sabab. \n"
                                f"\n"
                                f"Narxi: 99000 som", reply_markup=menuAksiya)

@dp.message_handler(text="3 ta pizza 99000 ga")
async def ppz(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuAksiya)

#back
@dp.message_handler(text="⬅Asosiymenu")
async def asosiy(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuAsosiy)


#Donar kombor
@dp.message_handler(text="Donar Kombo")
async def dnp(msg: Message):
    img = open("photo/photo_2022-11-03_11-10-04.jpg", "rb")
    await msg.answer_photo(img, f"Donar kombo"
                                f"\n"
                                f"\n"
                                f"\nHaqiqiy donar go‘shti va mazali motsarella pishlog‘i solingan Donar Pitsa, "
                                f"\n1 litrlik Coca-cola hamda 8 ta pepperoni rolllari — 2-3 "
                                f"\nkishi bemalol to‘ydiradigan kombo"
                                f"\n"
                                f"\n"
                                f"\nNarxi: 84000 som", reply_markup=menuAksiya)

@dp.message_handler(text="Donar Kombo")
async def dnp(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuAksiya)

#back
@dp.message_handler(text="⬅Asosiymenu")
async def asosiy(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuAsosiy)



#fillial
@dp.message_handler(text="📍Bizning fillialarimiz")
async def fillial(msg: Message):
    txt = f"Filialni Tanlang!"
    await msg.answer(txt, reply_markup=fillialBiz)

#gulzor fillial
@dp.message_handler(text="Gulzor")
async def gulzor(msg: Message):
    await msg.answer_location(f"Gulzor \n📍General Uzoqov 60-A dom \n⏰10:00a.m- 00:00a.m",
                             longitude=69.194513)


#@dp.message_handler(text="Gulzor")
#async def gulzor(msg: Message):
   # await msg.answer(f"S")

#menu start
@dp.message_handler(text="Foods🥙")
async def food(msg: Message):
    await msg.answer(f"Menu:", reply_markup=menuBar)



#Menu Hamburger
@dp.message_handler(text="Hamburger🍔")
async def hamburger(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuHamburger)



#BBq burger info
@dp.message_handler(text="BBQ Burger")
async def bbqburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-19.jpg", "rb")
    await msg.answer_photo(img, f"BBQ Burger"
                                f"\n---------------"
                                f"\nNarxi 26000som ", reply_markup=menuHamburger)

@dp.message_handler(text="BBQ Burger")
async def bbqburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#bbq cheeseburger info
@dp.message_handler(text='BBQ Cheeseburger')
async def bbqchburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-29.jpg", "rb")
    await msg.answer_photo(img, f"BBQ Cheese Burger"
                                f"\n---------------"
                                f"\n---------------"
                                f"\nNarxi 29000som ", reply_markup=menuHamburger)

@dp.message_handler(text="BBQ Cheeseburger")
async def bbqchburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)





#Cheeseburger info
@dp.message_handler(text='Cheeseburger')
async def chburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-29.jpg", "rb")
    await msg.answer_photo(img, f"Cheese Burger"
                                f"\n---------------"
                                f"\nNarxi 28000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Cheeseburger")
async def chburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Chicken cheeseburger info
@dp.message_handler(text='Chicken Cheese Burger')
async def chchburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-35.jpg", "rb")
    await msg.answer_photo(img, f"Chicken Cheese Burger"
                                f"\n---------------"
                                f"\nNarxi 24000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Chicken Cheese Burger")
async def chchburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Chicken zinger info
@dp.message_handler(text='Chicken Zinger')
async def chzburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-39.jpg", "rb")
    await msg.answer_photo(img, f"Chicken Zinger"
                                f"\n---------------"
                                f"\nNarxi 22000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Chicken Zinger")
async def chzburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Double burger info
@dp.message_handler(text='Double Burger')
async def dburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-45.jpg", "rb")
    await msg.answer_photo(img, f"Double Burger"
                                f"\n---------------"
                                f"\nNarxi 33000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Double Burger")
async def dburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Double cheeseburger info
@dp.message_handler(text='Double Cheeseburger')
async def dchburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-51.jpg", "rb")
    await msg.answer_photo(img, f"Double Cheeseburger"
                                f"\n---------------"
                                f"\nNarxi 36000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Double Cheeseburger")
async def dchburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Gamburger info
@dp.message_handler(text='Gamburger')
async def gburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-07-58.jpg", "rb")
    await msg.answer_photo(img, f"Gamburger"
                                f"\n---------------"
                                f"\nNarxi 25000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Gamburger")
async def gburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)




#Chicken zingercheese info
@dp.message_handler(text='Chicken Zinger Cheese')
async def chzburger(msg: Message):
    img = open("photo/photo_2022-10-30_19-08-04.jpg", "rb")
    await msg.answer_photo(img, f"Chicken Zinger Cheese"
                                f"\n---------------"
                                f"\nNarxi 25000som ", reply_markup=menuHamburger)

@dp.message_handler(text="Chicken Zinger Cheese")
async def chzburger(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHamburger)


#back
@dp.message_handler(text="⬅Orqaga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#Hot dog menu
@dp.message_handler(text="Hot-Dog🌭")
async def hotdog(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuHotdog)

#Hot dog info
@dp.message_handler(text='Hot Dog')
async def hotdogg(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-31.jpg", "rb")
    await msg.answer_photo(img, f"Hot Dog\n---------------\nNarxi 15000som ", reply_markup=menuHotdog)

@dp.message_handler(text="Hot Dog")
async def hotdogg(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHotdog)


#King dog info
@dp.message_handler(text='King Dog')
async def kingdogg(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-31.jpg", "rb")
    await msg.answer_photo(img, f"Hot Dog\n---------------\nNarxi 20000som ", reply_markup=menuHotdog)

@dp.message_handler(text="King Dog")
async def kingdogg(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHotdog)


#Long upper info
@dp.message_handler(text='Long Upper')
async def longup(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-36.jpg", "rb")
    await msg.answer_photo(img, f"Long Upper\n---------------\nNarxi 32000som ", reply_markup=menuHotdog)

@dp.message_handler(text="Long Upper")
async def longup(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuHotdog)

#back
@dp.message_handler(text="⬅Orqaga")
async def orqaga(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#Sandwich menu
@dp.message_handler(text="Sandwich🥪")
async def sandwich(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuSandwich)

#Clab Sandwich info
@dp.message_handler(text='Clab Sandwich')
async def sandwich(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-06.jpg", "rb")
    await msg.answer_photo(img, f"Long Upper\n---------------\nNarxi 26000som ", reply_markup=menuSandwich)

@dp.message_handler(text="Clab Sandwich")
async def sandwich(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuSandwich)

#back
@dp.message_handler(text="⬅Orqaga")
async def orqaga(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#Lavash menu
@dp.message_handler(text="Lavash🌯")
async def lavash(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuLavash)

#Cheese lavash
@dp.message_handler(text="Cheese Lavash")
async def chelavash(msg: Message):
    img = open("photo/photo_2022-10-30_19-08-17.jpg", "rb")
    await msg.answer_photo(img, f"Cheese Lavash\n---------------\nNarxi 29000som ", reply_markup=menuLavash)

@dp.message_handler(text="Cheese Lavash")
async def chelavash(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuLavash)


#Cheese little lavash
@dp.message_handler(text="Cheese Little Lavash")
async def chellavash(msg: Message):
    img = open("photo/photo_2022-10-30_19-08-17.jpg", "rb")
    await msg.answer_photo(img, f"Cheese Little Lavash\n---------------\nNarxi 20000som ", reply_markup=menuLavash)

@dp.message_handler(text="Cheese Little Lavash")
async def chellavash(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuLavash)


#chicken lavash
@dp.message_handler(text="Chicken Lavash")
async def chlavash(msg: Message):
    img = open("photo/photo_2022-10-30_19-08-42.jpg", "rb")
    await msg.answer_photo(img, f"Chicken Lavash\n---------------\nNarxi 25000som ", reply_markup=menuLavash)

@dp.message_handler(text="ChickenLavash")
async def chlavash(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuLavash)


#Lavash
@dp.message_handler(text="Lavash")
async def lavash(msg: Message):
    img = open("photo/photo_2022-10-30_19-08-17.jpg", "rb")
    await msg.answer_photo(img, f"Lavash\n---------------\nNarxi 26000som ", reply_markup=menuLavash)

@dp.message_handler(text="Lavash")
async def lavash(msg: Message):
    await msg.answer(f"Tanlaganongizdan Hursandmiz!", reply_markup=menuLavash)

#back
@dp.message_handler(text="⬅Orgaga")
async def orqaga(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#Pizza menu
@dp.message_handler(text="PIZZA🍕")
async def pizza(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuPizza)


#pizza combo
@dp.message_handler(text="Pizza Kombo")
async def pzcomboo(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-18.jpg", "rb")
    await msg.answer_photo(img, f"Pizza combo\n---------------\nNarxi 45000som", reply_markup=menuPizza)

@dp.message_handler(text="Pizza Kombo")
async def pzcomboo(msg: Message):
    await msg.answer(f"Tanlanganingizdan Hursandmiz!", reply_markup=menuPizza)



#pizza cheese
@dp.message_handler(text="Pizza Chicken Cheese")
async def pzches(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-22.jpg", "rb")
    await msg.answer_photo(img, f"Pizza Chicken Cheese\n---------------\nNarxi 47000som", reply_markup=menuPizza)

@dp.message_handler(text="Pizza Chicken Cheese")
async def pzches(msg: Message):
    await msg.answer(f"Tanlanganingizdan Hursandmiz!", reply_markup=menuPizza)



#pizza meat
@dp.message_handler(text="Pizza Meat")
async def pzmt(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-28.jpg", "rb")
    await msg.answer_photo(img, f"Pizza Meat \n---------------\nNarxi 55000som", reply_markup=menuPizza)

@dp.message_handler(text="Pizza Meat")
async def pzmt(msg: Message):
    await msg.answer(f"Tanlanganingizdan Hursandmiz!", reply_markup=menuPizza)



#pizza Alfedro
@dp.message_handler(text="Pizza Alfedro")
async def pzalfed(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-32.jpg", "rb")
    await msg.answer_photo(img, f"Pizza Alfedro \n---------------\nNarxi 50000som", reply_markup=menuPizza)

@dp.message_handler(text="Pizza Alfedro")
async def pzalfed(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuPizza)

#back
@dp.message_handler(text="⬅Orqaga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#Ichimliklar
@dp.message_handler(text="Ichimliklar🥤")
async def ichimlik(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuIchimlik)

#cola info
@dp.message_handler(text="Coca-cola 0.5")
async def cola(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-13.jpg", "rb")
    await msg.answer_photo(img, f"Coca-cola 0.5 \n---------------\nNarxi 7000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Coca-cola 0.5")
async def cola(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)




#Fanat info
@dp.message_handler(text="Fanta 0.5")
async def fanta(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-13.jpg", "rb")
    await msg.answer_photo(img, f"Fanta 0.5 \n---------------\nNarxi 7000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Fanta 0.5")
async def fanta(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#Sprite
@dp.message_handler(text="Sprite 0.5")
async def sprite(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-13.jpg", "rb")
    await msg.answer_photo(img, f"Sprite 0.5 \n---------------\nNarxi 7000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Sprite 0.5")
async def sprite(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#gazli suv
@dp.message_handler(text="Gazli suv 0.5")
async def gazli(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-13.jpg", "rb")
    await msg.answer_photo(img, f"Gazli suv 0.5 \n---------------\nNarxi 3000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Gazli suv")
async def gazli(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#Moxito
@dp.message_handler(text="Moxito")
async def moxito(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-41.jpg", "rb")
    await msg.answer_photo(img, f"Moxito \n---------------\nNarxi 15000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Moxito")
async def moxito(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#Ice tea choy
@dp.message_handler(text="Ice tea choy")
async def icetea(msg: Message):
    img = open("photo/photo_2022-10-30_19-06-04.jpg", "rb")
    await msg.answer_photo(img, f"Moxito \n---------------\nNarxi 21000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Ice tea choy")
async def icetea(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#limon kok choy
@dp.message_handler(text="Limonli kok choy")
async def limonkok(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"Limonli kok choy \n---------------\nNarxi 4000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Limonli kok choy")
async def limonkok(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#limon qora choy
@dp.message_handler(text="Limonli qora choy")
async def limonqora(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"Limonli qora choy \n---------------\nNarxi 4000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Limonli qora choy")
async def limonqora(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#kok choy
@dp.message_handler(text="Kok choy")
async def kokchoy(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"Kok choy \n---------------\nNarxi 3000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Kok choy")
async def kokchoy(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#qora choy
@dp.message_handler(text="Qora choy")
async def qorachoy(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"Qora choy \n---------------\nNarxi 3000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Qora choy")
async def qorachoy(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#qora coffe
@dp.message_handler(text="Qora coffe")
async def qoracoffe(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"Qora coffe \n---------------\nNarxi 6000som", reply_markup=menuIchimlik)

@dp.message_handler(text="Qora coffe")
async def qoracoffe(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)



#3v1 coffe
@dp.message_handler(text="3v1 coffe")
async def coffe(msg: Message):
    img = open("photo/photo_2020-02-29_12-54-37.jpg", "rb")
    await msg.answer_photo(img, f"3v1 coffe \n---------------\nNarxi 6000som", reply_markup=menuIchimlik)

@dp.message_handler(text="3v1 coffe")
async def coffe(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuIchimlik)

#back
@dp.message_handler(text="⬅Orqaga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#souslar
@dp.message_handler(text="Souslar🍶")
async def sous(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuSouslar)

#ketchup
@dp.message_handler(text="Ketchup")
async def ketchup(msg: Message):
    img = open("photo/photo_2021-06-01_00-26-12.jpg", "rb")
    await msg.answer_photo(img, f"Ketchup \n---------------\nNarxi 1000som", reply_markup=menuSouslar)

@dp.message_handler(text="Ketchup")
async def ketchup(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuSouslar)



#mayoney
@dp.message_handler(text="Mayonez")
async def mayonez(msg: Message):
    img = open("photo/photo_2021-06-09_21-00-10.jpg", "rb")
    await msg.answer_photo(img, f"Mayonez \n---------------\nNarxi 1000som", reply_markup=menuSouslar)

@dp.message_handler(text="Mayonez")
async def mayonez(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuSouslar)

#back
@dp.message_handler(text="⬅Orqaga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuBar)



#fri menu
@dp.message_handler(text="Fri va narsala🍟")
async def fri(msg: Message):
    await msg.answer(f"Quyidagilarni Tanlang!", reply_markup=menuFri)

#kartoshka fri
@dp.message_handler(text="Kartoshka fri")
async def kartoshka(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-12.jpg", "rb")
    await msg.answer_photo(img, f"Kartoshka fri \n---------------\nNarxi 11000som", reply_markup=menuFri)

@dp.message_handler(text="Kartoshka fri")
async def kartoshka(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuFri)



#Qishloqcha kartoshka
@dp.message_handler(text="Qishloqcha kartoshka")
async def qishloqcha(msg: Message):
    img = open("photo/photo_2022-10-30_19-09-21.jpg", "rb")
    await msg.answer_photo(img, f"Qishloqcha kartoshka \n---------------\nNarxi 11000som", reply_markup=menuFri)

@dp.message_handler(text="Qishloqcha kartoshka")
async def qishloqcha(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuFri)

#back
@dp.message_handler(text="⬅Ortga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuStart)


#back
@dp.message_handler(text="⬅Asosiymenu")
async def orqaga(msg: Message):
    await msg.answer(f"Buyurtma bering!", reply_markup=menuAsosiy)




#desert
@dp.message_handler(text="Desert🧁")
async def desert(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuDesert)

#sinamon roll 8
@dp.message_handler(text="Sinomon rollar 8 ta")
async def sinamon(msg: Message):
    img = open("photo/photo_2022-11-01_15-36-56.jpg", "rb")
    await msg.answer_photo(img, f"Sinamon Rollar 8ta \n---------------\nNarxi 10000som", reply_markup=menuDesert)

@dp.message_handler(text="Sinomon rollar 8 ta")
async def sinamon(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuDesert)



#sinamon roll 16
@dp.message_handler(text="Sinomon rollar 16 ta")
async def sinamonr(msg: Message):
    img = open("photo/photo_2022-11-01_15-36-56.jpg", "rb")
    await msg.answer_photo(img, f"Sinamon Rollar 16ta \n---------------\nNarxi 20000som", reply_markup=menuDesert)

@dp.message_handler(text="Sinomon rollar 16 ta")
async def sinamonr(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuDesert)



#shokoladli fonfon
@dp.message_handler(text="Shokoladli Fondan")
async def shokolad(msg: Message):
    img = open("photo/photo_2021-12-14_16-25-43.jpg", "rb")
    await msg.answer_photo(img, f"Shokoladli fondan \n---------------\nNarxi 19000som", reply_markup=menuDesert)

@dp.message_handler(text="Shokoladli Fondan")
async def shokolad(msg: Message):
    await msg.answer(f"Tanlaganganingizdan Hursandmiz!", reply_markup=menuDesert)

#back
@dp.message_handler(text="⬅Ortga")
async def back(msg: Message):
    await msg.answer(f"Quyidigilarni Tanlang!", reply_markup=menuStart)




if __name__ == "__main__":
    executor.start_polling(dp)
