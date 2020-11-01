'''
Date: 2020-11-01
Author: Vitali Lupusor

Description: TODO
'''

def scrap_json(url):
    '''Send a request to the provided URL in order to retrive the 
    names of the users, their preferences as well as the venues and 
    their simplified menue.

    Arguments:
        url (str): URL where the data is hosted.

    return (list): Read into a list the file linked to the URL address.
    '''

    # Import extenal modules
    json = __import__('json')
    _requests = __import__('requests', fromlist=['get'])
    get = _requests.get

    with get(url) as payload:
        file = json.loads(payload.text)

    return file

if __name__ == '__main__':
    test_url = (
        'https://gist.githubusercontent.com/benjambles/'
        'ea36b76bc5d8ff09a51def54f6ebd0cb/raw/'
        'ee1d0c16eaf373cccadd3d5604a1e0ea307b2ca0/users.json'
    )

    test_web_scrap = scrap_json(url=test_url)

    print(test_web_scrap)
