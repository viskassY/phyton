def get_full_clock_angle(h, m, s):
    
    sec_angle = s * 6
    min_angle = (m * 6) + (s * 0.1)
    
    # 0.00833 — 0.5 град / 60 сек
    hour_angle = ((h % 12) * 30) + (m * 0.5) + (s * 0.00833)
    angle = abs(hour_angle - min_angle)
    
    if angle > 180:
        angle = 360 - angle
        
    return round(angle, 2) 
print(f"Кут: {get_full_clock_angle(15, 30, 10)}°")