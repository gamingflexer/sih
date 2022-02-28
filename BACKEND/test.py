# import json

# aList = [{'text': 'text___ TEXT', 'name': [['Om'], ['Om2']], 'loc': ['Panvel']},{'text': 'text___ TEXT', 'name': [['Om'], ['Om2']], 'loc': ['Panvel']},{'text': 'text___ TEXT', 'name': [['Om'], ['Om2']], 'loc': ['Panvel']}]

# for a in aList:
#     jsonStr = json.dumps(a, indent=4)
#     jsonFile = open(
#         "/Users/cosmos/Desktop/SIH - MAIN/sih/BACKEND/data.json", "a")
#     jsonFile.write(jsonStr)
# jsonFile.close()


import http.client

conn = http.client.HTTPSConnection("hashtagy-generate-hashtags.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "hashtagy-generate-hashtags.p.rapidapi.com",
    'x-rapidapi-key': "cba192a5eemsh3f08f2e925759d7p1183a7jsn69d65156c2ae"
    }

conn.request("GET", "/v1/custom_1/tags?keyword=disaster", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))