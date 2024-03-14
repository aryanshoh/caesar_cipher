import modules


def launch_app():
    modules.greeting()
    is_coding = modules.is_coding()
    lang = modules.choose_language()
    key = modules.chose_key(lang)
    text = modules.get_text()

    if is_coding:
        print(modules.coding_text(text, lang, key))
    else:
        print(modules.decoding_text(text, lang, key))


launch_app()
