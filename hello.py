def hello_user(only_star, length_str):
    what_print = []
    symbol_for_length = " "
    text_hello = '|Приветствую вас в программе, предоставляющей точные координаты по указанному вами адресу'
    hello_token_key = "|Перед тем как начать поиск, введите ваш: token, secret_key - " \
                      "который вами был получен при регистраиции"
    what_print.extend([text_hello.ljust(length_str, symbol_for_length),
                       hello_token_key.ljust(length_str, symbol_for_length),
                       only_star])
    print(only_star, "|\n".join(what_print), sep="\n")
    what_print.clear()
    token = input("введите ваш token = ")
    secret_key = input("введите ваш sekret_key = ")
    select_lang = "|Выберите язык, на котором хотите получить ответ от сайта dadata.ru: 'en/ru'."
    select_lang1 = "|1) ru"
    select_lang2 = "|2) en"
    what_print.extend([select_lang.ljust(length_str, symbol_for_length),
                       select_lang1.ljust(length_str, symbol_for_length),
                       select_lang2.ljust(length_str, symbol_for_length),
                       only_star])
    print(only_star, "|\n".join(what_print), sep="\n")
    language = input("Введите число ")
    print("-" * length_str)
    while language != '1' and language != 2:
        ans = '|Вы ввели некорректное значение: введите число ru - "1" или en - "2"'
        print(ans.ljust(length_str, symbol_for_length) + "|")
        print("-" * length_str)
        language = input("Введите число ")
    print(only_star)
    print("|Ответы на ваши ")