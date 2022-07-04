from api import *
from metrics import *
from plot import *
from tree import *

import json
import math
import os
import sys

def analyze_post(id, plot = False):
    # get post
    post = get_post_by_id(id)

    # load comment tree
    # see if already loaded before
    # i.e. search for the file name in directory
    fname = f'{post.id}.json'

    if os.path.exists(fname):
        root = load_comment_tree_from_json(fname)
    else:
        root = load_comment_tree_from_post(post)
        save_comment_tree_to_json(root)
        save_comment_tree_to_dotfile(root)

    save_histogram_as_png(
        get_unweighted_heights(root).values(), 
        post.id,
        'Unweighted Height'
    )

    save_histogram_as_png(
        get_unweighted_sizes(root).values(), 
        post.id,
        'Unweighted Size'
    )

    save_histogram_as_png(
        get_unweighted_potentials(root).values(), 
        post.id,
        'Unweighted Potential'
    )

    save_histogram_as_png(
        get_weighted_heights(root).values(), 
        post.id,
        'Weighted Height'
    )

    save_histogram_as_png(
        get_weighted_sizes(root).values(), 
        post.id,
        'Weighted Size'
    )

    save_histogram_as_png(
        get_weighted_potentials(root).values(), 
        post.id,
        'Weighted Potential'
    )

if __name__ == '__main__':
    analyze_post(sys.argv[1])