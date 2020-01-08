import numpy as np
import itertools
import random
import datetime
from collections import namedtuple

class TreeGenerator():
    """Implement a tree-like structure.
    """
    
    
    def __init__(self, depth : int = 5, growth_rate : int = 2):
        """Initialize self.
        
        Parameters
        ----------
        depth : int, optional
            Depth of the tree structure in terms of levels, by default 5.
        growth_rate : int, optional
            Rate of tree growth in terms of number of children nodes for each parent node, by default 2.
        """
        
        # len(last_level) = growth_rate**(depth + 1)
        
        self.depth = depth # tree depth in terms of number of levels - excluding the root level!
        self.growth_rate = growth_rate # number of children nodes for each parent node
        self.make_node = namedtuple('node', ['contents', 'level', 'child_of', 'child_number']) # struct to contain each node, made of its attribute (contents, level, child_of, child_number)
                
    def update_contents(self, contents):
        """Let perform custom update of node contents.
        
        Parameters
        ----------
        contents 
            Almost any Python object.
        
        Returns
        -------
        CustomType
            An updated Python object.
        """
        updated_contents = contents
        return updated_contents   
        
    def get_children(self, node : namedtuple) -> list:
        """Retrieve children of a given parent node.
        
        Parameters
        ----------
        node : namedtuple
            The parent node,
        
        Returns
        -------
        list of namedtuple
            The list of children of the parent node.
        """     
        children = [self.make_node(contents=self.update_contents(node.contents), 
                                   level=node.level + 1, 
                                   child_of=node, 
                                   child_number=k) 
                    for k in range(self.growth_rate)]
        
        return children
    
    def generate_tree(self, root_contents) -> dict:
        """Generate a tree given the contents of the root node. 

        Parameters
        ----------
        root_contents : CustomType
            Contents of the root node.
        
        Returns
        -------
        dict
            A dict containing the levels of the tree as keys and the corresponding lists of nodes as values.
        """

        start_time = datetime.datetime.now()
                
        tree = {}
        root = self.make_node(contents=root_contents, 
                              level=0,
                              child_of=None,
                              child_number=0) # initialization of root node
        tree[0] = [root] # initialization of root level
        
        for k in range(1, self.depth + 1): 
            tree[k] = list(itertools.chain.from_iterable([self.get_children(node) for node in tree[k-1]])) 
            
        end_time = datetime.datetime.now()
        
        execution_time = (end_time - start_time).total_seconds()
        print('Tree generation time (depth={}, growth rate={}): {} s'.format(self.depth, self.growth_rate, execution_time))
        
        return tree
    
    def path_to_node(self, node : namedtuple) -> list:
        """Retrieve a path from the root node to the specified one.
        
        Parameters
        ----------
        node : namedtuple
            The target node (at the end of the path).
        
        Returns
        -------
        list
            The path between the root node and the target one in terms of tree nodes.
        """
               
        path = [node]
        for k in range(node.level):
            path.append(node.child_of)
            node = node.child_of                    
        path = path[::-1]       
        
        return path

