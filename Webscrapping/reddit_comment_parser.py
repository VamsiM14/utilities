import requests

# Define the URL of the Reddit post
# 'https://www.reddit.com/r/Python/comments/abcdefg/my_post_title.json'
post_url = 'https://www.reddit.com/r/dataengineering/comments/11f8yxo/quarterly_salary_discussion/'

# Make an HTTP GET request to the Reddit API to fetch the post and its comments
response = requests.get(post_url, headers={
                        'User-agent': 'myBot/0.0.1 (contact info: xxxx@gmail.com)'})

# Parse the JSON response and extract the comments and sub-comments
data = response.json()
# the comments are in the second element of the data list
comments = data[1]['data']['children']

# For each comment and sub-comment
for comment in comments:
    # Check if it contains the sentence of interest
    if '7.' in comment['data']['body']:
        # Store the comment/sub-comment and its associated information
        print(f"Comment by {comment['data']['author']}:")
        print(comment['data']['body'])
        print(f"Upvotes: {comment['data']['ups']}")
        print("---")
    # Check if there are any sub-comments
    if comment['data']['replies']:
        sub_comments = comment['data']['replies']['data']['children']
        # For each sub-comment
        for sub_comment in sub_comments:
            # Check if it contains the sentence of interest
            if '7.' in sub_comment['data']['body']:
                # Store the sub-comment and its associated information
                print(f"Sub-comment by {sub_comment['data']['author']}:")
                print(sub_comment['data']['body'])
                print(f"Upvotes: {sub_comment['data']['ups']}")
                print("---")
