import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from map_generator import generate_islands
from island_analysis import (
    to_binary_map,
    find_islands,
    distances_from_base,
    shortest_bridge
)

def analyze_and_plot(height_map, n, island_count, subplot_idx):

    sea_level = 6
    binary_map = to_binary_map(height_map, sea_level)
    islands = find_islands(binary_map)

    base_x, base_y = 23, 60
    if binary_map[base_x][base_y] == 1:
        base_x, base_y = 1, 1

    distances = distances_from_base(binary_map, islands, base_x, base_y)

    for i, island in enumerate(islands):
        island["distance"] = distances[i]
        island["score"] = island["area"] / (distances[i] + 1)

    print(f"\n" + "-"*30)
    print(f"СТАТИСТИКА КАРТИ {n}x{n}")
    print(f"Кількість островів: {len(islands)}")

    bridge_result = shortest_bridge(binary_map, islands)

    if bridge_result:
        print(f"Найкоротший міст: {bridge_result[2]}")

    top5 = sorted(islands, key=lambda x: x["score"], reverse=True)[:5]
    nearest5 = sorted(islands, key=lambda x: x["distance"])[:5]

    print(f"\nТОП-5 ЗА РЕЙТИНГОМ:")
    for idx, island in enumerate(top5, 1):
        print(f"{idx}. Score: {island['score']:.3f}, Area: {island['area']}, Distance: {island['distance']}")

    print(f"\nТОП-5 НАЙБЛИЖЧИХ ДО БАЗИ:")
    for idx, island in enumerate(nearest5, 1):
        print(f"{idx}. Distance: {island['distance']}, Area: {island['area']}")

    ax = plt.subplot(1,3,subplot_idx)
    im = ax.imshow(height_map, cmap="terrain")
    plt.colorbar(im, ax=ax)

    plt.scatter(base_y, base_x, c="red", s=30, zorder=5)

    for i, island in enumerate(islands):
        min_x, min_y, max_x, max_y = island["bbox"]
        cx, cy = (min_y + max_y) / 2, (min_x + max_x) / 2

        plt.text(cx, cy, str(i+1),
                 color="black",
                 fontsize=7,
                 ha='center',
                 va='center',
                 zorder=7)

    offset = max(1, n // 50)

    for idx, island in enumerate(nearest5,1):

        min_x, min_y, max_x, max_y = island["bbox"]
        cx, cy = (min_y + max_y) / 2, (min_x + max_x) / 2

        plt.text(cx-offset, cy-offset,
                 f"N{idx}",
                 color="black",
                 fontsize=8,
                 weight='bold',
                 ha='right',
                 zorder=8)

        rect = patches.Rectangle(
            (min_y-0.5, min_x-0.5),
            island["width"],
            island["height"],
            linewidth=1,
            edgecolor="black",
            facecolor="none",
            zorder=4
        )

        ax.add_patch(rect)

    for idx, island in enumerate(top5,1):

        min_x, min_y, max_x, max_y = island["bbox"]
        cx, cy = (min_y + max_y) / 2, (min_x + max_x) / 2

        plt.text(cx+offset, cy+offset,
                 f"R{idx}",
                 color="red",
                 fontsize=8,
                 weight='bold',
                 ha='left',
                 zorder=8)

        rect = patches.Rectangle(
            (min_y-1, min_x-1),
            island["width"]+1,
            island["height"]+1,
            linewidth=1,
            edgecolor="red",
            facecolor="none",
            linestyle=':',
            zorder=4
        )

        ax.add_patch(rect)

    if bridge_result:

        id1,id2,_ = bridge_result

        b1 = islands[id1-1]["bbox"]
        b2 = islands[id2-1]["bbox"]

        y1,x1 = (b1[1]+b1[3])/2, (b1[0]+b1[2])/2
        y2,x2 = (b2[1]+b2[3])/2, (b2[0]+b2[2])/2

        plt.plot([y1,y2],[x1,x2],
                 color="red",
                 linestyle="--",
                 linewidth=2,
                 zorder=10)


params = ((100,7),(500,20),(1000,35))

grids=[]

for n,count in params:
    grids.append(generate_islands(n,14,count))

plt.figure(figsize=(18,6))

for i in range(len(grids)):
    analyze_and_plot(grids[i], params[i][0], params[i][1], i+1)

plt.tight_layout()
plt.show()