'''
'''

def zombie_clusters(zombies):
    n = len(zombies)

    number_of_clusters = 0

    stack = []

    visited = []

    def zombie_helper(zombies)
        for i in range(n):
            if not visited[i]:
                number_of_clusters += 1
                dfs[zombies[i]]
        return number_of_clusters

    def dfs(e):
        visited[i] = true
        for i in range(n):
            if zombies[i] == 'i' and not visited[i]:
                dfs(zombies[i])
        return




