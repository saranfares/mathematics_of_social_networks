import json
import sys

import numpy as np

MAIN_DIR = "data/"

users = "U4INQZOPSUaj8hMjLlZ3KA PKEzKWv_FktMm2mGPjwd0Q d_TBs6J3twMy9GChqUEXkg bLbSNkLggFnqwNNzzq-Ijw cMEtAiW60I5wE_vLfTxoJQ JaqcCU3nxReTW2cBLHounA QJI9OSEn6ujRCtrX06vs1w YMgZqBUAddmFErxLtCfK_w 1O638BDK_fWuxgTVJwff-A kmE8w5Y785eZmodsx0V6Ag tH0uKD-vNwMoEc3Xk3Cbdg UYcmGbelzRa0Q6JqzLoguw 8DEyKVyplnOcSKx39vatbg C2C0GPKvzWWnP57Os9eQ0w DeVGAiOf2mHVUDfxvuhVlQ Ryxj0u0AW3mRsRypdYli2A DK57YibC5ShBmqQl97CKog whINg-cC-FiAv_ATDGMDTg w-w-k-QXosIKQ8HQVwU6IQ n86B7IkbU20AkxlFX_5aew U4INQZOPSUaj8hMjLlZ3KA PKEzKWv_FktMm2mGPjwd0Q bLbSNkLggFnqwNNzzq-Ijw YMgZqBUAddmFErxLtCfK_w kmE8w5Y785eZmodsx0V6Ag 1O638BDK_fWuxgTVJwff-A QJI9OSEn6ujRCtrX06vs1w DeVGAiOf2mHVUDfxvuhVlQ Ryxj0u0AW3mRsRypdYli2A UYcmGbelzRa0Q6JqzLoguw d_TBs6J3twMy9GChqUEXkg EiwxlbR8fb68lMgEXhcWKA C2C0GPKvzWWnP57Os9eQ0w tH0uKD-vNwMoEc3Xk3Cbdg JaqcCU3nxReTW2cBLHounA 8DEyKVyplnOcSKx39vatbg F_5_UNX-wrAFCXuAkBZRDw whINg-cC-FiAv_ATDGMDTg n86B7IkbU20AkxlFX_5aew hkSiQAfl6w3882JJQzRTlQ PKEzKWv_FktMm2mGPjwd0Q bLbSNkLggFnqwNNzzq-Ijw U4INQZOPSUaj8hMjLlZ3KA tH0uKD-vNwMoEc3Xk3Cbdg UYcmGbelzRa0Q6JqzLoguw C2C0GPKvzWWnP57Os9eQ0w n86B7IkbU20AkxlFX_5aew JaqcCU3nxReTW2cBLHounA kmE8w5Y785eZmodsx0V6Ag 8DEyKVyplnOcSKx39vatbg N3oNEwh0qgPqPP3Em6wJXw YMgZqBUAddmFErxLtCfK_w 3nDUQBjKyVor5wV0reJChg eZZyuJDouIg4p-GYB3PV_A qewG3X2O4X6JKskxyyqFwQ y3FcL4bLy0eLlkb0SDPnBQ TdYKJgSgY2GF_YJnwsi5yQ oeAhRa8yFa9jtrhaHnOyxQ 3nIuSCZk5f_2WWYMLN7h3w 8OeTLey-p-WaL9ErNEci1Q PKEzKWv_FktMm2mGPjwd0Q U4INQZOPSUaj8hMjLlZ3KA bLbSNkLggFnqwNNzzq-Ijw UYcmGbelzRa0Q6JqzLoguw tH0uKD-vNwMoEc3Xk3Cbdg kmE8w5Y785eZmodsx0V6Ag C2C0GPKvzWWnP57Os9eQ0w YMgZqBUAddmFErxLtCfK_w n86B7IkbU20AkxlFX_5aew JaqcCU3nxReTW2cBLHounA 8DEyKVyplnOcSKx39vatbg d_TBs6J3twMy9GChqUEXkg 3nDUQBjKyVor5wV0reJChg F_5_UNX-wrAFCXuAkBZRDw eZZyuJDouIg4p-GYB3PV_A N3oNEwh0qgPqPP3Em6wJXw Ryxj0u0AW3mRsRypdYli2A DeVGAiOf2mHVUDfxvuhVlQ QJI9OSEn6ujRCtrX06vs1w qewG3X2O4X6JKskxyyqFwQ"
businesses = "X4JNXUYY8wbaaDmk3BPzlWw iCQpiavjjPzJ5_3gPD5Ebg K7lWdNUhCbcnEvI0NhGewg RESDUcs7fIiihp38.d6_6g DkYS3arLOhA8si5uUEmHOw X5LNZ67Yw9RD6nf4_UhXOjw P7pxQFqr7yBKMMI2J51udw rcaPajgKOJC2vo_l3xa42A ujHiaprwCQ5ewziu0Vi9rw X2weQS.RnoOBhb1KsHKyoSQ eoHdUeQDNgQ6WYEnP2aiRw El4FC8jcawUVgw_0EIcbaQ Wxxvi3LZbHNIDwJ.ZimtnA cYwJA2A6I12KNkm2rtXd5g Cni2l.VKG_pdospJ6xliXQ f4x1YBxkLrZg652xt2KR5g KskYqH1Bi7Z_61pH6Om8pg eAc9Vd6loOgRQolMXQt6FA NCFwm2.TDb.oBQ2medmYDg pSQFynH1VxkfSmehRXlZWw X4JNXUYY8wbaaDmk3BPzlWw P7pxQFqr7yBKMMI2J51udw DkYS3arLOhA8si5uUEmHOw iCQpiavjjPzJ5_3gPD5Ebg cYwJA2A6I12KNkm2rtXd5g ujHiaprwCQ5ewziu0Vi9rw X5LNZ67Yw9RD6nf4_UhXOjw K7lWdNUhCbcnEvI0NhGewg El4FC8jcawUVgw_0EIcbaQ RESDUcs7fIiihp38.d6_6g eoHdUeQDNgQ6WYEnP2aiRw f4x1YBxkLrZg652xt2KR5g rcaPajgKOJC2vo_l3xa42A Wxxvi3LZbHNIDwJ.ZimtnA X2weQS.RnoOBhb1KsHKyoSQ NCFwm2.TDb.oBQ2medmYDg AV6weBrZFFBfRGCbcRGO4g UUGoM4q4i8rK2CBRS0xDAw KskYqH1Bi7Z_61pH6Om8pg Cni2l.VKG_pdospJ6xliXQ K7lWdNUhCbcnEvI0NhGewg DkYS3arLOhA8si5uUEmHOw X4JNXUYY8wbaaDmk3BPzlWw RESDUcs7fIiihp38.d6_6g iCQpiavjjPzJ5_3gPD5Ebg X5LNZ67Yw9RD6nf4_UhXOjw X2weQS.RnoOBhb1KsHKyoSQ P7pxQFqr7yBKMMI2J51udw eoHdUeQDNgQ6WYEnP2aiRw Wxxvi3LZbHNIDwJ.ZimtnA rcaPajgKOJC2vo_l3xa42A ujHiaprwCQ5ewziu0Vi9rw El4FC8jcawUVgw_0EIcbaQ cYwJA2A6I12KNkm2rtXd5g NvKNe9DnQavC9GstglcBJQ uGupeWqih0yIcCg8anM1PA QJatAcxYgK1Zp9BRZMAx7g KskYqH1Bi7Z_61pH6Om8pg Cni2l.VKG_pdospJ6xliXQ LNGBEEelQx4zbfWnlc66cw X4JNXUYY8wbaaDmk3BPzlWw K7lWdNUhCbcnEvI0NhGewg RESDUcs7fIiihp38.d6_6g DkYS3arLOhA8si5uUEmHOw iCQpiavjjPzJ5_3gPD5Ebg X5LNZ67Yw9RD6nf4_UhXOjw P7pxQFqr7yBKMMI2J51udw X2weQS.RnoOBhb1KsHKyoSQ eoHdUeQDNgQ6WYEnP2aiRw rcaPajgKOJC2vo_l3xa42A Wxxvi3LZbHNIDwJ.ZimtnA ujHiaprwCQ5ewziu0Vi9rw El4FC8jcawUVgw_0EIcbaQ cYwJA2A6I12KNkm2rtXd5g Cni2l.VKG_pdospJ6xliXQ KskYqH1Bi7Z_61pH6Om8pg QJatAcxYgK1Zp9BRZMAx7g LNGBEEelQx4zbfWnlc66cw uGupeWqih0yIcCg8anM1PA NvKNe9DnQavC9GstglcBJQ"

user_set = set()
business_set = set()
for user in users.split(" "):
    if user not in user_set:
        user_set.add(user)

for business in businesses.split(" "):
    if business not in business_set:
        business_set.add(business)

#business_file = open(MAIN_DIR+"business_matrix.txt", "w")

data = {}
item = "review"
file = item + ".json"
print("working on ", file)

# open the input file and read in lines
f = open(MAIN_DIR + file , "r")
lines = f.readlines()

# figure out which attributes to keep using the attributes dict
for line in lines:
    # read in as json
    # filter out to get only the attributes we want
    l = json.loads(line)
    txt = l["text"].replace('\n', ' ')
    label = l["stars"]
    if l["business_id"] not in data.keys():
        data[l["business_id"]] = {"text":[], "label":[]}
    data[l["business_id"]].append(txt)
    data[l["business_id"]]["label"].append(label)

    if l["user_id"] not in data.keys():
        data[l["user_id"]] = {"text":[], "label":[]}
    data[l["user_id"]]["text"].append(txt)
    data[l["user_id"]]["text"].append(label)

user_output = open(MAIN_DIR+"top_user_reviews.txt", "w")
business_output = open(MAIN_DIR+"top_business_reviews.txt", "w")

# go through reviews and find the ones that go with all of the top restaurants
count = 0 
for business in business_set:
    # find all reviews for this business
    reviews = []
    if business in data.keys():
        reviews = data[business]
    for review in reviews:
        business_output.write(count+"__"+review + "\n")
        count+=1

print("num reviews business: ", count)
# go through reviews and find the ones that go with all of the top users

count = 0
for user in user_set:
    # find all reviews for this user
    reviews = []
    if user in data.keys():
        reviews = data[user]
    for review in reviews:
        user_output.write(review + "\n")
        count+=1
        
print("num reviews user: ", count)
