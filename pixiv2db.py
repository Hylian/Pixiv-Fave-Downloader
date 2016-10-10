from pixivpy3 import *
import json

api = PixivAPI()
with open('config.json', 'r') as f:
  config = json.load(f)

last_fave_id = int(config['last_fave_id'])

api.login(config['username'], config['password'])

json_result = api.me_favorite_works()
my_ids = json_result.response

for my_id in my_ids:
  if (my_id.work.favorite_id >= last_fave_id):
    print("End of new faves")
    break
  api.download(my_id.work.image_urls['large'])
  print('Downloaded 'my_id.work.favorite_id)

config['last_fave_id'] = str(my_ids[0].work.favorite_id)
print("last_fave_id:" + config['last_fave_id'])

with open('config.json', 'w') as f:
  json.dump(config, f)
