import requests
import requests_cache
import json
import pandas as pd



requests_cache.install_cache('api_cache')
session = requests_cache.CachedSession()



# https://ing.wd3.myworkdayjobs.com/en-US/JVSGBLCOR
url = "https://ing.wd3.myworkdayjobs.com/wday/cxs/ing/JVSGBLCOR/jobs"

# where postman placed this code
#payload = json.dumps({
#  "appliedFacets": {},
#  "limit": 20,
#  "offset": 0,
#  "searchText": ""
#})

headers = {
  'accept': 'application/json',
  'accept-language': 'en-US',
  'content-type': 'application/json',
  'cookie': 'wd-browser-id=25ccc480-392c-43d1-ad63-faba88a891e5; CALYPSO_CSRF_TOKEN=17bcad84-2249-490d-acb0-418823989c7a; PLAY_SESSION=dc26804869bbc8ed32df60478804aeccd2d5daee-ing_pSessionId=jb9jbqv4fnobh66v9l2vjee92o&instance=vps-prod-1l2eqn5o.prod-vps.pr501.cust.dub.wd; wday_vps_cookie=2472057098.53810.0000; __cflb=02DiuJFb1a2FCfph91kR4XMuWBo9zS6ftMN5HkTm24KLg; _cfuvid=eUerj1PUst8ois0iRGlLD8bk.z.jjzlAFrEq8o6ivyQ-1733376463139-0.0.1.1-604800000; timezoneOffset=480; __cf_bm=XHLrsyOn6ynRQ54yH71ay8X8eUFSJ2dCKT45PGHJxj8-1733379734-1.0.1.1-dC3pj9t6JCR7McdE4DuWkONVad2zEmsxh736E7PDEf1P6Tkipp4ovmmDXhxyby_ltYeEqfhqR4oyURNX1IFZxg; PLAY_SESSION=dc26804869bbc8ed32df60478804aeccd2d5daee-ing_pSessionId=jb9jbqv4fnobh66v9l2vjee92o&instance=vps-prod-1l2eqn5o.prod-vps.pr501.cust.dub.wd; __cf_bm=0uBMVXyPSYTj.Bs1kdi09X17ryTzDtHXkRbIKlhsDA0-1733389804-1.0.1.1-DG2vXoOwoptjHmEYhXbTkZBNfE9gpIKuOAeB_eE.DsFtXQshbTYbWytNMY4dXD3suU4TNynJDn6Zv1EWmzPNVQ; __cflb=02DiuJFb1a2FCfph91mEfCE19uWmaV9PEQtbk8hBrnt12; _cfuvid=j..OFaTbV2PLE9YfQyusJbs04aEtGwc2cLdLcXxMeW4-1733389804588-0.0.1.1-604800000; wd-browser-id=708359b5-c6c8-4a4a-9e22-5f7f52baa82a; wday_vps_cookie=2472057098.53810.0000',
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



# Pagination variables
# Limit = how much entries you can extract from the data
limit = 10
# Offset = pointer/index of the current entry, think of data as an array
offset = 0
MAX_JOBS = 51
# store each json entry
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

# If you want to manually clear cache, uncomment the line below, then run and comment out the same line.
#requests_cache.clear()



# if interested in generating only the content of the first page or limit
# then remove while loop above and uncomment the lines below
#response = session.request("POST", url, headers=headers, data=payload)
#responseJSON = json.loads(response.text)
#df = pd.DataFrame(responseJSON["jobPostings"], index=None)
try:
    df = pd.DataFrame(allJobs, index=None)
    print(df)
    print("\n\n\n")
    df.dropna(inplace=True)
    columns=["Title", "Link", "Type", "Location", "Posted On", "Job ID"]
    df.columns = columns
    df["Title"] = df["Title"].str.lower()
    df["Title"] = df["Title"].str.strip()
    df["Posted On"] = df["Posted On"].str.lower()
    df["Posted On"] = df["Posted On"].str.strip()
    df = df[df["Title"].str.contains("software", na=False) | df["Title"].str.contains("it", na=False) | df["Title"].str.contains("programmer", na=False)]
    df = df[df["Posted On"].str.contains("today", na=False)]
    # filter df by location here
    print(df)
    print("\n\n\n")
    df.to_csv("jobs_data.csv", index=False)
    print("A .csv file has been created.")
except Exception as e:
    print(f"An error occurred while generating the dataframe.: {e}")
