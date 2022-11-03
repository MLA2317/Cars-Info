from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import logging
menuAsosiy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🍴Katolog🍽")
        ],
        [
            KeyboardButton(text="Mening Buyurtmalarim🛎"),
            KeyboardButton(text="Savatcha🛒")
        ],
        [
            KeyboardButton(text="🎉Aksiyalar🎊"),
            KeyboardButton(text="☎Bog'lanish")
        ],
        [
            KeyboardButton(text="Lokatsiya📍", request_location=True),
            KeyboardButton(text="📍Bizning fillialarimiz")
        ]
    ],
    resize_keyboard=True
)

menuStart = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foods🥙"),
            KeyboardButton(text="Desert🧁")
        ],
        [
            KeyboardButton(text="Yetkazib berish🚗")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Asosiymenu")
        ]
    ],
    resize_keyboard=True
)
menuBar = ReplyKeyboardMarkup(
     keyboard=[
         [
             KeyboardButton(text="Hamburger🍔"),
             KeyboardButton(text="Hot-Dog🌭")
         ],
         [
             KeyboardButton(text="Sandwich🥪"),
             KeyboardButton(text="Lavash🌯")
         ],
         [
             KeyboardButton(text="PIZZA🍕")
         ],
         [
             KeyboardButton(text="Ichimliklar🥤"),
             KeyboardButton(text="Souslar🍶")
         ],
         [
             KeyboardButton(text="Fri va narsala🍟")
         ],
         [
             KeyboardButton(text="Savatcha🛒"),
             KeyboardButton(text="⬅Ortga")
         ]
     ],
    resize_keyboard=True
 )

menuHamburger = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BBQ Burger"),
            KeyboardButton(text="BBQ Cheeseburger")
        ],
        [
            KeyboardButton(text="Cheeseburger"),
            KeyboardButton(text="Chicken Cheese Burger")
        ],
        [
            KeyboardButton(text="Chicken Zinger"),
            KeyboardButton(text="Double Burger")
        ],
        [
            KeyboardButton(text="Double Cheeseburger"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Chicken Zinger Cheese")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuHotdog = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hot Dog"),
            KeyboardButton(text="King Dog")
        ],
        [
            KeyboardButton(text="Long Upper")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuSandwich = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Clab Sandwich")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuLavash = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cheese Lavash"),
            KeyboardButton(text="Cheese Little Lavash")
        ],
        [
            KeyboardButton(text="Chicken Lavash"),
            KeyboardButton(text="Lavash")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuPizza = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pizza Kombo"),
            KeyboardButton(text="Pizza Chicken Cheese")
        ],
        [
            KeyboardButton(text="Pizza Meat"),
            KeyboardButton(text="Pizza Alfedro")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuIchimlik = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Coca-cola 0.5"),
            KeyboardButton(text="Fanta 0.5")
        ],
        [
            KeyboardButton(text="Sprite 0.5"),
            KeyboardButton(text="Gazli suv 0.5")
        ],
        [
            KeyboardButton(text="Moxito"),
            KeyboardButton(text="Ice tea choy")
        ],
        [
            KeyboardButton(text="Limonli kok choy"),
            KeyboardButton(text="Limonli qora choy")
        ],
        [
            KeyboardButton(text="Kok choy"),
            KeyboardButton(text="Qora choy")
        ],
        [
            KeyboardButton(text="Qora coffe"),
            KeyboardButton(text="3v1 coffe")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuSouslar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ketchup"),
            KeyboardButton(text="Mayonez")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)

menuFri = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kartoshka fri"),
            KeyboardButton(text="Qishloqcha kartoshka")
        ],
        [
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Orqaga")
        ]
    ],
    resize_keyboard=True
)
menuDesert = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Sinomon rollar 8 ta"),
            KeyboardButton(text="Sinomon rollar 16 ta")
        ],
        [
            KeyboardButton(text="Shokoladli Fondan")
        ],
[
            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Ortga")
        ]
    ],
    resize_keyboard=True
)

menuAksiya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="3 ta pizza 99000 ga"),
            KeyboardButton(text="Donar Kombo")
        ],
        [

            KeyboardButton(text="Savatcha🛒"),
            KeyboardButton(text="⬅Asosiymenu")
        ]
    ],
    resize_keyboard=True
)

fillialBiz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Gulzor"),
            KeyboardButton(text="Maksim Gorkiy")
        ],
        [
            KeyboardButton(text="⬅Asosiymenu")
        ]
    ],
    resize_keyboard=True
)