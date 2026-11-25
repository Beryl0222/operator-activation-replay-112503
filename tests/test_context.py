"""验证业务输入之间的引用关系及形状，不计算目标输出。"""
import numpy as np
from support.inspect_data import load_bundle

def test_linked_materials():
    _, arrays, r, scenarios = load_bundle()
    assert len(r['tokens']) == arrays['activation'].shape[0]
    assert sorted(r['reorder']) == list(range(len(r['tokens'])))
    assert len(set(r['consumers'])) == len(r['consumers'])
    assert len(r['zero_points']) == arrays['activation'].shape[1]
    assert arrays['scale'].shape[0] == arrays['activation'].shape[1]
