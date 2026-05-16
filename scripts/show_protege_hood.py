import json
d = json.loads(open('G:/ai_projects/nwcb/data/gear.json', encoding='utf-8').read())
hood = next((i for i in d if i['name'] == "Protégé's Hood"), None)
if hood:
    print(json.dumps(hood, indent=2, ensure_ascii=False))
else:
    print("NOT FOUND in gear.json")
