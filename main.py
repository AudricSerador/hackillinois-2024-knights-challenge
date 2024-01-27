import requests
import os
from dotenv import load_dotenv

load_dotenv()
JWT_TOKEN = os.getenv("JWT_TOKEN")

def get_max_goodness(nodes, edges):
    graph = {node : [] for node in nodes}
    visited = {node : False for node in nodes}
    
    def dfs(node):
        visited[node] = True
        total = nodes[node]
        for neighbor in graph[node]:
            if not visited[neighbor]:
                total += dfs(neighbor)
        return total

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    max_goodness = float('-inf')
    for node in nodes:
        if not visited[node]:
            goodness = dfs(node)
            if goodness > max_goodness:
                max_goodness = goodness

    return max_goodness

def get_data(jwt):
    headers = {
        "Authorization": jwt,
        "Content-Type": "application/json"
    }
    response = requests.get('https://artemis.hackillinois.org/challenge', headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return Exception(f"Error getting data: {response.status_code}")

def post_data(jwt, max_goodness):
    headers = {
        "Authorization": jwt,
        "Content-Type": "application/json"
    }
    data = {
        "max_goodness": max_goodness
    }
    response = requests.post('https://artemis.hackillinois.org/challenge', headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()
    else:
        return Exception(f"Error posting data: {response.status_code}")
    
data = get_data(JWT_TOKEN)

nodes = data['wizards']
edges = data['alliances']
max_goodness = get_max_goodness(nodes, edges)

response = post_data(JWT_TOKEN, max_goodness)
print(response)
