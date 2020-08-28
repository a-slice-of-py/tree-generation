# tree_generation

tree_generation is a Python library for implementing a tree-like structure.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tree_generation.

```bash
pip install -e .
```

## Usage

```python
from tree_generation import TreeGenerator

tree_generator = TreeGenerator()
tree = tree_generator.generate_tree(0)
path = tree_generator.path_to_node(tree.get(tree_generator.depth)[0])

print(f'Tree with root node at (0): {tree}')
print(f'Path to bottom-left node: {path}')
```

## Authors

* **Silvio Lugaro** - *Advanced Analytics team, Iren S.p.A.*
