import praw

reddit = praw.Reddit(
        client_id = os.environ.get('CLIENT_ID'),
        client_secret = os.environ.get('CLIENT_SECRET'),
        user_agent = 'comments'
    )

# https://praw.readthedocs.io/en/latest/tutorials/comments.html
def get_post_by_id(id):
    post = reddit.submission(id)
    post.comments.replace_more(limit = None)

    return post

def get_hot_k_posts_from_subreddit(k, r = 'all'):
    return reddit.subreddit(r).hot(limit = k)