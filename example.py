from bitChangerSDK import SDK

sdk = SDK.SDK("private_key", "public_key")
# Get balance
balance = sdk.Token.balance("USDTTRC")
print(balance)

# Создание транзакции на ввод по фиатным направлениям
invoice_response = sdk.Transaction.transaction_create_in(
    token="CARDRUB",  # CARDRUB - фиат рубль эквайринг через киви, для P2P решения токен CARDRUBP2P
    callback_url="https://ngrok.io",
    # сюда мы пришлём external_id, по которому можно будет узнать информацию по транзакции
    card_number="123456789",
    # обязательно должен совпадать с номером карты, с которой клиент будет совершать пополнение
    amount=1000,
    email="example@gmail.com"  # почта вашего клиента
)

print(f"Fiat RUB transaction response: {invoice_response}")

# Создание транзакции на ввод криптовалюты
invoice_response = sdk.Transaction.transaction_create_in(
    token="ETH",
    callback_url="https://ngrok.io",
    email="example@gmail.com",
    amount=1000
)
"""
Почему не указывается amount?
Потому что для создания транзакции на ввод по криптовалюте мы создаём новый кошелёк,
и вы можете пополнить его на любую сумму, а мы сами отловим эту транзакцию и пришлём вам колбэк
с нашим идентификатором этой транзкции. Главное, чтобы транзакция проходила по минимальным лимитам
на ввод, иначе она потеряется, и мы не сможем вернуть средства.
То есть при желании вы можете создать одну транзакцию
"""

print(f"Crypto transaction response: {invoice_response}")

# Создание транзакции на вывод

withdraw_response = sdk.Transaction.transaction_create_out(
    callback_url="https://ngrok.io",
    token="CARDRUB",
    receiver="123456789",  # в случае криптовалют вы просто указываете криптокошелёк
    amount=2500
)

print(f"Fiat RUB withdraw transaction response: {withdraw_response}")

"""
Важно уточнить, что для вывода средств, полученных через токен CARDRUBP2P нужно использовать
токен USDTTRC, так как зачисления при пополнении CARDRUBP2P конвертируются в баланс по тезеру.
"""

# Получение информации по курсу обмена
exchange_rate = sdk.Order.get_exchange_rate(
    token_from="USDTTRC",
    token_to="CARDRUB"
)

print(f"Exchange rate: {exchange_rate}")

# Создание обмена
swap_response = sdk.Swap.swap_create(
    token_from="USDTTRC",
    token_to="BTC",
    amount=1500,  # количество токенов, из которых производится обмен
    callback_url="https://ngrok.io"
)

print(f"Swap response: {swap_response}")

# Создание пэйформы
"""
Наша платёжная форма - это универсальный способ получать необходимую вам валюту, вне зависимости от того,
какой валютой удобно оплачивать ваши товары или услуги пользователем
"""
pay_form_response = sdk.Order.create_pay_form(
    token="USDTTRC",
    amount=300,
    callback_url="https://ngrok.io"
)

print(f"PayFrom response {pay_form_response}")