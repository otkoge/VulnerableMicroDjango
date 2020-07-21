import requests
import sys


r = requests.get('https://ifconfig.me')
TARGET = f'http://{r.text}:8000'




def authenticate_session(session, username, password):
    session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
    login_url = f'{TARGET}/login?next=/'
    response = session.get(login_url)
    csrf_token = ''
    for line in response.text.split('\n'):
        if "csrfmiddlewaretoken" in line:
            csrf_token = line.split('value="')[1].split('"')[0]
    response = session.post(login_url, data={'username': username, 'password': password, 'csrfmiddlewaretoken': csrf_token})
    if not response.history:
        return False
    return True

def crawl(session):
    pages_to_visit = ['/',
                      '/containers',
                      '/images',
                      '/ifconfig',
                      '/route',
                      '/ping',
                      '/ping?ip=1.1.1.1o']
    for page in pages_to_visit:
        url = f'{TARGET}{page}'
        r = session.get(url)

def do_test(username, password):
    for i in range(20):
        print(f"Creating session {i}...")
        session = requests.Session()
        authenticate_session(session, username, password)
        crawl(session)

if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
    except IndexError:
        sys.exit(-1)
    do_test(username, password)
    print("Application has been crawled.")
