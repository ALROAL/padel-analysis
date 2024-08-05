from torcheval.metrics import BinaryAccuracy, BinaryPrecision, BinaryRecall
from typing import List, Dict

_AVAILABLE_METRICS = {
    "binary_accuracy": BinaryAccuracy,
    "binary_precision": BinaryPrecision,
    "binary_recall": BinaryRecall
}

class MetricsEvaluator():
    def __init__(self, metric_names: List[str], device: str):
        self.metrics = initialize_metrics(metric_names, device)

    def update(self, output, labels):

        for name, metric in self.metrics.items():
            metric.update(output, labels)

    def compute(self) -> Dict:
        compute_results = {}
        for name, metric in self.metrics.items():
            compute_results[name] = metric.compute()
        return compute_results

    def reset(self):
        for name, metric in self.metrics.items():
            metric.reset()

def initialize_metrics(metric_names, device):

    metrics = {}
    for name in metric_names:
        metric = _AVAILABLE_METRICS.get(name)
        metrics[name] = metric(device=device)

    return metrics