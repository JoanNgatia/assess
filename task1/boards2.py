# Create class data models that synchronise with Trello’s API for
# creating lists and cards within the lists.
# Create a List class with the following methods
# - create(), edit() and delete().
# Create a Card class with the following methods
# - create(), edit() and delete().
# Create a function in the List class, void addCard(Card card), for adding
# cards to the list.

import requests

ACCESS_KEY = 'da15af8c50eed328c49a1a416074463a'


class List(object):
    """Class model to create ,edit and delete board lists."""

    def create(self, board_id, name):
        """Create a list on a board."""
        url_to_lists = 'https://api.trello.com/1/boards/' + self.board_id
        + '/lists'
        payload = {'key': 'da15af8c50eed328c49a1a416074463a'}
        response = requests.post(url_to_lists, params=payload,
                                 data=self.name)
        return response.data

    def edit(self, board_id, name):
        """Edit a board's list."""
        url_to_lists = 'https://api.trello.com/1/boards/' + self.board_id
        + '/lists'
        payload = {'key': 'da15af8c50eed328c49a1a416074463a'}
        response = requests.put(url_to_lists, params=payload,
                                data=self.name)
        return response.data

    def delete(self, board_id):
        """Edit a board's list."""
        url_to_lists = 'https://api.trello.com/1/boards/' + self.board_id
        + '/lists'
        payload = {'key': 'da15af8c50eed328c49a1a416074463a'}
        response = requests.delete(url_to_lists, params=payload)
        return response.data
