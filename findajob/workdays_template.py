import requests
import json
import pandas as pd

url = "https://ing.wd3.myworkdayjobs.com/wday/cxs/ing/JVSGBLCOR/jobs"

payload = json.dumps({
  "appliedFacets": {},
  "limit": 20,
  "offset": 0,
  "searchText": ""
})
headers = {
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': 'wd-browser-id=25ccc480-392c-43d1-ad63-faba88a891e5; CALYPSO_CSRF_TOKEN=17bcad84-2249-490d-acb0-418823989c7a; PLAY_SESSION=dc26804869bbc8ed32df60478804aeccd2d5daee-ing_pSessionId=jb9jbqv4fnobh66v9l2vjee92o&instance=vps-prod-1l2eqn5o.prod-vps.pr501.cust.dub.wd; wday_vps_cookie=2472057098.53810.0000; __cflb=02DiuJFb1a2FCfph91kR4XMuWBo9zS6ftMN5HkTm24KLg; _cfuvid=eUerj1PUst8ois0iRGlLD8bk.z.jjzlAFrEq8o6ivyQ-1733376463139-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=XHLrsyOn6ynRQ54yH71ay8X8eUFSJ2dCKT45PGHJxj8-1733379734-1.0.1.1-dC3pj9t6JCR7McdE4DuWkONVad2zEmsxh736E7PDEf1P6Tkipp4ovmmDXhxyby_ltYeEqfhqR4oyURNX1IFZxg; PLAY_SESSION=dc26804869bbc8ed32df60478804aeccd2d5daee-ing_pSessionId=jb9jbqv4fnobh66v9l2vjee92o&instance=vps-prod-1l2eqn5o.prod-vps.pr501.cust.dub.wd; __cf_bm=WQChkjstVP8k5hFW0B8W_PHsI0uLrmOo.xpPbzseGn8-1733380941-1.0.1.1-kEkKdyVls9kJe9y0_amGvpN.KhSKdVAQxBaEpoT48ilS5DYBsjW_L.sb8lRTSWbMlpdTV.TS1d_pwbppP14aLQ; __cflb=02DiuJFb1a2FCfph91mEfCE19uWmaV9PEQtbk8hBrnt12; _cfuvid=Q.RELZ3gWk_Js_jXL1LoA80NkNAusUGCfVVuPrIGWhU-1733380941452-0.0.1.1-604800000; wd-browser-id=708359b5-c6c8-4a4a-9e22-5f7f52baa82a; wday_vps_cookie=2472057098.53810.0000',
  'origin': 'https://ing.wd3.myworkdayjobs.com',
  'priority': 'u=1, i',
  'referer': 'https://ing.wd3.myworkdayjobs.com/en-US/JVSGBLCOR',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-calypso-csrf-token': '17bcad84-2249-490d-acb0-418823989c7a'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
