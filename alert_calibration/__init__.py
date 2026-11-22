"""alert_calibration — 内部安全运营用的校准审计器。

对合成事故样本评估基准策略与候选策略的告警处置行为：
规则按固定优先级触发（两个指标同时越线），阈值只能取自输入给定的
整数候选；允许最多一个采集域不可信；fit 搜索满足全部允许资料解释的
固定阈值，review 单独评估给定阈值并给出可重放的真值见证。
"""

from .core import (
    CaseError,
    Case,
    Constraint,
    Evaluation,
    Event,
    Mark,
    Rule,
    load_case,
    supported_labels,
    SEVERITY,
    TRUTH_SEVERITY,
    LABELS,
)

__all__ = [
    "CaseError",
    "Case",
    "Constraint",
    "Evaluation",
    "Event",
    "Mark",
    "Rule",
    "load_case",
    "supported_labels",
    "SEVERITY",
    "TRUTH_SEVERITY",
    "LABELS",
]

__version__ = "1.0.0"
