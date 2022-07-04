from anytree import Node

import math

# get unweighted sizes
def get_unweighted_sizes(root):
    return {
        comment.name: len(comment.descendants)
        for comment in root.children
    }

# get unweighted heights
def get_unweighted_heights(root):
    return {
        comment.name: comment.height
        for comment in root.children
    }

# get unweighted size of subtree
def get_unweighted_S(node):
    return 1 + len(node.descendants)

# get unweighted rank of subtree
def get_unweighted_rank(node):
    return math.log2(get_unweighted_S(node))

# get unweighted potential of each comment
def get_unweighted_potentials(root):
    potentials = {}
    
    # iterate over top-level comments
    for comment in root.children:
        phi = get_unweighted_rank(comment)
        
        # iterate over replies, take sum of ranks
        for reply in comment.descendants:
            phi += get_unweighted_rank(reply)
        
        potentials[comment.name] = phi

    return potentials

# get weighted sizes
def get_weighted_sizes(root):
    sizes = {}

    # iterate over top-level comments
    for comment in root.children:
        size = abs(comment.score)

        # iterate over replies, take sum of scores
        for reply in comment.descendants:
            size += abs(reply.score)
    
        sizes[comment.name] = size
    
    return sizes

# get weighted heights
def get_weighted_heights(root):
    heights = {}

    for comment in root.children:
        max_height = -1

        for leaf in comment.leaves:
            # NOTE: multiple leaves may be at same depth,
            # so we want to calculate the maximum weighted
            # height for any such node

            # check if leaf is at max depth
            # ignore root in depth computation
            if leaf.depth - 1 != comment.height:
                continue

            # calculate weighted height
            # update max weighted height, if applicable
            max_height = max(
                max_height,
                # ignore root
                sum([abs(reply.score) for reply in leaf.path[1:]])
            )
        
        heights[comment.name] = max_height

    return heights

# get weighted size of subtree
def get_weighted_S(node):
    return sum([reply.score for reply in node.descendants])

# get weighted rank of subtree
def get_weighted_rank(node):
    # take absolute value to prevent taking log(-)
    # add 1 to prevent taking log(0)
    return math.log2(abs(get_weighted_S(node)) + 1)

# get weighted potential of each comment
def get_weighted_potentials(root):
    potentials = {}
    
    # iterate over top-level comments
    for comment in root.children:
        phi = get_weighted_rank(comment)
        
        # iterate over replies, take sum of ranks
        for reply in comment.descendants:
            phi += get_weighted_rank(reply)
        
        potentials[comment.name] = phi

    return potentials