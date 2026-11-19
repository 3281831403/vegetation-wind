# 植被风摆：相位、LOD 与批次

草地在阵风里整片同步摆动、远处闪烁：风相位按全局时间而不是实例偏移，弯曲量没有按刚度，LOD 索引越界，视锥裁剪漏掉边缘实例，公告板缩放没有下限，阴影级联超过上限，批次没有拆分，实例哈希不唯一，地形贴合按坡度算反，批量实例只提交一半。

## 目录结构

```
README.md
conftest.py
.gitignore
render/__init__.py
render/vegetation.py
tests/test_vegetation.py
```

## 当前状态

`render/vegetation.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_vegetation.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 风相位按实例偏移
2. 弯曲量按刚度
3. LOD 索引不越界
4. 视锥裁剪包含边缘
5. 公告板缩放有下限
6. 阴影级联不超过上限
7. 实例批次拆分
8. 实例哈希确定性
9. 地形贴合按坡度
10. 批量实例统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `render/vegetation.py`
后 15 条用例应全部通过。
