import heapq

def model_graph(buses):
    graph = {}
    for bus in buses:
        for i in range(len(bus) - 1):
            if bus[i] not in graph:
                graph[bus[i]] = [bus[i+1]]
            else:
                graph[bus[i]].append(bus[i+1])
    return graph

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return path, distances[end]

def find_min_bus_changes(buses, start, end):
    graph = model_graph(buses)
    path, min_changes = dijkstra(graph, start, end)
    return min_changes

# Example usage
buses = [
    [1, 3, 7],
    [4, 7, 9, 10],
    [2, 1, 10],
    [8, 4, 11, 10]
]
start = 1
end = 8

min_changes = find_min_bus_changes(buses, start, end)
print(f"Minimum number of bus changes required: {min_changes}")
