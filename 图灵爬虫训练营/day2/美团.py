import base64
import json
import time
import zlib
import requests


# 二进制解压
# data='eJx1j11vgjAYhf9LbyVSEKol8QIFHTqtU8SPZRdAoaADlA9Flv331cQl7mLJm5zT5z05efsFcosCTYIQQyiAS5ADDUht2EZAAGXBNwjJHYRVpHZkLAD/L1N6SABe7hhAe5dkpSfgLvq4kyUHT+TJygqfe8biERCV5anQRJE17SSIy8pN236WiNwXUSzyG/4JAN6Q2LyB6/Gh7kPL3/eM/4VXFDFLuQsm18+DLZPrQX+LAjxU6LQ25Zl1zApHWmc5YSq7DQbjMb4sg9dm5UdxxVymGGGox+SEgzQTh1Bkl2uQ1nOzCXVDDVu+UZEQ97ya1ju91hPJjsNmZBvrAyyuu1WJEn1fb6xoTMYLH1b2okkNOp9J6lEndpw1twSObLKXG7M7o+7ZnPgTVaryPUsbRM2Mns1W6L+IyfCcDkht3rZGC2GKqZthL3NOgcFIsi1g3HWGh1PpTXuLnamuNqj0dpK9Xd1kx7GKLVniCWH9Pvj+AatOmAo='
# def Token123(data):
#     token_encode = base64.b64decode(data.encode())
#     # 二进制解压
#     token_sting = zlib.decompress(token_encode).decode('utf-8')
#     print(token_sting) #  iP
#
#     sign = json.loads(token_sting)['sign']
#     Token123(sign) # 请求参数

# 二进制压缩
def decode_sign(token_string):
    # base编码
    encode1 = str(token_string).encode()
    # 参数 压缩成 特殊的编码 ->
    compress = zlib.compress(encode1)  # 二进制压缩
    b_encode = base64.b64encode(compress)
    # 转变 str
    e_sign = str(b_encode, encoding='utf-8')
    return e_sign


params = {
    "cityName": "广州",
    "cateId": "0",
    "areaId": "0",
    "sort": "",
    "dinnerCountAttrId": "",
    "page": "1",
    "userId": "279640882",
    "uuid": "304656507e314691be4f.1661244039.1.0.0",
    "platform": "1",
    "partner": "126",
    "originUrl": "https://gz.meituan.com/meishi/",
    "riskLevel": "1",
    "optimusCode": "10"
}

sign = decode_sign(params)

ip = {
    "rId": 100900,
    "ver": "1.0.6",
    "ts": round(time.time() * 1000),
    "cts": round(time.time() * 1000 + 2000),
    "brVD": [
        1248,
        976
    ],
    "brR": [
        [
            1248,
            976
        ],
        [
            1248,
            976
        ],
        24,
        24
    ],
    "bI": [
        "https://gz.meituan.com/meishi/",
        "https://gz.meituan.com/"
    ],
    "mT": [],
    "kT": [],
    "aT": [],
    "tT": [],
    "aM": "",
    "sign": sign
}

token = decode_sign(ip)
params['_token'] = token

# print(params)

url = 'https://gz.meituan.com/meishi/api/poi/getPoiList?'
headers = {
    'Cookie': 'uuid=304656507e314691be4f.1661244039.1.0.0; _lxsdk_cuid=182c9dc64d267-06ea926631b29a-45647f52-1fa400-182c9dc64d3ac; ci=20; mtcdn=K; iuuid=DC0CF9AD7922F5E2CC30363B8732829E97259EF2463C98559AF4A6862CE30DF7; _lxsdk=DC0CF9AD7922F5E2CC30363B8732829E97259EF2463C98559AF4A6862CE30DF7; _hc.v=a6d157c4-243e-4a0a-32d6-9ae74f21d2d1.1661935353; lat=23.29038; lng=113.83308; userTicket=dYcKyJIMyjubLCxYdEzqVvrhkBhUhXbwdOmdxBei; ci3=20; IJSESSIONID=node01nef6ak4bgnfa1uq07onzxmi1h173995584; cityname=%E5%B9%BF%E5%B7%9E; webp=1; i_extend=H__a100002__b1; __utma=74597006.1163298560.1662363627.1662363627.1662363627.1; __utmc=74597006; __utmz=74597006.1662363627.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; latlng=23.132618%2C113.409449; qruuid=3945bb25-6cce-4a90-a43f-38e7f00ba899; token=DlQrD_5yccYJh-nZaYCpyMyie7IAAAAA6xMAAJ6sxwIwpmNmfmfwGwp60qwZCWxXCH46hasF0weuC2_FCDdxs_8nmE_-gy7qwgtP3g; mt_c_token=DlQrD_5yccYJh-nZaYCpyMyie7IAAAAA6xMAAJ6sxwIwpmNmfmfwGwp60qwZCWxXCH46hasF0weuC2_FCDdxs_8nmE_-gy7qwgtP3g; oops=DlQrD_5yccYJh-nZaYCpyMyie7IAAAAA6xMAAJ6sxwIwpmNmfmfwGwp60qwZCWxXCH46hasF0weuC2_FCDdxs_8nmE_-gy7qwgtP3g; userId=279640882; token2=DlQrD_5yccYJh-nZaYCpyMyie7IAAAAA6xMAAJ6sxwIwpmNmfmfwGwp60qwZCWxXCH46hasF0weuC2_FCDdxs_8nmE_-gy7qwgtP3g; lt=DlQrD_5yccYJh-nZaYCpyMyie7IAAAAA6xMAAJ6sxwIwpmNmfmfwGwp60qwZCWxXCH46hasF0weuC2_FCDdxs_8nmE_-gy7qwgtP3g; u=279640882; n=wackyd; unc=wackyd; client-id=bb671b23-02b2-412e-87dc-c9faf02371f4; WEBDFPID=w362u467wvu0517yz0yv9z86wz22w8v58169xu76w5y97958y1x00y76-1662455946287-; __mta=145144459.1661933453261.1662445804851.1662445818637.12; firstTime=1662445864259; _lxsdk_s=183117ddb59-7bd-b9f-07d%7C%7C11',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'Referer': 'https://gz.meituan.com/meishi/'
}
response = requests.get(url, headers=headers, params=params).json()
print(response)
