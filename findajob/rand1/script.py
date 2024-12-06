import requests
import requests_cache
import json
import pandas as pd



requests_cache.install_cache('api_cache')

# ========== ONE ======================================================================================================

session = requests_cache.CachedSession()

# https://ngc.wd1.myworkdayjobs.com/en-US/Northrop_Grumman_External_Site
url = "https://ngc.wd1.myworkdayjobs.com/wday/cxs/ngc/Northrop_Grumman_External_Site/jobs"

headers = {
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': '_ga=GA1.4.1879089968.1725735584; __cflb=02DiuEyZJzFVW6zKk23dzrfyh8dkkAVvMhDHm8ZPpkXbr; wd-browser-id=d47ffec3-33cf-45d6-8a3c-266d3c9168e3; CALYPSO_CSRF_TOKEN=8bcdc03e-11ee-4857-b57f-f679df794cf1; PLAY_SESSION=e271d7d54c98be257c54bf2e953928c5546d28a9-ngc_pSessionId=dg4s95oavkmrinbjl45ij768n9&instance=vps-prod-07lemcfi.prod-vps.pr501.cust.ash.wd; wday_vps_cookie=3178788874.53810.0000; _cfuvid=KwU0RvdImDqp153P2JoINELNLkVxu8lSLpVP0K09mWM-1733425555726-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=cHzKFSZguVos.6rv8rX1tgbmhYlaX1i4sm18XQ.wUIU-1733430745-1.0.1.1-AGu6cx6Wy6tGkTFL70UTcLlC5ANjfihqWUSL9vmMdQzD2Nkoslefy6a2iNtlIWxhaIvInXJ8qFWw5JwSnf9AQA; _gat=1; PLAY_SESSION=e271d7d54c98be257c54bf2e953928c5546d28a9-ngc_pSessionId=dg4s95oavkmrinbjl45ij768n9&instance=vps-prod-07lemcfi.prod-vps.pr501.cust.ash.wd; __cf_bm=eRklueTvVvzVNW4brrZnd.BS95H.KTgjNBv0m7QW464-1733430899-1.0.1.1-mSKW2Yp_XE4RLn6M5dDoiOAycBgfAwKIOJQrpBoeliX1Xm7u.lrIzoVhsS19OORTvDUNtWao.WMqvW1RQu1Seg; _cfuvid=qURxV3HtzqvdunUc.fTNgLLE5r4xoTtdGXHVGgiTkH8-1733430899585-0.0.1.1-604800000; wday_vps_cookie=3178788874.53810.0000',
  'origin': 'https://ngc.wd1.myworkdayjobs.com',
  'priority': 'u=1, i',
  'referer': 'https://ngc.wd1.myworkdayjobs.com/en-US/Northrop_Grumman_External_Site',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-calypso-csrf-token': '8bcdc03e-11ee-4857-b57f-f679df794cf1'
}

limit = 10
offset = 0
MAX_JOBS = 101
allJobs = []

while offset < MAX_JOBS:
    # Prepare payload with the updated offset
    payload = json.dumps({
        "appliedFacets": {},
        "limit": limit,
        "offset": offset,
        "searchText": ""
    })

    # Make the request and store it in cache for an specified period of time
    response = session.request("POST", url, headers=headers, data=payload, expire_after=3600)
    responseJSON = json.loads(response.text)

    # Extract job postings and append to the list
    jobs = responseJSON.get("jobPostings", [])
    if not jobs:
        break  # Stop if no jobs are returned

    allJobs.extend(jobs)
    offset += limit  # Increment the offset for the next page

# ========== END OF ONE ===============================================================================================





# ========== TWO ======================================================================================================

session2 = requests_cache.CachedSession()

# https://globalhr.wd5.myworkdayjobs.com/REC_RTX_Ext_Gateway
url = "https://globalhr.wd5.myworkdayjobs.com/wday/cxs/globalhr/REC_RTX_Ext_Gateway/jobs"

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
  'cookie': '__cflb=02DiuHJZe28xXz6hQKLeTYyWYf7NxYcM1UosQfnbyryVe; wd-browser-id=e6e13693-0956-4cb4-9774-92c5b7f6fafe; CALYPSO_CSRF_TOKEN=fbe1c562-cc60-4246-b72d-19ca9d7a8e76; PLAY_SESSION=abab593f269af15d68babc7377e42ad4317e10d0-globalhr_pSessionId=2rdj1bcshpteiep3oaq7kpopvu&instance=vps-prod-rfmlfqph.prod-vps.pr502.cust.pdx.wd; wday_vps_cookie=4193033226.53810.0000; _cfuvid=LN6PHarfgFkLWg4N3YDUxLBz1zFzU7hAUy3aKqbCrAw-1733425557779-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=ZShsXE8Dxu6Duq51UB0P1vlLPTcfkKfP7zo9NnJOwnk-1733432465-1.0.1.1-Xw44zh5KaY5LNgRyWnCgNt0e4o4pOMQhAPksQUbzZE0ZkM2sdhGXwVV7so87uBafU8L7dth8l._r7.eBxhBFvA; PLAY_SESSION=abab593f269af15d68babc7377e42ad4317e10d0-globalhr_pSessionId=2rdj1bcshpteiep3oaq7kpopvu&instance=vps-prod-rfmlfqph.prod-vps.pr502.cust.pdx.wd; __cf_bm=E1tBkf0tjgvrIO8MC4qIrSbMNDoS3UQJrVOfuBet4Kc-1733433070-1.0.1.1-dAI1xCkOWXScvlI3_kBNngcuH77Ym0VrOn1hOGe8jS6opHlcUnapLbohgAbT4dNAVhKXNffDRyiwWmNEILh3eQ; _cfuvid=UHocRaA3umEx6VfUj2ShIgAisiJ3JV6nHlBsMXgf_us-1733433070966-0.0.1.1-604800000; wday_vps_cookie=4193033226.53810.0000',
  'origin': 'https://globalhr.wd5.myworkdayjobs.com',
  'priority': 'u=1, i',
  'referer': 'https://globalhr.wd5.myworkdayjobs.com/REC_RTX_Ext_Gateway',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-calypso-csrf-token': 'fbe1c562-cc60-4246-b72d-19ca9d7a8e76'
}

limitTwo = 10
offsetTwo = 0
MAX_JOBS_TWO = 101
allJobsTwo = []

while offsetTwo < MAX_JOBS_TWO:
    # Prepare payload with the updated offset
    payload = json.dumps({
        "appliedFacets": {},
        "limit": limitTwo,
        "offset": offsetTwo,
        "searchText": ""
    })

    # Make the request and store it in cache for an specified period of time
    response2 = session2.request("POST", url, headers=headers, data=payload, expire_after=3600)
    responseJSONTwo = json.loads(response2.text)

    # Extract job postings and append to the list
    jobsTwo = responseJSONTwo.get("jobPostings", [])
    if not jobsTwo:
        break  # Stop if no jobs are returned

    allJobsTwo.extend(jobsTwo)
    offsetTwo += limitTwo  # Increment the offset for the next page

# ========== END OF TWO ===============================================================================================





# ========== THREE ====================================================================================================

session3 = requests_cache.CachedSession()

# https://aero.wd5.myworkdayjobs.com/External
url = "https://aero.wd5.myworkdayjobs.com/wday/cxs/aero/External/jobs"

headers = {
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': '__cflb=02DiuHJZe28xXz6hQKLf1exjNbMDM5uxfSuz98WwFpZNC; wd-browser-id=62a20c2b-8cd1-427d-8029-34a3cf0c2063; CALYPSO_CSRF_TOKEN=dcb3411f-5e2b-4796-b73c-be15c17fea51; PLAY_SESSION=bc46c8d61a48ebbc431c28d60fd76e3f689c154d-aero_pSessionId=8d6fc3s7ujnngf8f6afnq2bk4i&instance=vps-prod-2jxlxr5m.prod-vps.pr501.cust.pdx.wd; wday_vps_cookie=434805770.53810.0000; _cfuvid=xf1txket3rZDoC7ygwIhihskySJ9nY0IQzVp02JfZpM-1733434426580-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=8w5lOomjIl_5Vv6fZ4XF4pZbl3BYEv_7PLEWb0HmMJY-1733436971-1.0.1.1-KrvVi.pjLGhpNeILq98wRIgugFSD5EecZSjmeYKaF9s6iBUTXih0XQBLbHfz5e1s.bBoiksa3Ms0CfcFp96aEQ; PLAY_SESSION=bc46c8d61a48ebbc431c28d60fd76e3f689c154d-aero_pSessionId=8d6fc3s7ujnngf8f6afnq2bk4i&instance=vps-prod-2jxlxr5m.prod-vps.pr501.cust.pdx.wd; __cf_bm=e85hb3YQJyEEtWOA.VXlcoHKVcl0Uk3L4ILgkgtdrkU-1733437932-1.0.1.1-jMGBwh_BrL6_pzmRlc3led9rpaBYeSQ5LKe..m5kFCospc4a9EJlQ_KS04l7w.2eLbzMcf4u9GEg6EpUEdlWZw; _cfuvid=cofA5i_Fu6rtWP8yHmBprjnMSHrG0Q7tqndgwisjSV8-1733437932277-0.0.1.1-604800000; wday_vps_cookie=434805770.53810.0000',
  'origin': 'https://aero.wd5.myworkdayjobs.com',
  'priority': 'u=1, i',
  'referer': 'https://aero.wd5.myworkdayjobs.com/External',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-calypso-csrf-token': 'dcb3411f-5e2b-4796-b73c-be15c17fea51'
}

limitThree = 10
offsetThree = 0
MAX_JOBS_THREE = 101
allJobsThree = []

while offsetThree < MAX_JOBS_THREE:
    # Prepare payload with the updated offset
    payload = json.dumps({
        "appliedFacets": {},
        "limit": limitThree,
        "offset": offsetThree,
        "searchText": ""
    })

    # Make the request and store it in cache for an specified period of time
    response3 = session3.request("POST", url, headers=headers, data=payload, expire_after=3600)
    responseJSONThree = json.loads(response3.text)

    # Extract job postings and append to the list
    jobsThree = responseJSONThree.get("jobPostings", [])
    if not jobsThree:
        break  # Stop if no jobs are returned

    allJobsThree.extend(jobsThree)
    offsetThree += limitThree  # Increment the offset for the next page

# ========== END OF THREE =============================================================================================





# ========== FOUR  ====================================================================================================

session4 = requests_cache.CachedSession()

# https://boeing.wd1.myworkdayjobs.com/EXTERNAL_CAREERS
url = "https://boeing.wd1.myworkdayjobs.com/wday/cxs/boeing/EXTERNAL_CAREERS/jobs"

headers = {
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': 'wd-browser-id=32bd1299-88ac-46e5-ba2f-86a1e1ace050; CALYPSO_CSRF_TOKEN=b592c648-0895-494b-8bc0-aca3efefe7d5; PLAY_SESSION=6f2a75aa7625d235a69b4bb7a28b081b93ad81f7-boeing_pSessionId=hmj3ln1n3cbc2p41gl3b6obf9v&instance=vps-prod-v10zu64i.prod-vps.pr502.cust.ash.wd; wday_vps_cookie=3984160778.53810.0000; __cflb=02DiuEyZJzFVW6zKk23ddk9h3x7TomPC1xfJ692KaEaDJ; _cfuvid=p0dZnD7GXU5Ef6aK5N1s61LLyXqQ8tUQKjqXsHYVZs8-1733443859833-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=VS32NsSEVYDKrUmKYdqvZVsmFWPnzN3uqy7J_px04oc-1733445428-1.0.1.1-4fC83wj.SvYIqOemhxrgqq_1DKg8UlSIF3KN1r1kKh_dtk75fiapAe5LfNa0.504ROLHqPuM0bPP6JNseNp.EA; PLAY_SESSION=6f2a75aa7625d235a69b4bb7a28b081b93ad81f7-boeing_pSessionId=hmj3ln1n3cbc2p41gl3b6obf9v&instance=vps-prod-v10zu64i.prod-vps.pr502.cust.ash.wd; __cf_bm=IEJ4PEZw2SdS3ATBZN6mxSQDjF67Bhe15yNMJF9O65Q-1733445530-1.0.1.1-gjS1KdoTimVMe7Jr9ehE2MSl_m25bQ2RgS4PaGQehGKsCfYzXUZ5mMhj_ygTFt1NfLGpQvn45n4CnOy041qHcg; _cfuvid=X2MOkdvE2lEwMKoF7O75EBE_xudnniS070pUigHB95w-1733445530333-0.0.1.1-604800000; wday_vps_cookie=3984160778.53810.0000',
  'origin': 'https://boeing.wd1.myworkdayjobs.com',
  'priority': 'u=1, i',
  'referer': 'https://boeing.wd1.myworkdayjobs.com/EXTERNAL_CAREERS',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
  'x-calypso-csrf-token': 'b592c648-0895-494b-8bc0-aca3efefe7d5'
}

limitFour = 10
offsetFour = 0
MAX_JOBS_FOUR = 51
allJobsFour = []

while offsetFour < MAX_JOBS_FOUR:
    # Prepare payload with the updated offset
    payload = json.dumps({
        "appliedFacets": {},
        "limit": limitFour,
        "offset": offsetFour,
        "searchText": ""
    })

    # Make the request and store it in cache for an specified period of time
    response4 = session4.request("POST", url, headers=headers, data=payload, expire_after=3600)
    responseJSONFour = json.loads(response4.text)

    # Extract job postings and append to the list
    jobsFour = responseJSONFour.get("jobPostings", [])
    if not jobsFour:
        break  # Stop if no jobs are returned

    allJobsFour.extend(jobsFour)
    offsetFour+= limitFour # Increment the offset for the next page

# ========== END OF FOUR ==============================================================================================





try:
    df = pd.DataFrame(allJobs, index=None)
    df.dropna(inplace=True)
    columns=["Title", "Link", "Type", "Location", "Posted On", "Job ID"]
    df.columns = columns
    df["Company"] = "Northrop Grumman"
    col = df.pop("Company")
    df.insert(0, col.name, col)
    df["Title"] = df["Title"].str.lower()
    df["Title"] = df["Title"].str.strip()
    df["Posted On"] = df["Posted On"].str.lower()
    df["Posted On"] = df["Posted On"].str.strip()
    df["Location"] = df["Location"].str.strip()
    df = df[df["Title"].str.contains("software", na=False) |
            df["Title"].str.contains("it ", na=False) |
            df["Title"].str.contains("information ", na=False) |
            df["Title"].str.contains("data", na=False) |
            df["Title"].str.contains("programmer", na=False)]
    df = df[df["Posted On"].str.contains("today", na=False)]
    df = df[df["Link"].str.contains("United-States", na=False)]


    df2 = pd.DataFrame(allJobsTwo, index=None)
    df2.dropna(inplace=True)
    df2.columns = columns
    df2["Company"] = "RTX"
    col = df2.pop("Company")
    df2.insert(0, col.name, col)
    df2["Title"] = df2["Title"].str.lower()
    df2["Title"] = df2["Title"].str.strip()
    df2["Posted On"] = df2["Posted On"].str.lower()
    df2["Posted On"] = df2["Posted On"].str.strip()
    df2["Location"] = df2["Location"].str.strip()
    df2 = df2[df2["Title"].str.contains("software", na=False) |
            df2["Title"].str.contains("it ", na=False) |
            df2["Title"].str.contains("information ", na=False) |
            df2["Title"].str.contains("data", na=False) |
            df2["Title"].str.contains("programmer", na=False)]
    df2 = df2[df2["Posted On"].str.contains("today", na=False)]
    df2 = df2[df2["Link"].str.contains("USA", na=False)]


    df3 = pd.DataFrame(allJobsThree, index=None)
    df3.dropna(inplace=True)
    columns=["Title", "Link", "Location", "Posted On", "Job ID"]
    df3.columns = columns
    df3["Company"] = "Boeing"
    col = df3.pop("Company")
    df3.insert(0, col.name, col)
    df3.insert(2, "Type", "See details")
    df3["Title"] = df3["Title"].str.lower()
    df3["Title"] = df3["Title"].str.strip()
    df3["Posted On"] = df3["Posted On"].str.lower()
    df3["Posted On"] = df3["Posted On"].str.strip()
    df3["Location"] = df3["Location"].str.strip()
    df3 = df3[df3["Title"].str.contains("software", na=False) |
            df3["Title"].str.contains("it ", na=False) |
            df3["Title"].str.contains("information ", na=False) |
            df3["Title"].str.contains("data", na=False) |
            df3["Title"].str.contains("programmer", na=False)]
    df3 = df3[df3["Posted On"].str.contains("today", na=False)]
    df3 = df3[df3["Link"].str.contains("CA", na=False)]


    df4 = pd.DataFrame(allJobsFour, index=None)
    df4.dropna(inplace=True)
    columns=["Title", "Link", "Location", "Posted On", "Type", "Job ID"]
    df4.columns = columns
    df4["Company"] = "Boeing"
    col = df4.pop("Company")
    df4.insert(0, col.name, col)
    col = df4.pop("Type")
    df4.insert(2, col.name, col)
    df4["Title"] = df4["Title"].str.lower()
    df4["Title"] = df4["Title"].str.strip()
    df4["Posted On"] = df4["Posted On"].str.lower()
    df4["Posted On"] = df4["Posted On"].str.strip()
    df4["Location"] = df4["Location"].str.strip()
    df4 = df4[df4["Title"].str.contains("software", na=False) |
            df4["Title"].str.contains("it ", na=False) |
            df4["Title"].str.contains("information ", na=False) |
            df4["Title"].str.contains("data", na=False) |
            df4["Title"].str.contains("programmer", na=False)]
    df4 = df4[df4["Posted On"].str.contains("today", na=False)]
    df4 = df4[df4["Link"].str.contains("USA", na=False)]


    dfCombined = pd.concat([df, df2, df3, df4])
    dfCombined.to_csv("jobs_data.csv", index=False)
    print("A .csv file has been created in your folder.")
except Exception as e:
    print(f"An error occurred while generating the dataframe.: {e}")
