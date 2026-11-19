"""植被风摆：相位、LOD 与批次：核心模块实现。"""

import math


def wind_phase(time, speed, phase):
    """风相位按实例偏移。"""
    return math.sin(time * speed + phase)

def bend_amount(wind, stiffness, phase):
    """弯曲量按刚度。"""
    return wind / stiffness * phase

def lod_index(distance, distances):
    """LOD 索引不越界。"""
    index = sum(1 for d in distances if distance > d)
    return min(index, len(distances))

def cull_frustum(points, bounds):
    """视锥裁剪包含边缘。"""
    min_x, max_x, min_y, max_y = bounds
    return [
        i for i, (px, py) in enumerate(points)
        if min_x <= px <= max_x and min_y <= py <= max_y
    ]

def billboard_scale(distance, base, min_scale):
    """公告板缩放有下限。"""
    return max(base / distance, min_scale)

def shadow_cascade(lod, max_cascade):
    """阴影级联不超过上限。"""
    return min(lod, max_cascade)

def batch_count(count, max_batch):
    """实例批次拆分。"""
    return math.ceil(count / max_batch)

def instance_hash(x, y, seed):
    """实例哈希确定性。"""
    return int(x * 73856093) ^ int(y * 19349663) ^ seed

def terrain_align(height, slope, max_slope):
    """地形贴合按坡度。"""
    return height - min(slope, max_slope)

def commit_instances(statuses):
    """批量实例全部成功才提交。"""
    return all(statuses)
