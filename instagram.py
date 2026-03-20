# Created by Gwan Woo Kim
# Python script taking in the follower and following json files from instagram export.
# Adds respective users to a set and compares the two to see who doesn't follow you back

import json

with open('following.json', 'r') as file:
    followingData = json.load(file)

with open('followers_1.json', 'r') as file:
    followerData = json.load(file)


# Just debugging/understanding how the json file works
# print(json.dumps(followerdata, indent=4))

following = {item["title"] for item in followingData["relationships_following"]}
follower = {item['string_list_data'][0]['value'] for item in followerData}

opps = set(following) - set(follower)

print(f"{len(opps)} people don't follow you back: ")
for user in sorted(opps):
    print(user)
