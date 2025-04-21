import os

import httpx


class SSPANELCheckin:
    def __init__(self):
        self.email = os.environ.get('EMAIL')
        self.passwd = os.environ.get('PASSWD')
        self.server_key = os.environ.get('SERVER_KEY')
        self.domain = os.environ.get('DOMAIN')
        self.headers = {
            'origin'    : 'https://ikuuu.one',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }

    def checkin(self):
        with httpx.Client(headers=self.headers) as client:
            data = {'email': self.email, 'passwd': self.passwd}
            resp = client.post(f'{self.domain}/auth/login', data=data).json()
            print(resp['msg'])
            resp = client.post(f'{self.domain}/user/checkin').json()
            print(resp['msg'])
            client.post(f'https://sctapi.ftqq.com/{self.server_key}.send?title=iKuuu签到-{resp["msg"]}')


if __name__ == '__main__':
    ssp = SSPANELCheckin()
    ssp.checkin()
