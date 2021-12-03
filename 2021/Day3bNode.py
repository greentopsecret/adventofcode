class Node:
    _counter: int

    def __init__(self):
        self._counter = 0
        self._zero_node = None
        self._one_node = None

    def get_counter(self) -> int:
        return self._counter

    def get_zero_node(self):
        return self._zero_node

    def get_one_node(self):
        return self._one_node

    def increase_zero_node_counter(self) -> None:
        if self._zero_node is None:
            self._zero_node = Node()

        self._zero_node._increase_counter()

    def increase_one_node_counter(self) -> None:
        if self._one_node is None:
            self._one_node = Node()

        self._one_node._increase_counter()

    def get_zero_node_children_cnt(self) -> int:
        return self._zero_node.get_counter() if self._zero_node else 0

    def get_one_node_children_cnt(self) -> int:
        return self._one_node.get_counter() if self._one_node else 0

    def _increase_counter(self) -> None:
        self._counter += 1
