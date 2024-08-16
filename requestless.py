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

useragen = UserAgent(min_version=122, platforms=["pc"], os="windows")
useragent = useragen.chrome

#request format - r=requests.post("domain.com", impersonate="chrome122")