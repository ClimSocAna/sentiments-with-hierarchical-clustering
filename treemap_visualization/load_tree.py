import json
from typing import Any, Dict, Optional


class Node:
    """Represents a cluster in the clustering hierarchy.

    Attributes:
        name: Unique name consiting of original level and cluster id within level.
        level: Original level in clustering tree.
        level_id: Cluster id within original level.
        weight_dict: Stores weight (= number of tweets in cluster)
        keywords: Extracted keywords.
        label: User-chosen label for the cluster.
        description: User-chosen description for the cluster.
        parent: parent of cluster, represented by the Node.name attribute.
        children: Children of cluster, represented by the Node.name attributes.
    """

    def __init__(
        self,
        name: str,
        level: int,
        level_id: int,
        weight_dict: Dict[str, int],
        keywords: list,
        label: Optional[str] = None,
        description: Optional[str] = None,
        sentiment_dict: Optional[Dict[str, Dict[str, int]]] = None,
        parent: Optional[Any] = None,
        children: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.level = level
        self.level_id = level_id

        self.weight_dict = weight_dict
        self.keywords = keywords

        self.label = label
        self.description = description

        self.sentiment_dict = sentiment_dict

        self.parent = parent
        self._children = children

    def __repr__(self):
        return repr(
            f"level={self.level}, level_id={self.level_id}, weight={self.weight()}, keywords={self.keywords}"
        )

    @property
    def children(self, nodes_only: bool = False):
        if self._children is not None:
            if nodes_only:
                return list(self._children.values())
            return self._children
        return None

    @children.setter
    def children(self, children: Dict[str, Any]):
        self._children = children

    @property
    def is_root(self):
        if self.parent is None:
            return True
        return False

    @property
    def is_leaf(self):
        if self.children is None:
            return True
        return False

    def weight(self, kind: str = "total"):
        """Get weight for cluster.

        Args:
            kind: Period for which tweets are considered.
        """
        if kind in self.weight_dict:
            return self.weight_dict[kind]
        return -1

    def sentiment_score(self, kind: str = "total"):
        """Get sentiment score for cluster.

        Args:
            kind: Period for which tweets are considered.
        """
        label_map = {"positive": 1, "neutral": 0, "negative": -1}
        if self.sentiment_dict is not None and kind in self.sentiment_dict:
            return round(
                sum(
                    [
                        self.sentiment_dict[kind][label] * score
                        for label, score in label_map.items()
                    ]
                )
                / sum(list(self.sentiment_dict[kind].values())),
                4,
            )
        return None


class Tree:
    """Represents the clustering hierarchy. Used to load and storing clustering hierarchy.

    Attributes:
        levels: Stores mapping of original level id to clusters in level.
    """

    def __init__(self, levels: Dict[str, Dict[int, Node]]):
        self.levels = levels

    @staticmethod
    def _load_nodes(path: str):
        with open(path) as f:
            nodelist = [json.loads(line) for line in f]

        return nodelist

    @classmethod
    def build_tree_from_path(cls, path: str):
        nodelist = Tree._load_nodes(path)

        nodelist = sorted(nodelist, key=lambda x: x["level"])

        levels, current_level, level_map = {}, nodelist[0]["level"], {}
        for node_dict in nodelist:

            if node_dict["level"] > current_level:
                levels[current_level] = level_map
                current_level, level_map = node_dict["level"], {}

            node = Node(
                name=node_dict["name"],
                level=node_dict["level"],
                level_id=node_dict["level_id"],
                weight_dict=node_dict["weight_dict"],
                label=node_dict["label"],
                description=node_dict["description"],
                keywords=node_dict["keywords"],
                sentiment_dict=(
                    node_dict["sentiment_dict"]
                    if "sentiment_dict" in node_dict
                    else None
                ),
            )

            children = None
            if "children" in node_dict and node_dict["children"] is not None:
                children = {}
                for level, level_id in [
                    [int(c) for c in child.split("/")]
                    for child in node_dict["children"]
                ]:
                    child = levels[level][level_id]
                    child.parent = node
                    children[child.name] = child

            node.children = children

            level_map[node.level_id] = node

        levels[current_level] = level_map

        return cls(levels)

    def __repr__(self):
        return repr(f"#levels: {len(self.levels)}, #roots: {len(self.roots)}")
