from aiogram import Bot, Dispatcher, types, executor
from inline import til
from default import info, main_menu, troll, troll_fut, otziv, products, rang, timur_fut, timur, konsta, chz, konsta_fut, s_fut, shahz_fut, shahz, subyektiv, gouz_fut, gouz, chumoli_fut,chumoli

TOKEN = "7419983048:AAG01vFF8DXm83qZXGobegy6rJVaDaM5B9o"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("""
Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️
""", reply_markup=til)

@dp.callback_query_handler(text="rus")
async def rusCallbackQuery(callbackQuery: types.CallbackQuery):
    await callbackQuery.message.answer(f"""
Ассалому алайкум, {callbackQuery.from_user.full_name}!

Спасибо, что проявили интерес к творчеству!

На данный момент для вас доступны футболки, худи, свитшоты, бейсболки и стикеры. В ближайшее время будет и другое. Кстати, при заказе любой одежды вы получите стикерпак в подарок :)

Доставка по Узбекистану занимает 2-5 рабочих дней.

Стоимость доставки по Ташкенту: - 20 000 сумов.
Стоимость доставки по Узбекистану - 30 000 сумов.

При заказе на сумму от 450 000 сумов, доставка осуществляется бесплатно!

Если вас устраивают условия, нажмите на кнопку “🔥 Продукция” для перехода к покупкам.
""", reply_markup=main_menu)

@dp.callback_query_handler(text="uzb")
async def uzb_callback(callbackQuery: types.CallbackQuery):
    await callbackQuery.message.answer("🇷🇺 Этот бот работает только на русском")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def menu(message: types.Message):
    if message.text == "🔥 Продукция":
        await message.answer("Выберите раздел 👇🏻", reply_markup=products)
    elif message.text == "📥 Корзина" or message.text == "🚖 Оформить заказ":
        await message.answer("<b>Ваша корзина пуста</b>", parse_mode='HTML')
    elif message.text == "💼 Сотрудничество":
        await message.answer("""
Мы рады сотрудничеству с вашей компанией и готовы 
изготовить футболки, худи, свитшоты и многое другое 
специально под ваши запросы.

Для связи с менеджером: @tirik_chilik""")
    elif message.text == "ℹ️ Информация":
        await message.answer("Выберите нужный вам раздел ⬇️", reply_markup=info)
    elif message.text == "🏠 Главное меню":
        await message.answer(f"""
Ассалому алайкум, {message.from_user.full_name}!

Спасибо, что проявили интерес к творчеству!

На данный момент для вас доступны футболки, худи, свитшоты, бейсболки и стикеры. В ближайшее время будет и другое. Кстати, при заказе любой одежды вы получите стикерпак в подарок :)

Доставка по Узбекистану занимает 2-5 рабочих дней.

Стоимость доставки по Ташкенту: - 20 000 сумов.
Стоимость доставки по Узбекистану - 30 000 сумов.

При заказе на сумму от 450 000 сумов, доставка осуществляется бесплатно!

Если вас устраивают условия, нажмите на кнопку “🔥 Продукция” для перехода к покупкам.
""", reply_markup=main_menu)
    elif message.text == "✍️ Оставить отзыв":
        await message.answer("""
✅ Контроль сервиса проекта Tirikchilik
Мы благодарим за сделанный выбор и будем рады, если 
Вы поможете улучшить качество нашего сервиса!
Оцените нашу работу по 5 бальной шкале.""", reply_markup=otziv)
    elif message.text == "😊Все понравилось, на 5 ❤️" or message.text == "☺️Нормально, на 4 ⭐️⭐️⭐️⭐️":
        await message.answer("Мы рады, что Вы остались довольны 😊. Будем продолжать стараться радовать Вас и Ваших близких 🤗", reply_markup=main_menu)
    elif message.text == "😐Удовлетворительно на 3 ⭐️⭐️⭐️" or message.text == "☹️Не понравилось, на 2 ⭐️⭐️" or message.text == "😤Хочу пожаловаться👎🏻":
        await message.answer("Нам жаль, что Вас не удовлетворил наш бот 😔. Помогите нам стать лучше, оставьте свои замечания и предложения 👇🏻. Будем стараться исправиться 🙏🏻.", reply_markup=main_menu)
    elif message.text == "🚀 Правила доставки":
        await message.answer("""
Условия доставки:
Доставка по Узбекистана осуществляется в течение 2-5 рабочих дней. 

Стоимость доставки по Ташкенту: - 20 000 сумов.
Стоимость доставки по Узбекистану - 30 000 сумов.

При заказе на сумму от 450 000 сумов, доставка осуществляется бесплатно!
""")
    elif message.text == "☎️ Контакты":
        await message.answer("""
Для обратной связи:
@tirik_chilik
""")
    elif message.text == "🌐 Выбрать язык":
        await message.answer("""
Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️
""", reply_markup=til)
    elif message.text == "Troll.uz":
        await message.answer("Выберите раздел 👇🏻", reply_markup=troll)
    elif message.text == "Футболки":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=troll_fut)
    elif message.text == "Don't be Sheep":
        await message.answer_photo("AgACAgIAAxkBAANaZlsHoZGnAbGzlkAVgqj4JKeChpsAAhDaMRsWv9hKQdt-S7GITsQBAAMCAAN5AAM1BA",
                                   caption="""
<b>Don't be Sheep</b>

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Troll.uz идет в подарок к футболке :)

<b>Цена: 150 000 UZS</b>""", parse_mode="HTML", reply_markup=rang)
    elif message.text == "⬅️ Назад":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=products)
    elif message.text == "Timur Alixonov":
        await message.answer("Выберите раздел 👇🏻", reply_markup=timur)
    elif message.text == "Футболки Timur Alixonov":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=timur_fut)
    elif message.text == "Такой лёгкий!":
        await message.answer_photo("AgACAgIAAxkBAAOBZlsKlnj5V8b4uAcgaLOj0JK7B_AAAibaMRsWv9hKrg0IIHNvWAEBAAMCAAN5AAM1BA", caption="""
<b>Такой лёгкий!</b>

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Тимура Алиханова идет в подарок к футболке  :)

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "#ЧЗХ":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=chz)
    elif message.text == "Лимитированные футболки!":
        await message.answer_photo("AgACAgIAAxkBAAODZlsLKmcICDSm0KJcBMyYVRxhoWQAAijaMRsWv9hKL5bNXbloyY0BAAMCAAN5AAM1BA", caption="""
<b>Лимитированные футболки!</b>

Для поддержки проекта #ЧЗХ от Оскара Джалилова! 

Состав: Хлопок 60 % Полиестер 30% Лайкра 10% 

Плотная футболка. Отлично подойдет на осень :)

К каждой футболке в подарок идут стикеры. Всего 100 футболок.

<b>Цена: 200 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "Konsta":
        await message.answer("Выберите раздел 👇🏻", reply_markup=konsta)
    elif message.text == "Футболки Konsta":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=konsta_fut)
    elif message.text == "Birgina pul bilan...":
        await message.answer_photo("AgACAgIAAxkBAAOHZlsXXX-gfU_pBwABM1-gcUUo9sikAAKl2jEbFr_YSisewB1aCBRrAQADAgADeQADNQQ", caption="""
<b>Birgina pul bilan...</b>

Перевод: "Для счастья недостаточно денег"

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Konsta идет в подарок к футболке  :)

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "Go Uz":
        await message.answer("Выберите раздел 👇🏻", reply_markup=gouz)
    elif message.text == "Футболки Go Uz":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=gouz_fut)
    elif message.text == "Ko'z Tegmasin":
        await message.answer_photo("AgACAgIAAxkBAAOJZlsYO7qJBatURNPLIxWTqIkrkSgAAqnaMRsWv9hK0BUJBZsgWlUBAAMCAAN5AAM1BA", caption="""
<b>Ko'z Tegmasin</b>

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от GoUz🔥 идет в подарок к футболке!

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "Subyektiv":
        await message.answer("Выберите раздел 👇🏻", reply_markup=subyektiv)
    elif message.text == "Футболки Subyektiv":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=s_fut)
    elif message.text == "Mantiq left Uzbekistan":
        await message.answer_photo("AgACAgIAAxkBAAOLZlsY00felBFataBUaOkHcK1ck34AAqzaMRsWv9hKnmkBWZkzJ0IBAAMCAAN5AAM1BA", caption="""
<b>Mantiq left Uzbekistan</b>

Перевод: "Логика покинула Узбекистан"

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Субъектив идет в подарок к футболке!

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "Shahzoda":
        await message.answer("Выберите раздел 👇🏻", reply_markup=shahz)
    elif message.text == "Футболки Shahzoda":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=shahz_fut)
    elif message.text == "Dratutiiii":
        await message.answer_photo("AgACAgIAAxkBAAONZlsZSuAeBvUdQk0hFgLNLLL_QFYAAq3aMRsWv9hKKX4ZiQtcihABAAMCAAN5AAM1BA", caption="""
<b>Dratutiiii</b>

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Шахзоды идет в подарок к футболке  :)

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)
    elif message.text == "Chumoli":
        await message.answer("Выберите раздел 👇🏻", reply_markup=chumoli)
    elif message.text == "Футболки Chumoli":
        await message.answer("Выберите продукцию 👇🏻", reply_markup=chumoli_fut)
    elif message.text == "Hammamiz chumolimiz":
        await message.answer_photo("AgACAgIAAxkBAAOPZlsZ-8Zw11IoRaKP5zGGzv1X_hwAArDaMRsWv9hKuhbb2WalzfwBAAMCAAN5AAM1BA", caption="""
<b>Hammamiz chumolimiz</b>

Ткань: 100% узбекская пахта (хлопок)

Стикерпак от Chumoli 🐜  идет в подарок к футболке!

<b>Цена: 150 000 UZS</b>
        """, parse_mode="HTML", reply_markup=rang)

@dp.message_handler(content_types=['photo'])
async def send_photo(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(file_id)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
