'''
Date: 2020-11-01
Author: Vitali Lupusor

Description: This is a practical test for the Senior Data Engineer position 
    with TimeOut. All the requirements are presented below.

    The Problem
    The Time Out team loves to socialise, some of us are also really fussy! 
    In order to spend less time deciding where to go we’d like a program that 
    decides for us. All members of the team will want both food and drink so 
    if a member of staff cannot eat anything, or no drinks are served that 
    they like, the team will not visit the venue.

    The Input
    There are two JSON feeds, one of which is a list of the team members with 
    what they do drink and do not eat, the other feed contains venues with 
    the food and drink options for that venue.
    The person using the app needs to be able to enter which team members 
    will be attending.

    The Output
    The output should return which places are safe to go to, and if applicable 
    why the team should avoid the other places.
'''

def main():
    '''TODO: Add description.
    '''

    # Import internal modules
    from support_functions import scrap_json
    from support_functions import user_prompt

    # Read in the input data
    users = scrap_json(
        (
            'https://gist.githubusercontent.com/benjambles/'
            'ea36b76bc5d8ff09a51def54f6ebd0cb/raw/'
            'ee1d0c16eaf373cccadd3d5604a1e0ea307b2ca0/users.json'
        )
    )
    venues = scrap_json(
        (
            'https://gist.githubusercontent.com/benjambles/'
            'ea36b76bc5d8ff09a51def54f6ebd0cb/raw/'
            'ee1d0c16eaf373cccadd3d5604a1e0ea307b2ca0/venues.json'
        )
    )

    # Prompt for a list of attendees
    attendees = user_prompt(users=users)

    if not attendees:
        return (
            'Nobody is going anywhere, since you have not '
            'specified any member of the team!'
        )

    # Filter out the users that won't attend
    attending_users = {
        user['name']: {
            'wont_eat': [food.lower() for food in user['wont_eat']],
            'drinks': [drink.lower() for drink in user['drinks']]
        } for user in users \
            if user['name'] in attendees
    }

    # Create the output
    output = {
        'places_to_visit': [],
        'places_to_avoid': {}
    }
    for attendee, preferences in attending_users.items():
        for venue in venues:
            would_eat = [
                food.lower() for food in venue['food'] \
                    if food.lower() not in preferences['wont_eat']
            ]
            would_drink = [
                drink for drink in preferences['drinks'] \
                    if drink in [drink.lower() for drink in venue['drinks']]
            ]
            if not would_eat:
                if venue['name'] not in output['places_to_avoid'].keys():
                    output['places_to_avoid'][venue['name']] = [
                        f'There is nothing for {attendee} to eat.'
                    ]
                else:
                    output['places_to_avoid'][venue['name']].append(
                        f'There is nothing for {attendee} to eat.'
                    )
            if not would_drink:
                if venue['name'] not in output['places_to_avoid'].keys():
                    output['places_to_avoid'][venue['name']] = [
                        f'There is nothing for {attendee} to drink.'
                    ]
                else:
                    output['places_to_avoid'][venue['name']].append(
                        f'There is nothing for {attendee} to drink.'
                    )

    output['places_to_visit'] = [
        venue['name'] for venue in venues \
            if venue['name'] not in output['places_to_avoid'].keys()
    ]
    output['places_to_avoid'] = [
        {
            'name': name,
            'reason': reason
        } for name, reason in output['places_to_avoid'].items()
    ]

    return output
