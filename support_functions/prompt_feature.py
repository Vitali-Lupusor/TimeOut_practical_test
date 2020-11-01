'''
Date: 2020-11-01
Author: Vitali Lupusor

Description: Unit test for the "prompt" feature.
'''

def user_prompt():
    '''TODO: 

    Arguments:
        arg (): TODO

    return (): TODO
    '''

    # Import external modules
    _re = __import__('re', fromlist=['search', 'sub'])
    search = _re.search
    sub = _re.sub

    # Prompt for a list of attendees
    attendees = []
    prompt = input(
        (
            'Please provide the names of the attendees in a '
            'singular order:\n'
        )
    ).strip()

    while True:
        if search(r'^[a-zA-Z]+\s+[a-zA-Z]+', prompt):
            prompt = sub(
                    r'\s{2,}', ' ', prompt.title()
                )
            if prompt in [user['name'] for user in users]:
                attendees.append(prompt)
            else:
                prompt = input(
                    (
                        'The name provided does not match any of the existing '
                        'users. Please try again.\n'
                        'If you want to exit the prompt, type in "stop".\n'
                    )
                )
                continue

            prompt = input(
                (
                    'Is anybody else attending? If so, input their First '
                    'and Last names below.\n'
                )
            )
        else:
            if prompt.strip().lower() in ['stop', 'n', 'no']:
                break
            else:
                prompt = input(
                    (
                        'The input values should be alphabetical with a space '
                        'separating the First and Last names.\n'
                        'If you want to exit the prompt, print "stop", '
                        'alternatively, re-enter the values.\n'
                    )
                )

    return attendees

if __name__ == '__main__':
    users = [
        {
            'name': 'Danielle Ren',
            'wont_eat': [
                'Fish'
            ],
            'drinks': [
                'Cider', 'Rum', 'Soft drinks'
            ]
        },
        {
            'name': 'Cristiana Lusitano',
            'wont_eat': [
                'Eggs', 'Pasta'
            ],
            'drinks': [
                'Tequila', 'Soft drinks', 'beer', 'Coffee'
            ]
        },
        {
            'name': 'Karol Drewno',
            'wont_eat': [
                'Bread', 'Pasta'
            ],
            'drinks': [
                'Vodka', 'Gin', 'Whisky', 'Rum'
            ]
        },
        {
            'name': 'Gaston Chambray',
            'wont_eat': [],
            'drinks': [
                'Cider', 'Beer', 'Rum', 'Soft drinks'
            ]
        },
        {
            'name': 'Tom Mullen',
            'wont_eat': [
                'Meat', 'Fish'
            ],
            'drinks': [
                'Soft drinks', 'Tea'
            ]
        },
        {
            'name': 'Rosie Curran',
            'wont_eat': [
                'Mexican'
            ],
            'drinks': [
                'Vodka', 'Gin', 'whisky', 'Rum', 'Cider', 'Beer', 'Soft drinks'
            ]
        },
        {
            'name': 'Wen Li',
            'wont_eat': [
                'Chinese'
            ],
            'drinks': [
                'Beer', 'cider', 'Rum'
            ]
        }
    ]

    attendees = user_prompt()

    print(attendees)
