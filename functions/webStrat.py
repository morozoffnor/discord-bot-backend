import os
import json
import random


def singledraft():
    htmlstring = ""
    strength = random.choice(list(open('./data/dota/s.txt', encoding="utf-8")))
    agility = random.choice(list(open('./data/dota/a.txt', encoding="utf-8")))
    intelligence = random.choice(
        list(open('./data/dota/i.txt', encoding="utf-8")))

    html = """
<h1 style="text-align: center;">&nbsp;{}<img style="margin-bottom: -10;" src="http://govnoed.ml/apicontent/Strength.png" alt="http://govnoed.ml/apicontent/Strength.png" width="40" height="40" /></h1>
<h1 style="text-align: center;">{}<img style="margin-bottom: -10;" src="http://govnoed.ml/apicontent/Agility.png" alt="http://govnoed.ml/apicontent/Agility.png" width="40" height="40" /></h1>
<h1 style="text-align: center;">{}<img style="margin-bottom: -10;" src="http://govnoed.ml/apicontent/Intelligence.png" alt="http://govnoed.ml/apicontent/Intelligence.png" width="40" height="40" /></h1>
    
    
    """.format(strength, agility, intelligence)
    return html
