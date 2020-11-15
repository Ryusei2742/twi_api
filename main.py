import json
from requests_oauthlib import OAuth1Session

API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_SECRET_TOKEN = ''

# 情報の取得
twitter = OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
params = {'count':5} #辞書型 個数指定

res = twitter.get(url, params = params)
# print(res.status_code) 200

timelines = json.loads(res.text)
# print(timelines[0])
timeline = timelines[0]
# print(timeline["user"]["name"]) #ユーザーの名前を取得
# print(timeline['user']['description']) #ユーザーのユーザーのプロフィール文を取得
# print(timeline['text']) #ユーザーのツイートの文を取得

#投稿
twitter = OAuth1Session(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN)
url = 'https://api.twitter.com/1.1/statuses/update.json'
params = {'status' : 'APIお試し'}
res = twitter.post(url, params = params)
print(res)






