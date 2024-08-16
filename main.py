from curl_cffi import requests
import random
import string
from faker import Faker
from fake_useragent import UserAgent
import re

fake = Faker()

global domain
domain = "domain.com"

proxies = {
    "http": "http://x:x@x.com",
    "https": "http://x:x@x.com"
}

def fakerformat():
    full = fake.name()
    f=full.split(" ")[0]
    l=full.split(" ")[1]
    return f,l
name = fakerformat()

def sec_cha(user_agent):
    chromium_versions = re.findall(r'Chrome/(\d+\.\d+\.\d+\.\d+)', user_agent)
    chrome_versions = re.findall(r'Chrome/(\d+\.\d+\.\d+\.\d+)', user_agent)
    sec_ch_ua_header = f'Chromium";v="{"".join(chromium_versions)}, Not(A:Brand)";v="24", Google Chrome";v="{"".join(chrome_versions)}"'
    return sec_ch_ua_header # generates sec_ch_ua header for cloudflare

format1 = f"{name[0]}.{name[1]}@{domain}"     #  jess smith = jess.smith@domain.com
format2 = f"{name[0][-1]}.{name[1]}@{domain}" #  jess smith = j.smith@domain.com
format3 = f"{name[0]}.{name[1][-1]}@{domain}" #  jess smith = jess.s@domain.com
format4 = f"{name[0]}{name[1]}@{domain}"      #  jess smith = jesssmith@domain.com
format5 = f"{name[0][-1]}{name[1]}@{domain}"  #  jess smith = jsmith@domain.com
format6 = f"{name[0]}{name[1][-1]}@{domain}"  #  jess smith = jesss@domain.com
format7 = f"{name[0]}_{name[1]}@{domain}"     #  jess smith = jess_smith@domain.com
format8 = f"{name[0][-1]}_{name[1]}@{domain}" #  jess smith = j_smith@domain.com
format9 = f"{name[0]}_{name[1][-1]}@{domain}" #  jess smith = jess_s@domain.com
format10 = f"Make Your Own"

#Default Password Format # "^!D2Mh)15z"

def stuff(email):
    useragent = UserAgent(min_version=122, platforms=["pc"], os="windows")
    x=200 # target sites response code for valid logins
    password = fake.password()
    data = {
        "email": format1,
        "password": password
    }
    headers = {
        "user-agent": useragent.chrome # Most phishing pages will log useragent so we add it as a precaution
    }
    r = requests.post("https://login.exampledomain.live/post.php", json=data, headers=headers, impersonate="chrome122")
    if r.status_code == x:
        print("Success")
    else:
        print(r.status_code, r.text)

def cloudflare_stuff(email):
    useragent = UserAgent(min_version=122, platforms=["pc"], os="windows")
    x=200 # target sites response code for valid logins
    sec = sec_cha(useragent)
    password = fake.password()
    data = {
        "email": format1,
        "password": password
    }
    headers = {
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://login.exampledomain.live/',
        'priority': 'u=1, i',
        'referer': 'https://login.exampledomain.live/',
        'sec-ch-ua': sec,
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': useragent.chrome,
    }
    r = requests.post("https://login.exampledomain.live/post.php", json=data, headers=headers, impersonate="chrome122")
    if r.status_code == x:
        print("Success")
    else:
        print(r.status_code, r.text)

#cloudflare_stuff(format1)
#stuff(format1)