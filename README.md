# howamun-api

ほわむんボタンの押された数（いいね数）を管理

https://howamunsample-1-f1414439.deta.app/docs


## Needed

- `ACCESS_TOKEN`: deta.space access token
- `PROJECT_ID`: deta.space project id

## endpoints

- `/v1/get/{key}`: get like count by key
- `/v1/create/{key}`: create like count by key
  - `likes (int)`: initial like count (default: 0)
- `/v1/increment/{key}`: update like count by key
  - `num_increment (int)`: increment number (default: 1)