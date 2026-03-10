import numpy as np

def box_blur(arr: np.ndarray, r: int) -> np.ndarray:
    if r <= 0:
        return arr.astype(np.float32, copy=False)

    a = arr.astype(np.float32, copy=False)
    h, w = a.shape
    k = 2 * r + 1
    p = np.pad(a, ((r, r), (r, r)), mode="edge")

    s = np.zeros((p.shape[0] + 1, p.shape[1] + 1), dtype=np.float32)
    s[1:, 1:] = p.cumsum(axis=0).cumsum(axis=1)

    total = (
        s[k : k + h, k : k + w]
        - s[0 : h,     k : k + w]
        - s[k : k + h, 0 : w]
        + s[0 : h,     0 : w]
    )
    return total / (k * k)

def normalize01(x: np.ndarray, eps: float = 1e-8) -> np.ndarray:
    x = x.astype(np.float32, copy=False)
    mn = float(x.min())
    mx = float(x.max())
    return (x - mn) / (mx - mn + eps)

def _pick_radii(n: int, island_count: int, land_frac: float, rng):
    land_frac = float(np.clip(land_frac, 0.02, 0.85))
    area_per = (land_frac * (n * n)) / max(1, island_count)
    r_eq = np.sqrt(area_per / np.pi)

    r_min = max(3, int(round(r_eq * 0.55)))
    r_max = max(r_min + 1, int(round(r_eq * 1.35)))

    r_max = min(r_max, max(8, n // 6))
    r_min = min(r_min, max(6, r_max - 2))

    return r_min, r_max

def generate_islands(n: int, seed: int, island_count: int):

    rng = np.random.default_rng(seed)
    r_min, r_max = _pick_radii(n, island_count, 0.18, rng)

    height = np.zeros((n, n), dtype=np.float32)
    yy, xx = np.mgrid[0:n, 0:n].astype(np.float32)

    centers = []

    for _ in range(island_count):

        for _ in range(100):
            rad = int(rng.integers(r_min, r_max + 1))
            cy = int(rng.integers(rad + 5, n - rad - 5))
            cx = int(rng.integers(rad + 5, n - rad - 5))

            ok = True
            for (py, px, pr) in centers:
                d = np.sqrt((cy - py)**2 + (cx - px)**2)
                if d < rad + pr + 5:
                    ok = False
                    break

            if ok:
                centers.append((cy, cx, rad))
                break

        d = np.sqrt((yy - cy) ** 2 + (xx - cx) ** 2)
        island = np.clip(1 - d / rad, 0, 1)
        height = np.maximum(height, island)

    land = height > 1e-4
    out = np.zeros((n, n), dtype=np.uint8)

    if np.any(land):
        lh = normalize01(height[land])
        out[land] = (np.floor(lh * 9).astype(np.int32) + 1).clip(1, 9)

    return out