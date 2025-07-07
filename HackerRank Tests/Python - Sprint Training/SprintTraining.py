def getMostVisited(n, sprints):
    visits = [0] * (n + 1)  # 1-based indexing
    for i in range(len(sprints) - 1):
        start = sprints[i]
        end = sprints[i + 1]
        if start < end:
            for marker in range(start, end + 1):
                visits[marker] += 1
        else:
            for marker in range(end, start + 1):
                visits[marker] += 1
    max_visits = max(visits[1:])  # Exclude index 0
    for marker in range(1, n + 1):
        if visits[marker] == max_visits:
            return marker
    return -1  # Should not happen as per problem constraints
