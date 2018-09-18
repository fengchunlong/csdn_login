import requests
from bs4 import BeautifulSoup


def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'passport.csdn.net',
        'Referer': 'https://www.csdn.net/'
    }

def write_html(text, filename):
    """
    将返回的响应信息写入文件
    :param text: 响应页面内容
    :param filename:   保存的文件名
    :return:
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


login_url = "https://passport.csdn.net/account/login"        # csdn登入的url
login_verify = "https://passport.csdn.net/account/verify"
my_url = "https://my.csdn.net/my/mycsdn"


if __name__ == '__main__':
    # 通过requests的session请求
    seesion = requests.session()
    # 通过get请求登录页面的url，获取响应数据
    response = seesion.get(login_url, headers=get_headers())
    print(response.headers)
    # 输出响应码
    print(response.status_code)
    # 将返回的html写入文件
    write_html(response.text, 'get_login.html')

    # 使用BeautifulSoup解析html，使用lxml的方式解析
    soup = BeautifulSoup(response.text, 'lxml')
    # 获取登入页面的input标签中lt的值，后面post表单上传登入信息需要
    lt = soup.select('input[name="lt"]')[0]['value']
    # 获取登入页面的input标签中execution的值，后面post表单上传登入信息需要
    execution = soup.select('input[name="execution"]')[0]['value']

    fkid = soup.select('input[name="fkid"]')[0]['value']
    # 上传表单的data数据
    data = {
        "gps": '',
        "username": "694798056@qq.com",
        "password": "andy0510csdn",
        "lt": lt,
        "execution": execution,
        "_eventId": "submit",
        "rememberMe": "true",
        "fkid": fkid
    }

    # 打印data数据
    print(data)
    exit()

    # post请求上传data数据，模拟登入，获取响应结果
    # headers = response.headers
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,la;q=0.7,ja;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '467',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'TY_SESSION_ID=3775049b-aac8-4fcf-94e8-337c5c664494; fkid=WHJMrwNw1k/HzTA7IvIcrTpfGOeUt/AE3UtN9XUbq9ECVLfka25tkEchZGkYpGcbdWMACtLuOF/82R+Oa4wPMI7qT/5eBtVi0VkyjTP+1Nh8Tv06okQ1koYaHMOKM8qKVBJ7HANruhDjgssVEtOEyiJGebD4P9188Eyaxs83iOILDXDzGiHC8rLbK0zioAzrAzbQCr3JAl5/8vDnphun9XPGLYz537MAUPTYnEGPssl82kNF0emrW7C4Vc2T0mj05SBMZJRjFRB4%3D1487582755342; uuid_tt_dd=10_6108502880-1536633263442-187087; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; smidV2=201809130912479e444de078ebc4901d55ac0f66b4754000861df29d8c89d80; UN=fengchunlong11; dc_session_id=10_1537241482686.509274; csdn_edu_5599_course=5599; JSESSIONID=9E8935C1539D6D1B4FEA111D8131FFCE.tomcat2; __yadk_uid=SDpuebkPOFFr0fe3ciLqaE6kXja0Wv8u; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1537166307,1537166585,1537241484,1537252750; BT=1537254036485; LSSC=LSSC-3270540-1BUgINV9yfgfx2S747z1bR3TZWurDU-passport.csdn.net; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1537255822; dc_tos=pf8q6m; fkid=WHJMrwNw1k/HzTA7IvIcrTpfGOeUt/AE3UtN9XUbq9ECVLfka25tkEchZGkYpGcbdWMACtLuOF/82R+Oa4wPMI7qT/5eBtVi0VefhO7/XF4dgM8/2KBWqKoYHqxuZPWulBJ7HANruhDjgssVEtOEyiJGebD4P9188Eyaxs83iOILDXDzGiHC8rLbK0zioAzrAzbQCr3JAl5/8vDnphun9XC5obfU8el4FHvlk7tJMJ0jcLjlxvuKHBUNguZ28MSymF10/rPYNoNw%3D1487582755342',
        'Host': 'passport.csdn.net',
        'Origin': 'https://passport.csdn.net',
        'Referer': 'https://passport.csdn.net/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response = seesion.post(login_verify, data=data, headers=headers,allow_redirects=False)
    # # 打印响应的状态码
    print(response.status_code)
    print(response.headers['Location'])
    print(response.headers)
    # # 将响应的信息写入文件
    write_html(response.text, 'login_success.html')
    #
    # # 通过get请求，请求个人主页，如果没有登入成功，则会返回登页，登入成功，则会获取到登入的个人信息
    # response = seesion.get('https://my.csdn.net/my/mycsdn', headers=get_headers(),allow_redirects=False)
    # # # 打印响应码
    # print(response.status_code)
    # # # 将响应结果保存文件
    # write_html(response.text,'my.html')