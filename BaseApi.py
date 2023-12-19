import yaml
import logging
import requests

with open('testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class ApiHelper():
    def autorization(self):
        try:
            result = requests.post(url=testdata['url'], data={'username': testdata['login'], 'password': testdata['password']})
            token = result.json()['token']
        except:
            logging.exception(f"Exception get {token}")
            return None
        logging.info(f"Token get successful")
        return token
    
    def check_post_id(self):
        try:
            res_get = requests.get(url=testdata['urlpost'], headers={"X-Auth-Token": self.autorization()}, params={"owner": "notMe"})
            posts = [item['id'] for item in res_get.json()['data']]
        except:
            logging.exception("Exceptio check posts")
            return None
        logging.info("List of posts created")
        return posts