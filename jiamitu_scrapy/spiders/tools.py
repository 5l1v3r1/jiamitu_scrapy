# coding:utf-8
class TransCookie:
    def __init__(self,cookie):
        self.cookie = cookie

    def string2dict(self):
        item_dict = {}
        items = self.cookie.split(";")
        for item in items:
            key = item.split('=')[0].replace(' ', '')
            value = item.split('=')[1]
            item_dict[key] = value
        return item_dict
