import heapq

def dijkstra(graph, start):
    # Создание словаря для хранения расстояний до каждой вершины.
    distances = {vertex: float('infinity') for vertex in graph}

    # Расстояние до начальной вершины равно 0.
    distances[start] = 0

    # Создание очереди для хранения вершин и их расстояний.
    priority_queue = [(0, start)]


    while priority_queue:
        # Извлечение вершины с наименьшим расстоянием из очереди.
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние до вершины уже больше, чем сохранённое расстояние, игнорируем её.
        if current_distance > distances[current_vertex]:
            continue

        # Рассмотрим все соседние вершины текущей вершины.
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найден более короткий путь до соседа, обновим расстояние.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 4, 'C': 7},
    'B': {'A': 5, 'D': 6, 'E': 8},
    'C': {'A': 7, 'D': 2, 'E': 5},
    'D': {'B': 2, 'C': 2, 'E': 4,'F': 4},
    'E': {'C': 5, 'D': 1, 'F': 11},
    'F': {'B': 8, 'D': 4, 'E': 11}
}

result = dijkstra(graph, 'A')
# Выводим результат.
print("Кратчайшие расстояния до каждой вершины:")
for vertex, distance in result.items():
    print(f"До вершины {vertex}: {distance}")