import requests
# import json

ACCESS_KEY = 'da15af8c50eed328c49a1a416074463a'


def get_checklists():
    board_id = raw_input('Which board do you want to copy from?')
    payload = {'key': 'da15af8c50eed328c49a1a416074463a'}
    url_to_checklists = 'https://api.trello.com/1/boards/' + board_id + '/checklists'
    checklist_data = requests.get(url_to_checklists, data=payload)
    url_to_lists = 'https://api.trello.com/1/boards/' + board_id + '/lists'
    post_data = {'data': checklist_data}
    paster = requests.post(url_to_lists, params=payload,
                           data=post_data)
    return paster

get_checklists()
