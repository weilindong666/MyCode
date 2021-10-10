# -*- coding:utf-8 -*-
"""
    @Time : 2021/9/13 19:59
    @Author: Wei Lindong
    @File: ReferTools.py
    @Software: PyCharm
"""
import requests
import time
import random
import hashlib
import os
import pygame



class ReferTools(object):
    def __init__(self):
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
            'Referer': 'https://fanyi.youdao.com/?keyfrom=dict2.top',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=1777436480@123.136.117.175; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abct6Jjis5gxL8SUBXwWx; OUTFOX_SEARCH_USER_ID_NCOO=1993779311.779159; _ntes_nnid=ef99c9d2e6a1445dcb81a846ad8d6804,1632469650618; ___rl__test__cookies=1632471359200'
        }
        self.song = os.getcwd() + '/temp/'


    def md5(self, i):
        # 创建MD5对象
        md5 = hashlib.md5()
        # 加密字符串
        md5.update(bytes(i, encoding="utf-8"))
        # 返回16位的加密
        return md5.hexdigest()

    def refer(self, word):
        url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        lts = str(int(time.time() * 1000))
        salt = lts + str(random.randint(0, 9))
        sign = str(self.md5("fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"))
        param = {
            'i': str(word),
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'lts': lts,
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }

        response = requests.post(url, params=param, headers=self.header)
        response.encoding = 'utf-8'
        dict_ = response.json()
        result = dict_['translateResult'][0][0]['tgt']
        return result

    def downLoadAudio(self, word):
        url = f'https://tts.youdao.com/fanyivoice?word={word}&le=eng&keyfrom=speaker-target'
        response = requests.get(url, headers=self.header)
        try:
            with open(self.song + word + '.m4a', 'wb') as f:
                f.write(response.content)
                f.close()
        except Exception:
            pass


    def downLoadAndRead(self, word):
        self.downLoadAudio(word)
        self.read(word)

    def read(self, word):
        pygame.mixer.init()
        try:
            pygame.mixer.music.load(self.song + word + '.m4a')
        except Exception:
            return
        pygame.mixer.music.play(1)
        time.sleep(2)
        pygame.mixer.music.stop()


if __name__ == '__main__':
    tool = ReferTools()
    tool.downLoadAudio('ball')
    tool.read('ball')