import gitlab
import urllib3
import json
import pprint
from config import get_config
urllib3.disable_warnings()

data = get_config()

def old_config_credentials():
    '''
    Credentials from old gitlab instance
    '''
    gl_old = gitlab.Gitlab(data["origin"]["gitlab_url"], private_token=data["origin"]["token"], ssl_verify=True)
    return gl_old

def new_config_credentials():
    '''
    Credentials from new gitlab instance
    '''
    gl_new = gitlab.Gitlab(data["destination"]["gitlab_url"], private_token=data["destination"]["token"], ssl_verify=True)
    return gl_new
