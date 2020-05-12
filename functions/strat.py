import os
import json
import random

# Returns list of given amount of dota heroes


def dota(amount=1998):
    if amount == 1998:
        string = "Выберите количество героев (1-5) для страты. Использование !strat [1-5]"
        return string
    elif amount > 5:
        if amount > 10:
            string = "Зачем тебе так много героев, ты че удумал, а, сука?"
            return string
        else:
            string = f"Не, ну я тебе, конечно нарандомлю героев, только я не очень понимаю к чему тебе их целых {amount}... \n"
            for i in range(amount):
                hero = random.choice(
                    list(open('./data/dota.txt', encoding="utf-8")))
                string = string + hero
            return string
    else:
        string = "Твои герои для страты: \n"
        for i in range(amount):
            hero = random.choice(
                list(open('./data/dota.txt', encoding="utf-8")))
            string = string + hero
        return string
