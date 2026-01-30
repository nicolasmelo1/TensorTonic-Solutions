from datetime import datetime

def promote_model(models):
    def ts(m):
        return datetime.fromisoformat(m["timestamp"])

    best = max(
        models,
        key=lambda m: (
            float(m["accuracy"]),     # higher better
            -float(m["latency"]),     # lower better
            ts(m)                     # later better
        )
    )
    return best["name"]