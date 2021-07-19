import requests
import re
import os
import csv
import time
def string_clean(a):#Tiktok: special characters in the jitter text
    m=''
    f1=open('special.csv','w')
    wf=csv.writer(f1)
    for i in list(a):
        try:
            if i=='\n' or i=='\\' or i=='n'or i=='/':
                continue
            wf.writerow([i])
            m=m+i
        except UnicodeEncodeError:
            continue
    f1.close()
    return m
timeArray = int(time.time())
#print(timeArray)
timeArray=time.localtime(timeArray)
Time = time.strftime("%Y-%m-%d-%H-%M-%S", timeArray)
print(Time)
f=open(str(Time)+'.csv','w',newline='')
wf=csv.writer(f)
wf.writerow(['author_id','author_name','author_signature','author_diggCount','author_followerCount','author_followingCount','author_heartCount','author_videoCount','video_url','video_id','video_desc','video_commentCount','video_diggCount','video_playCount','video_shareCount'])
videoidlist=[]
for i in range(1,100):
    url = 'https://m.tiktok.com/api/recommend/item_list/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6980332468541769218&region=US&priority_region=&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.124+Safari%2F537.36+Edg%2F91.0.864.70&browser_online=true&verifyFp=verify_kr7zfk4t_Ljx86FrK_SaBL_4yz1_Aoim_O837PyspIDMy&app_language=en&timezone_name=Asia%2FShanghai&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=5&battery_info=1&count=30&itemID=1&language=en&from_page=fyp&insertedItemID=&_signature=_02B4Z6wo00f01-fM-awAAIDAVz0VZJGucQvnzP0AAJkQ3b'
    # url='https://m.tiktok.com/api/recommend/item_list/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6980332468541769218&region=US&priority_region=&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Chrome%2F91.0.4472.124+Safari%2F537.36+Edg%2F91.0.864.70&browser_online=true&verifyFp=verify_kr7zfk4t_Ljx86FrK_SaBL_4yz1_Aoim_O837PyspIDMy&app_language=en&timezone_name=Asia%2FShanghai&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=4&battery_info=0.94&count=30&itemID=1&language=en&from_page=fyp&insertedItemID=&_signature=_02B4Z6wo00f018ghmGAAAIDAeNB0q4cPZbfIIZzAAJMEa3'
    headers = {
        'upgrade-insecure-requests': '1',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="91", "Chromium";v="91"',
        'cookie':'tt_webid_v2=6980332468541769218; tt_webid=6980332468541769218; _abck=ED0A47101D299D43655EA43F587599B0~-1~YAAQB1lQaPDSXRl6AQAAJk/2iAY0txvRSX64Bb5hwBc/G5Z4PTPUvCGvfyMDXcKTaoEEJpWgaPnRnjPJaH9a07Pru8DMRP2+8hOR2kNEUoFonEzYMB9YiaDc/SMzGxwr0sJudie2O6Tw08GbpKocs3P4484d3npzUWIEA7Vf9HIaDra29tathzp4kIB/+2j8VtgSpzhCKdLoyfM3KjG9CLJqfV32amjE1Vlro/7gqgKAHn6Bpt93eLhsCCfJVpDDvmdaHuoUiHn9Hmi3ybw+llOzvFc3cesGCgRZYsiNezMF91nX7jEg8MsyT5pJwkz1592BhLmKNLE8ZNAGrPHh/XNVxeNwXocws1G81TKzynGKpgepEHOVM+I/8+GrOmeVxPL3FppL18vx6p4=~-1~-1~-1; tt_csrf_token=Pyy66AVv8_xfVHzsFsv1ll8q; csrf_session_id=c8c22a8dddd641aa8f4f874d68c8d066; R6kq3TV7=ANkNvbl6AQAAeDLJZWWoWRCDTtT2fDfGDuZk37BeEKqHlZVlqojprfm5M4J2|1|0|f22adb0c81e53a085d061ea8729132ab02f61f27; ttwid=1%7CKSoqQpL3ypWMZfRHXmf8VafcT8jvK3-_erv_JfaoJ6Q%7C1626617465%7Cecd1d687071f11ca1c057cea0940f45ce104f9c4a68a8a72793e93415047d88f',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70'}
    response = requests.get(url=url, headers=headers, verify=False).json()['itemList']
    print(len(response))
    for i in response:
        print(i)
        video_commentCount = i['stats']['commentCount']
        video_diggCount = i['stats']['diggCount']
        video_playCount=i['stats']['playCount']
        video_shareCount=i['stats']['shareCount']
        video_id = i['id']
        if video_id in videoidlist:
            continue
        videoidlist.append(video_id)
        video_desc=string_clean(i['desc'])
        author_id=i['author']['id']
        author_name=i['author']['nickname']
        author_name=string_clean(author_name)
        author_diggCount=i['authorStats']['diggCount']
        author_signature=string_clean(i['author']['signature'])
        author_followerCount=i['authorStats']['followerCount']
        author_followingCount=i['authorStats']['followingCount']
        author_heartCount=i['authorStats']['heartCount']
        author_videoCount=i['authorStats']['videoCount']
        video_url='https://www.tiktok.com/@steph_and_joey/video/'+str(id)+'?lang=en&is_copy_url=1&is_from_webapp=v1'
        print([author_id,author_name,author_signature,author_diggCount,author_followerCount,author_followingCount,author_heartCount,author_videoCount,video_url,video_id,video_desc,video_commentCount,video_diggCount,video_playCount,video_shareCount])
        wf.writerow([author_id,author_name,author_signature,author_diggCount,author_followerCount,author_followingCount,author_heartCount,author_videoCount,video_url,video_id,video_desc,video_commentCount,video_diggCount,video_playCount,video_shareCount])
