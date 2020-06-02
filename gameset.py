import json

def character(name): ## 캐릭터 생성
    character = {
        "name" : name,
        "myhp" : 100,
        "yourhp" : 100,
        "skill" : ["정권찌르기", "원인치펀치", "뒤돌려차기"]
    }
    with open("static/save.txt", "w", encoding='utf-8') as f:
        json.dump(character, f, ensure_ascii = False)
    return character

def save_game(filename, character): ## 게임 파일 저장
    f = open(filename, "w", encoding="utf-8")
    for key in character:
        print("%s:%s" % (key, character[key]))
        f.write("%s:%s" % (key, character[key]))
    f.close()