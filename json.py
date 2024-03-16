# results = {"request":"afdasfasf-qwerqwr-qwerqwer-qwerqwre"}
# print(results['request'])

# results = {"color":{"dominantColorForeground":"White", "dominantColorBackground":"White", "accentColor":["white"]}}
# print(results['color']['dominantColorForeground'])

# results = {"description":{"tag":{"bear","polar","animal","outdoor","water","white","walking","snow","standing"}}}
# print(results['description']['tags'][0])

results = {"description":{"tags":["bear","polar","animal","mammal","outdoor","water","white","large","walking","snow"],"captions":[{"text":"a large white polar bear walking in the water","confidence":0.7446564664}]}}

for item in results['description']['tags']:
    print(item)