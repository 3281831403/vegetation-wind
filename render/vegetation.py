"""植被风摆：相位、LOD 与批次：待实现的核心模块。"""


def wind_phase(time, speed, phase):
    """风相位按实例偏移。"""
    raise NotImplementedError

def bend_amount(wind, stiffness, phase):
    """弯曲量按刚度。"""
    raise NotImplementedError

def lod_index(distance, distances):
    """LOD 索引不越界。"""
    raise NotImplementedError

def cull_frustum(points, bounds):
    """视锥裁剪包含边缘。"""
    raise NotImplementedError

def billboard_scale(distance, base, min_scale):
    """公告板缩放有下限。"""
    raise NotImplementedError

def shadow_cascade(lod, max_cascade):
    """阴影级联不超过上限。"""
    raise NotImplementedError

def batch_count(count, max_batch):
    """实例批次拆分。"""
    raise NotImplementedError

def instance_hash(x, y, seed):
    """实例哈希确定性。"""
    raise NotImplementedError

def terrain_align(height, slope, max_slope):
    """地形贴合按坡度。"""
    raise NotImplementedError

def commit_instances(statuses):
    """批量实例全部成功才提交。"""
    raise NotImplementedError
