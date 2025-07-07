def getMostVisited(n, sprints):
    difference = [0] * (n + 2)  # 1-based indexing with extra space to avoid index issues
    for i in range(len(sprints) - 1):
        start = sprints[i]
        end = sprints[i + 1]
        if start < end:
            difference[start] += 1
            difference[end + 1] -= 1
        else:
            difference[end] += 1
            difference[start + 1] -= 1
    max_visits = 0
    result = 1
    current_visits = 0
    for marker in range(1, n + 1):
        current_visits += difference[marker]
        if current_visits > max_visits:
            max_visits = current_visits
            result = marker
        elif current_visits == max_visits and marker < result:
            result = marker
    return result
