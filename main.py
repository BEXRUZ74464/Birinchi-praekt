import asyncio
from aiogram import Dispatcher, Bot, filters, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import openai

SECRET_KEY = "sk-proj-ial1WuAymUn2Rwn09BLsT3BlbkFJGyktK0UlQqn0o0kOgSom"
openai.api_key = SECRET_KEY

bot = Bot(token="7394400587:AAFvQdi8T0do94I-pUhXtplbfxi1j4nSKkA")
dp = Dispatcher(bot=bot)


class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()

class Registration_1(StatesGroup):
    first_name_1 = State()
    last_name_1 = State()
    number_1 = State()

class Card(StatesGroup):
    card_number = State()
    card_number_2 = State()


class Card_1(StatesGroup):
    card_number = State()
    card_number_2 = State()


def answer_process(question):
    response = openai.Completion.create(
        model='gpt-3.5-turbo-instruct',
        prompt=f"Hey bro, i have question to and the question is {question}."
               f"After answering please just answer in Uzbek language",
        max_tokens=1000,
    )
    if response['choices'][0]['text']:
        answer = response['choices'][0]['text']
        answer.replace("_", "\\_")
        answer.replace("*", "\\*")
        answer.replace("[", "\\[")
        answer.replace("`", "\\`")
        answer.replace("=", "\\=")
        return answer
    else:
        return "Nima deb yozding?"


contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
], resize_keyboard=True)

til = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Uzb 🇺🇿")],
    [KeyboardButton(text="Rus 🇷🇺")]
], resize_keyboard=True)

til_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="O'zbek tili 🇺🇿")],
    [KeyboardButton(text="Русский язык 🇷🇺")]
], resize_keyboard=True)

kb_1 = [
    [KeyboardButton(text="💻 Kurslar bo'limi"), KeyboardButton(text="🛒 Savat"), KeyboardButton(text="📑 Ma'lumot")],
    [KeyboardButton(text="🤝 Yordam"), KeyboardButton(text="🔄 Tilni o'zgartirish")]
]
mb_1 = ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True)

kurslar_toplami = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💻 Front end"),
     KeyboardButton(text="💻 Back end")],
    [KeyboardButton(text="💻 Design"),
     KeyboardButton(text="🔙 Orqaga")]
], resize_keyboard=True)

front_toplami = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 HTML", callback_data="html"),
     InlineKeyboardButton(text="👨🏻‍💻 CSS and Sass", callback_data="css")],
    [InlineKeyboardButton(text="👨🏻‍💻 Java Script", callback_data="js"),
     InlineKeyboardButton(text="👨🏻‍💻 React", callback_data="react")]
])
#
back_toplami = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 Python", callback_data="py"),
     InlineKeyboardButton(text="👨🏻‍💻 C#", callback_data="c")],
    [InlineKeyboardButton(text="👨🏻‍💻 Java", callback_data="java"),
     InlineKeyboardButton(text="👨🏻‍💻 Node.js", callback_data="node")]
])
#
design_toplami = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 Grafik design", callback_data="g_ds"),
     InlineKeyboardButton(text="👨🏻‍💻 Design", callback_data="ds")]
])

muddat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🌘 3 oy", callback_data="3"), InlineKeyboardButton(text="🌗 6 oy", callback_data="6")],
    [InlineKeyboardButton(text="🌑 12 oy", callback_data="12"), InlineKeyboardButton(text="🌓 18 oy", callback_data="18")]
])

malumot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="To'liq ma'lumotni bilish 🌐", url="https://uz.wikipedia.org/wiki/Telegram")],
    [InlineKeyboardButton(text="Video ko'rish 🌐", url="https://youtu.be/lcRhiINSic0?si=qfyomtTDAakZPAgr")]
])


pay_3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_3")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_6")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_12")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

pay_18 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ O'qishni boshlash", callback_data="oqish_18")],
    [InlineKeyboardButton(text="❌ O'qishni tugatish", callback_data="orqaga")]
])

savat_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💸 Sotib olish"), KeyboardButton(text="🚮 Savatni tozalash")],
    [KeyboardButton(text="🗑 Savatni ko'rish"), KeyboardButton(text="🔙 Orqaga")]
], resize_keyboard=True)

cart = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💳 Uzcard", callback_data="Uzcard")],
    [InlineKeyboardButton(text="💳 Humo", callback_data="Humo")],
])

orders = []


@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(
        f"Salom {message.from_user.full_name}, botga xush kelibsiz !!! \nПривет {message.from_user.full_name}, добро пожаловать в бот!!!",
        reply_markup=til)


@dp.message(F.text == "Uzb 🇺🇿")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting: ")


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Yaxshi endi familya kiriting: ", reply_markup=ReplyKeyboardRemove())


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Yaxshi endi raqamingizni kiriting: ", reply_markup=contact_button)


@dp.message(Registration.number)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Gap yo'q!\nSizning ismingiz: {data['first_name']}\nSizning familyangiz: {data['last_name']}\nSizning nomeringiz: {data['number']}",
        reply_markup=mb_1)
    await state.clear()


@dp.message(F.text == "💻 Kurslar bo'limi")
async def kurs_function(message: types.Message):
    await message.answer_photo(photo="https://miro.medium.com/v2/resize:fit:1192/1*jXusXvCfxECPU_Jh9S_E3w.jpeg",
                               caption="Siz kurslar bo'limini tanladingiz \nBu bo'lim orqali o'zingizga yoqqan kursni tanlay olasiz. \n1. Front end \n2. Back end \n3. Design",
                               reply_markup=kurslar_toplami)


@dp.message(F.text == "🔙 Orqaga")
async def ortga_function(message: types.Message):
    await message.answer("Siz ortga qaytdiz", reply_markup=mb_1)


@dp.callback_query(F.data == "orqaga")
async def ortga_function(call: types.CallbackQuery):
    await call.message.answer("Siz ortga qaytdiz", reply_markup=kurslar_toplami)


@dp.message(F.text == "💻 Front end")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/05/31/71/02/360_F_531710260_ByieqNe7Ut6QBHgIR7xgdsxH7gICrHr1.jpg",
        caption="Siz Front end bo'limiga o'tdingiz. \nBu yurdan o'zizga yoqqan kursni tanlang.",
        reply_markup=front_toplami)


@dp.callback_query(F.data == "html")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz HTML ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "css")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz CSS va Sass yo'nalishlarini tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?",
        reply_markup=muddat)


@dp.callback_query(F.data == "js")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Java Script ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "react")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz React ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.message(F.text == "💻 Back end")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.ipraxa.com/blog/wp-content/uploads/2021/10/frontend-vs-backend.png",
        caption="Siz Back end bo'limiga o'tdingiz. \nBu yurdan o'zizga yoqqan kursni tanlang.",
        reply_markup=back_toplami)


@dp.callback_query(F.data == "py")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Python ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "c")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz C# ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "java")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Java ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "node")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Node.js ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.message(F.text == "💻 Design")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://cdn.sanity.io/images/tlr8oxjg/production/cbce8b3ffe9e0b82f5d710b56ed210546228c415-1232x690.png?w=3840&q=100&fit=clip&auto=format",
        caption="Siz Design bo'limiga o'tdingiz. \nBu yurdan o'zizga yoqqan kursni tanlang.",
        reply_markup=back_toplami)


@dp.callback_query(F.data == "g_ds")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Grafik Design ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?",
        reply_markup=muddat)


@dp.callback_query(F.data == "ds")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Siz Design ni tanladingiz. \nBu yo'nalish bo'yicha necha oy o'qimoqchisiz ?", reply_markup=muddat)


@dp.callback_query(F.data == "3")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Siz 3 oyli o'qish turini tanladingiz.", reply_markup=pay_3)


@dp.callback_query(F.data == "oqish_3")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 3 oyli o'qish")
    await call.message.answer(
        "Siz 3 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=kurslar_toplami)


@dp.callback_query(F.data == "6")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Siz 6 oyli o'qish turini tanladingiz.", reply_markup=pay_6)


@dp.callback_query(F.data == "oqish_6")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 6 oyli o'qish")
    await call.message.answer(
        "Siz 6 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=kurslar_toplami)


@dp.callback_query(F.data == "12")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Siz 12 oyli o'qish turini tanladingiz.", reply_markup=pay_12)


@dp.callback_query(F.data == "oqish_12")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 12 oyli o'qish")
    await call.message.answer(
        "Siz 12 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=kurslar_toplami)


@dp.callback_query(F.data == "18")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Siz 18 oyli o'qish turini tanladingiz.", reply_markup=pay_18)


@dp.callback_query(F.data == "oqish_18")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 18 oyli o'qish")
    await call.message.answer(
        "Siz 18 oyli o'qishni tanladingiz. \nTo'lovni savat bo'limidan amalga oshirishingiz mumkin",
        reply_markup=kurslar_toplami)


@dp.message(F.text == "📑 Ma'lumot")
async def malumot_function(message: types.Message):
    await message.answer_photo(photo="https://texnokun.uz/wp-content/uploads/2023/02/temy-v-gruppax-telegram.jpeg",
                               caption="Telegram – tezkor xabar almashish vositasi. Oddiy foydalanuvchilar matn xabarlashuvdan tashqari bir-birlariga har birining hajmi 2 GB gacha boʻlgan tasvir, video, audio va har xil fayllar yuborishlari hamda ovozli va video qoʻngʻiroqlarni amalga oshirishlari, kanal va guruhlarda ovozli hamda video chatlarda qatnashishlari mumkin. \n\nDastur Google, Android, Apple iOS, Microsoft Windows, Blackberry, MacOS, Linux va Windows Phone uchun mavjud.",
                               reply_markup=malumot)


@dp.message(filters.Command("🤝 Yordam"))
async def start_function(message: types.Message):
    await message.answer("Xush kelibsiz, men ChatGPT botman. Qanaqa savoling bor?")


# @dp.message(F.text)
# async def text_function(message: types.Message):
#     result = await answer_process(question=message.text)
#
#     await message.answer(text=result)


@dp.message(F.text == "🔄 Tilni o'zgartirish")
async def balance_function(message: types.Message):
    await message.answer(f"Siz tilni oʻzgartirishni tanladingiz \nTilni oʻzgartiring", reply_markup=til_1)


@dp.message(F.text == "O'zbek tili 🇺🇿")
async def balance_function(message: types.Message):
    await message.answer(f"Siz O'zbek tilga o'zgartirdingiz", reply_markup=mb_1)


@dp.message(F.text == "💸 Sotib olish")
async def savat_function(message: types.Message):
    await message.answer("To'lov turini tanlang Uzcard yoki Humo orqali to'lash", reply_markup=cart)


@dp.message(F.text == "🛒 Savat")
async def savat_function(message: types.Message):
    await message.answer("Siz savat bo'limini tanladingiz !", reply_markup=savat_button)


@dp.message(F.text == "🗑 Savatni ko'rish")
async def orders_function(message: types.Message):
    await message.answer(f"Sizda bor kurslar ro'yxati !!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb_1)


@dp.message(F.text == "🚮 Savatni tozalash")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Siz barcha kurslarni o'chirib yubordingiz !!!", reply_markup=mb_1)


@dp.callback_query(F.data == "Uzcard")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz to'lovni Uzcard kartasi orqali omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!", reply_markup=cart)
    await state.clear()


@dp.callback_query(F.data == "Humo")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card.card_number_2)
    await call.message.answer("Karta raqamini kiriting: ")


@dp.message(Card.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"\n \n Rahmat {message.from_user.full_name} siz Humo kartasi orqali to'lovni omalga oshirdingiz. \nBizdan harid qilganingiz uchun rahmat!!! \nYana harid qilmoqchi bo'lsangiz menu bo'limiga o'ting.",
            reply_markup=mb_1)
    else:
        await message.answer("Boshidan urinib ko'ring !!!", reply_markup=cart)
    await state.clear()


kb_2 = [
    [KeyboardButton(text="💻 Раздел Курсы"), KeyboardButton(text="🛒 Корзина"), KeyboardButton(text="📑 Информация")],
    [KeyboardButton(text="🤝 Поддерживать"), KeyboardButton(text="🔄 Изменить язык")]
]
mb_1_1 = ReplyKeyboardMarkup(keyboard=kb_2, resize_keyboard=True)

kurslar_toplami_1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💻 Frontend"),
     KeyboardButton(text="💻 Backend")],
    [KeyboardButton(text="💻 Дизайн"),
     KeyboardButton(text="🔙 Назад")]
], resize_keyboard=True)

front_toplami_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 HTML", callback_data="html_1"),
     InlineKeyboardButton(text="👨🏻‍💻 CSS and Sass", callback_data="css_1")],
    [InlineKeyboardButton(text="👨🏻‍💻 Java Script", callback_data="js_1"),
     InlineKeyboardButton(text="👨🏻‍💻 React", callback_data="react_1")]
])
#
back_toplami_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 Python", callback_data="py_1"),
     InlineKeyboardButton(text="👨🏻‍💻 C#", callback_data="c_1")],
    [InlineKeyboardButton(text="👨🏻‍💻 Java", callback_data="java_1"),
     InlineKeyboardButton(text="👨🏻‍💻 Node.js", callback_data="node_1")]
])
#
design_toplami_1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="👨🏻‍💻 Grafik design", callback_data="g_ds_1"),
     InlineKeyboardButton(text="👨🏻‍💻 Design", callback_data="ds_1")]
])


@dp.message(F.text == "💻 Frontend")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/05/31/71/02/360_F_531710260_ByieqNe7Ut6QBHgIR7xgdsxH7gICrHr1.jpg",
        caption="Вы перешли в раздел «Front end». \nВыберите здесь курс, который вам нравится.",
        reply_markup=front_toplami_1)


@dp.callback_query(F.data == "html_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали HTML. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.callback_query(F.data == "css_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали CSS и Sass. \nСколько месяцев вы хотите учиться по этому направлению?",
        reply_markup=muddat_1)


@dp.callback_query(F.data == "js_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Java Script. \nСколько месяцев вы хотите учиться по этому направлению?",
        reply_markup=muddat_1)


@dp.callback_query(F.data == "react_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали React. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.message(F.text == "💻 Backend")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://www.ipraxa.com/blog/wp-content/uploads/2021/10/frontend-vs-backend.png",
        caption="Вы перешли в раздел Back end. \nВыберите здесь курс, который вам нравится.",
        reply_markup=back_toplami_1)


@dp.callback_query(F.data == "py_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Python. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.callback_query(F.data == "c_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали C#. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.callback_query(F.data == "java_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Java. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.callback_query(F.data == "node_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Node.js. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.message(F.text == "💻 Дизайн")
async def front_function(message: types.Message):
    await message.answer("Front end", reply_markup=ReplyKeyboardRemove())
    await message.answer_photo(
        photo="https://cdn.sanity.io/images/tlr8oxjg/production/cbce8b3ffe9e0b82f5d710b56ed210546228c415-1232x690.png?w=3840&q=100&fit=clip&auto=format",
        caption="Вы перешли в раздел Дизайн. \nВыберите здесь курс, который вам нравится.",
        reply_markup=design_toplami_1)


@dp.callback_query(F.data == "g_ds_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Графический дизайн. \nСколько месяцев вы хотите учиться по этому направлению?",
        reply_markup=muddat_1)


@dp.callback_query(F.data == "ds_1")
async def html_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://t3.ftcdn.net/jpg/01/69/55/22/360_F_169552278_EwLpWLojaFu8xBmdHpHYrPWhlVPsuaRz.jpg",
        caption="Вы выбрали Дизайн. \nСколько месяцев вы хотите учиться по этому направлению?", reply_markup=muddat_1)


@dp.callback_query(F.data == "3_1")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Вы выбрали 3-месячный тип обучения.", reply_markup=pay_3_1)


@dp.callback_query(F.data == "oqish_3_1")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 3 месяца обучения")
    await call.message.answer(
        "Вы выбрали трехмесячное обучение. \nОплату можно произвести из раздела корзины.",
        reply_markup=kurslar_toplami_1)


@dp.callback_query(F.data == "6_1")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Вы выбрали 6-месячный тип обучения.", reply_markup=pay_6_1)


@dp.callback_query(F.data == "oqish_6_1")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 6 месяца обучения")
    await call.message.answer(
        "Вы выбрали 6-месячное обучение. \nОплату можно произвести из раздела корзины.",
        reply_markup=kurslar_toplami_1)


@dp.callback_query(F.data == "12_1")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Вы выбрали 12-месячный тип обучения.", reply_markup=pay_12_1)


@dp.callback_query(F.data == "oqish_12_1")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 12 месяца обучения")
    await call.message.answer(
        "Вы выбрали 12-месячное обучение. \nОплату можно произвести из раздела корзины.",
        reply_markup=kurslar_toplami_1)


@dp.callback_query(F.data == "18_1")
async def uch_function(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo="https://www.pngitem.com/pimgs/m/112-1127587_software-hire-developers-hd-png-download.png",
        caption="Вы выбрали 18-месячный тип обучения.", reply_markup=pay_18_1)


@dp.callback_query(F.data == "oqish_18_1")
async def uch_function(call: types.CallbackQuery):
    orders.append(" 18 месяца обучения")
    await call.message.answer(
        "Вы выбрали 18-месячное обучение. \nОплату можно произвести из раздела корзины.",
        reply_markup=kurslar_toplami_1)


@dp.message(F.text == "📑 Информация")
async def malumot_function(message: types.Message):
    await message.answer_photo(photo="https://texnokun.uz/wp-content/uploads/2023/02/temy-v-gruppax-telegram.jpeg",
                               caption="Telegram — это инструмент для обмена мгновенными сообщениями. Помимо текстовых сообщений обычные пользователи могут отправлять друг другу изображения, видео, аудио и различные файлы размером до 2 ГБ, совершать голосовые и видеозвонки, участвовать в голосовых и видеочатах в каналах и группах. \n\nПрограммное обеспечение доступно для Google, Android, Apple iOS, Microsoft Windows, Blackberry, MacOS, Linux и Windows Phone.",
                               reply_markup=malumot_1)

@dp.message(filters.Command("🤝 Поддерживать"))
async def start_function(message: types.Message):
    await message.answer("Xush kelibsiz, men ChatGPT botman. Qanaqa savoling bor?")


# @dp.message(F.text)
# async def text_function(message: types.Message):
#     result = await answer_process(question=message.text)
#
#     await message.answer(text=result)

@dp.message(F.text == "🔄 Изменить язык")
async def balance_function(message: types.Message):
    await message.answer(f"Вы выбрали смену языка\nИзменить язык", reply_markup=til_1)


@dp.message(F.text == "Русский язык 🇷🇺")
async def balance_function(message: types.Message):
    await message.answer(f"Вы пер ешли на русский", reply_markup=mb_1_1)


@dp.message(F.text == "💸 Покупка")
async def savat_function(message: types.Message):
    await message.answer("Вы приобрели товар \nСпасибо за покупку", reply_markup=cart_1)


@dp.message(F.text == "🛒 Корзина")
async def savat_function(message: types.Message):
    await message.answer("Вы выбрали раздел «Корзина»!", reply_markup=savat_button_1)


@dp.message(F.text == "🗑 Посмотреть корзину")
async def orders_function(message: types.Message):
    await message.answer(f"Список того, что у вас есть!!!")
    await message.answer(f"{"\n".join(orders)}", reply_markup=mb_1_1)


@dp.message(F.text == "🚮 Очистить корзину")
async def ordersdell_function(message: types.Message):
    orders.clear()
    await message.answer("Вы удалили все товары!!!", reply_markup=mb_1_1)


@dp.callback_query(F.data == "Uzcard_1")
async def pey_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Uzcard. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb_1_1)
    else:
        await message.answer("Попробуйте с начала!!!", reply_markup=cart_1)
    await state.clear()


@dp.callback_query(F.data == "Humo_1")
async def pay_function(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(Card_1.card_number_2)
    await call.message.answer("Введите номер карты: ")


@dp.message(Card_1.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer(
            f"Спасибо {message.from_user.full_name}, вы произвели оплату картой Humo. \nСпасибо, что делаете покупки у нас!!! \nЕсли вы хотите купить еще раз, перейдите в раздел «Меню».",
            reply_markup=mb_1_1)
    else:
        await message.answer("Попробуйте с начала!!!", reply_markup=cart_1)
    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
