from anytree import Node, find_by_attr
from anytree.exporter import DotExporter, JsonExporter
from anytree.importer import JsonImporter

def load_comment_tree_from_post(post):
    # create root node (for the post itself)
    root = Node(post.id)

    # create a node for each comment
    for comment in post.comments.list():
        parent_id = comment.parent_id[3:]
        Node(
            comment.id, 
            parent = find_by_attr(root, parent_id), 
            score  = comment.score
        )

    return root

def load_comment_tree_from_json(fname):
    importer = JsonImporter()

    with open(fname, 'r') as f:
        return importer.read(f)

def save_comment_tree_to_json(root):
    exporter = JsonExporter(indent = 2, sort_keys = True)
    
    with open(f'{root.name}.json', 'w') as f:
        exporter.write(root, f)

def save_comment_tree_to_dotfile(root):
    exporter = DotExporter(root)
    exporter.to_dotfile(f'{root.name}.dot')