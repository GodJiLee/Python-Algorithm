import collections
def maxDepth(self, root) -> int:
    if root is None:
        return 0

    queue = collections.deque([root]) # O(1)
    depth = 0

    while queue:
        depth += 1
        # insert child nodes into queue
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    # BFS iterative number == depth
    return depth
