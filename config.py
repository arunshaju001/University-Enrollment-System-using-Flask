import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or b'\xee\x7f:\xa1\xe6\x95m\xf4\x97A\x98r\xa5\x14I\xfa'

    MONGODB_SETTINGS = {'db' : 'UTA_Enrollment' }