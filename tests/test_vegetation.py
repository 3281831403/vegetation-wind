import pytest

from render import vegetation as mod

CASES = [
    ('wind_phase', [0.0, 2.0, 0.0], 0.0, True),
    ('wind_phase', [0.7853981633974483, 2.0, 0.0], 1.0, True),
    ('bend_amount', [2.0, 4.0, 0.5], 0.25, True),
    ('lod_index', [5.0, [10.0, 30.0]], 0, False),
    ('lod_index', [50.0, [10.0, 30.0]], 2, False),
    ('cull_frustum', [[[0, 0], [5, 5]], [0, 1, 0, 1]], [0], False),
    ('billboard_scale', [10, 20, 0.5], 2.0, True),
    ('billboard_scale', [100, 20, 0.5], 0.5, True),
    ('shadow_cascade', [2, 1], 1, False),
    ('batch_count', [100, 16], 7, False),
    ('instance_hash', [1.5, 2.5, 7], 74993409, False),
    ('terrain_align', [10.0, 0.5, 1.0], 9.5, True),
    ('commit_instances', [[True, True]], True, False),
    ('lod_index', [10.0, [10.0, 30.0]], 0, False),
    ('terrain_align', [10.0, 2.0, 1.0], 9.0, True),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_vegetation_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
