import requests

ACCESS_KEY = 'da15af8c50eed328c49a1a416074463a'
# sample =
# 'https://api.trello.com/1/boards/4eea4ffc91e31d1746000046/checklists?key=[application_key]&token=[optional_auth_token]'


def get_checklists(board_id):
    # r = requests.get('https://api.github.com/events')
    payload = {'key': 'da15af8c50eed328c49a1a416074463a'}
    r = requests.get(
        'https://api.trello.com/1/boards/checklists', params=payload)
    import ipdb
    ipdb.set_trace()
    return r

print get_checklists(20)
