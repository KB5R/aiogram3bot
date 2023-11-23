import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import InputMediaPhoto
import keyboard as kb
from dotenv import load_dotenv
import os
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder

logging.basicConfig(level=logging.INFO)

load_dotenv()
bot = Bot(os.getenv('TOKEN'), parse_mode='HTML')
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(F.text == '/start')
async def cmd_start(message: Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAIHI2Vd_nveUfm3Jm_Id43i0JW_2qKiAAKLzjEbhVXwSt_Wjo0LTGHBAQADAgADeQADMwQ',
        caption=f'Доброго времени суток,{message.from_user.first_name} 👋\n'
                f'Наш магазин одежды предлагает широкий ассортимент\n'
                f'стильной и качественной одежды для женщин, мужчин и детей.\n'
                f'Мы предлагаем различные модели одежды, от повседневной до \n'
                f'более формальной, а также аксессуары, обувь и сумки.\n'
                f'\n'
                f'В нашем магазине вы найдете одежду разных размеров и\n'
                f'стилей, чтобы каждый мог выбрать то, что ему подходит.\n'
                f'Мы следим за последними тенденциями моды и постоянно\n'
                f'обновляем нашу коллекцию, чтобы удовлетворить потребности\n'
                f'наших клиентов.\n'
                f'\n'
                f'<u>Мы гарантируем качество каждого изделия, так как мы</u>\n'
                f'<u>работаем только с проверенными поставщиками,</u>\n'
                f'<u>использующими только высококачественные материалы.</u>\n'
                f'\n'
                f'Наша команда продавцов-консультантов всегда готова помочь\n'
                f'вам с выбором и ответить на все ваши вопросы. Мы стремимся\n'
                f'создать уютную и дружелюбную атмосферу в магазине, чтобы\n'
                f'вы могли насладиться покупками.\n'
                f'\n'
                f'Посетив наш магазин одежды, вы найдете все необходимое для\n'
                f'создания своего стильного и модного образа.', reply_markup=kb.main)


@dp.message(F.text == 'Кроссовки')
async def brendkrs (message: Message):
    await message.answer('Выберете бренд', reply_markup=kb.brandkrs)


#Кросовки AIR MAX TERRASCAPE 90 NN------------------------------------------------------------------------------------------------

@dp.message(F.text == 'Nike')
async def shoes (message: Message):
    await message.answer('Выберете кроссовки', reply_markup=kb.nike)


@dp.message(F.text == 'AIR MAX TERRASCAPE 90 NN')
async def cmd_album(message: Message):
    album_builder = MediaGroupBuilder(
        caption=f'Кроссовки Nike Air Max Dawn выполнены из текстиля и искусственной кожи.\n'
                f'\n'
                f'Детали: шнуровка, амортизирующая вставка Air гарантирует мягкость каждого шага.\n'
                f'\n'
                f'Cпециальный фиксатор удерживает пятку для дополнительного комфорта при ходьбе,\n'
                f'\n'
                f'Петля на заднике для удобства переобувания\n'
                f'\n'
                f'<u>Цена: 25 990 ₽</u>')

    # Если мы сразу знаем тип, то вместо общего add
    # можно сразу вызывать add_<тип>

    album_builder.add_photo(
        media='AgACAgIAAxkBAAIGwWVd8SQAATwK8S5_8czIm16tYbYexQACxM8xG4VV6EqRtfMDeAJe7wEAAwIAA3kAAzME',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIGw2Vd8SSkVkisSlF4HZn94SB151fuAAK4zzEbhVXoSmJeaYmkw5HuAQADAgADeQADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIGwmVd8SRXaYHgB8umajU_SvP7T5fbAALDzzEbhVXoSl1Y7FuzSSLLAQADAgADeQADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIG8WVd-okkMNa9zxUqMu-5RSrzZl6BAAJ3zjEbhVXwShZP0h1kXS5DAQADAgADeQADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIG8mVd-ol3ywLKV4RJBHLd_qtGYWsrAAJ4zjEbhVXwSi7ARalM4g_XAQADAgADeQADMwQ',
    )

    await message.answer_media_group(
        # Не забудьте вызвать build()
        media=album_builder.build()
    )

#----------------------------------------------------------------------------------------------------------------------

#Кросовки Air ZOOMX VAPORFLY-------------------------------------------------------------------------------------------

@dp.message(F.text == 'Air ZOOMX VAPORFLY')
async def cmd_album(message: Message):
    album_builder = MediaGroupBuilder(
        caption=f'Кроссовки выполнены из сетчатого текстиля.\n'
                f'\n'
                f'Полноразмерная пластина из углеродного волокна под ногами создает ощущение движения\n'
                f'помогая увеличить темп.\n'
                f'\n'
                f'Водостойкий материал VaporWeave безумно прочный и безумно легкий.\n'
                f'Пеноматериал Nike ZoomX в передней части стопы обеспечивает исключительную отдачу энергии.\n'
                f'\n'
                f'<u>Цена: 23 993  ₽</u>')

    # Если мы сразу знаем тип, то вместо общего add
    # можно сразу вызывать add_<тип>

    album_builder.add_photo(
        media='AgACAgIAAxkBAAIHqmVeDGT3LLmnoM0ErsxnDJMCEwcAA_jOMRuFVfBKwtO2vZdTrPQBAAMCAAN5AAMzBA',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIHrGVeDGSrZh4tQGHBqQtesuSF-DAbAAL3zjEbhVXwSt0gT4BwNcU0AQADAgADeAADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIHq2VeDGR0mimSw-G3K4zmaYmdHiBcAAL2zjEbhVXwSvtZOtCABnc1AQADAgADeQADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIHrmVeDGSfBil_j9cGuPzNHSeHn9U8AAL6zjEbhVXwSlh52qsWpZbzAQADAgADeAADMwQ',
    )
    album_builder.add_photo(
        media='AgACAgIAAxkBAAIHrWVeDGSO5LGYpxI46MJmBCezOXibAAL5zjEbhVXwSibddPRaoTXnAQADAgADeAADMwQ',
    )

    await message.answer_media_group(
        # Не забудьте вызвать build()
        media=album_builder.build()
    )
#----------------------------------------------------------------------------------------------------------------------

@dp.message(F.text == 'Профиль')
async def cmd_my_id(message: Message):
    await message.answer(f'Ваше имя: {message.from_user.first_name}')
    await message.answer(f'Ваш ID: {message.from_user.id}')

@dp.message(F.text == 'Репозитории')
async def repository(message: Message):
    await message.answer('Мои репозитории GitHub', reply_markup=kb.repo)


@dp.message(F.text == 'ladmin')
async def cmd_auth(message: types.Message):
    if message.from_user.id not in [702918039]:
        await message.answer('Ошибся адресом, дружок')
    else:
        await message.answer('✋', reply_markup=kb.admin)

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(message.photo[-1].file_id)

@dp.message(F.document)
async def get_document(message: Message):
    await message.answer(message.document.file_id)

















# Ответы на несуществующие команды

@dp.message()
async def echo(message: Message):
    await message.answer('Такой команды необнаружено')

async def main():
    await dp.start_polling(bot)


# The main() function is run only if the script is run from this file
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Выход')