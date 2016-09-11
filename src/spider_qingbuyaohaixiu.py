import re
import urllib
#import time

url_page_mode = 'http://qingbuyaohaixiu.com/page/%d'
arch_reg = r'\<h1 class="entry\-title"\>\<a href="http\:\/\/qingbuyaohaixiu\.com\/archives\/[1-9]\d*'
arch_name = r'\<meta property="og:title" content=".*" \/\>'
arch_time = r'datetime=.{20}'
img_url1 = r'http\:\/\/qingbuyaohaixiu\.com\/.*\.jpg'
img_url2 = r'http\:\/\/qingbuyaohaixiu\.com\/.*\.png'
img_url3 = r'http\:\/\/qingbuyaohaixiu\.com\/.*\.jpeg'

img_mode = ['jpg', 'png', 'jpeg']
img_index = '-150x150'
img_url_re1 = re.compile(img_url1)
img_url_re2 = re.compile(img_url2)
img_url_re3 = re.compile(img_url3)

i = 1
while True:
#open ervery page url
    curr_page_url = url_page_mode % i
    print "============================================================================="+curr_page_url
    page = urllib.urlopen(curr_page_url)
    html = page.read()
    page.close()

    img_re = re.compile(arch_reg)
    img_list = img_re.findall(html)
    for i_list in img_list:
#get archives real url
        print i_list
        i_list = i_list[i_list.index('http'):]
        print i_list

#open archives real url
        page = urllib.urlopen(i_list)
        html = page.read()
        page.close()

#get img name
        img_re = re.compile(arch_name)
        img_list = img_re.findall(html)
        sub_i_list = img_list[0]
        print sub_i_list.decode("utf-8")
        sub_i_list = sub_i_list[sub_i_list.index('content="')+9:-4]
        print sub_i_list.decode("utf-8")

#get img datetime
        time_re = re.compile(arch_time)
        i_time = time_re.findall(html)
        print i_time
        sub_i_time = i_time[0]
        print sub_i_time
        sub_i_time = sub_i_time[sub_i_time.index('datetime="')+10:]
        sub_i_time = sub_i_time.replace(':', '-')
        print sub_i_time

#get img url
        i_img_url = img_url_re1.findall(html)
        if ( (len(i_img_url) > 0) and (i_img_url[0].find("-150x150") < 0) ):
            real_img_url = i_img_url[0]
            sufix = '.jpg'
        i_img_url = img_url_re2.findall(html)
        if ( (len(i_img_url) > 0) and (i_img_url[0].find("-150x150") < 0) ):
            real_img_url = i_img_url[0]
            sufix = '.png'
        i_img_url = img_url_re3.findall(html)
        if ( (len(i_img_url) > 0) and (i_img_url[0].find("-150x150") < 0) ):
            real_img_url = i_img_url[0]
            sufix = '.jpeg'
        print real_img_url 

        img_name_all = sub_i_time + '_' + sub_i_list + '_' + i_list[36:] + sufix
        print img_name_all.decode("utf-8")

        urllib.urlretrieve(real_img_url, img_name_all.decode("UTF-8"))
        #urllib.urlretrieve(real_img_url, img_name_all)

        #time.sleep(5)


    #time.sleep(20)
    i = i+1
    
