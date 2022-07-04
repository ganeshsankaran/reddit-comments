from api import *
from metrics import *
from plot import *
from tree import *

import statistics
import sys

# x data
scores      = []

# y data
agg_unweighted_heights    = []
agg_unweighted_sizes      = []
agg_unweighted_potentials = []
agg_weighted_heights      = []
agg_weighted_sizes        = []
agg_weighted_potentials   = []

# aggregation function
# mean, median, or max
func = max

posts = get_hot_k_posts_from_subreddit(20, 'dankmemes')

for post in posts:
    # If post has too many comments, skip
    if post.num_comments > 1500:
        print(f'{post.id}...Skipped')
        
        continue

    post.comments.replace_more(limit = None)
    root = load_comment_tree_from_post(post)

    # save x data
    scores.append(post.score)

    # save y data
    agg_unweighted_heights.append(
        func(get_unweighted_heights(root).values())
    )

    agg_unweighted_sizes.append(
        func(get_unweighted_sizes(root).values())
    )

    agg_unweighted_potentials.append(
        func(get_unweighted_potentials(root).values())
    )

    agg_weighted_heights.append(
        func(get_weighted_heights(root).values())
    )

    agg_weighted_sizes.append(
        func(get_weighted_sizes(root).values())
    )

    agg_weighted_potentials.append(
        func(get_weighted_potentials(root).values())
    )

    print(f'{post.id}...Done')

save_scatter_as_png(
    scores, agg_unweighted_heights,
    'Upvotes', 'Unweighted Height'
)

save_scatter_as_png(
    scores, agg_unweighted_sizes,
    'Upvotes', 'Unweighted Size'
)

save_scatter_as_png(
    scores, agg_unweighted_potentials,
    'Upvotes', 'Unweighted Potential'
)

save_scatter_as_png(
    scores, agg_weighted_heights,
    'Upvotes', 'Weighted Height'
)

save_scatter_as_png(
    scores, agg_weighted_sizes,
    'Upvotes', 'Weighted Size'
)

save_scatter_as_png(
    scores, agg_weighted_potentials,
    'Upvotes', 'Weighted Potential'
)