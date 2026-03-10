import numpy as np
from collections import deque


def to_binary_map(height_map, sea_level):
    return (height_map > sea_level).astype(int)


# ЧАСТИНА 2 

def find_islands(binary_map):

    n = binary_map.shape[0]
    visited = np.zeros_like(binary_map)
    islands = []

    directions8 = [(-1,-1), (-1,0), (-1,1),
                   (0,-1),         (0,1),
                   (1,-1),  (1,0), (1,1)]

    directions4 = [(-1,0),(1,0),(0,-1),(0,1)]

    for i in range(n):
        for j in range(n):
            if binary_map[i][j] == 1 and not visited[i][j]:
                queue = deque([(i,j)])
                visited[i][j] = 1

                cells = []
                coastal = []
                perimeter = 0

                min_x, min_y = i, j
                max_x, max_y = i, j

                while queue:
                    x,y = queue.popleft()
                    cells.append((x,y))

                    min_x = min(min_x, x)
                    min_y = min(min_y, y)
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

                    is_coastal = False

                    for dx,dy in directions4:
                        nx, ny = x+dx, y+dy
                        if nx<0 or ny<0 or nx>=n or ny>=n:
                            perimeter += 1
                            is_coastal = True
                        elif binary_map[nx][ny] == 0:
                            perimeter += 1
                            is_coastal = True

                    if is_coastal:
                        coastal.append((x,y))

                    for dx,dy in directions8:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<n:
                            if binary_map[nx][ny]==1 and not visited[nx][ny]:
                                visited[nx][ny]=1
                                queue.append((nx,ny))

                islands.append({
                    "cells": cells,
                    "area": len(cells),
                    "bbox": (min_x,min_y,max_x,max_y),
                    "width": max_y-min_y+1,
                    "height": max_x-min_x+1,
                    "perimeter": perimeter,
                    "coastal": coastal
                })

    return islands


#  ЧАСТИНА 3 

def distances_from_base(binary_map, islands, base_x, base_y):

    n = binary_map.shape[0]
    dist = np.full((n,n), -1)
    queue = deque([(base_x, base_y)])
    dist[base_x][base_y]=0

    directions4=[(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x,y = queue.popleft()
        for dx,dy in directions4:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if binary_map[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    queue.append((nx,ny))

    result=[]
    for island in islands:
        min_d=float("inf")
        for x,y in island["coastal"]:
            for dx,dy in directions4:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<n:
                    if binary_map[nx][ny]==0 and dist[nx][ny]!=-1:
                        min_d=min(min_d,dist[nx][ny])
        result.append(min_d)

    return result


#  ЧАСТИНА 5 

def shortest_bridge(binary_map, islands):

    n=binary_map.shape[0]
    labels=np.zeros_like(binary_map)
    id=1

    for island in islands:
        for x,y in island["cells"]:
            labels[x][y]=id
        id+=1

    queue=deque()
    dist=np.full((n,n),-1)

    for i in range(n):
        for j in range(n):
            if labels[i][j]>0:
                queue.append((i,j))
                dist[i][j]=0

    directions4=[(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        x,y=queue.popleft()
        for dx,dy in directions4:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<n:
                if labels[nx][ny]==0:
                    labels[nx][ny]=labels[x][y]
                    dist[nx][ny]=dist[x][y]+1
                    queue.append((nx,ny))
                elif labels[nx][ny]!=labels[x][y]:
                    return labels[x][y], labels[nx][ny], dist[nx][ny] + dist[x][y]

    return None