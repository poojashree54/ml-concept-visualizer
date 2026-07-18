import json
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression

# 1. Create a simple 2-feature dataset (so it's easy to visualize)
X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    random_state=42
)

# 2. Train a simple classifier
model = LogisticRegression()
model.fit(X, y)

# 3. Export everything Codex needs to visualize it
export = {
    "model_type": type(model).__name__,
    "feature_names": ["feature_1", "feature_2"],
    "task": "classification",
    "classes": model.classes_.tolist()
}

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 50), np.linspace(y_min, y_max, 50))
grid = np.c_[xx.ravel(), yy.ravel()]
preds = model.predict(grid)

export["decision_grid"] = {
    "x": xx.ravel().tolist(),
    "y": yy.ravel().tolist(),
    "prediction": preds.tolist()
}
export["data_points"] = {
    "x": X[:, 0].tolist(),
    "y": X[:, 1].tolist(),
    "labels": y.tolist()
}

with open("model_export.json", "w") as f:
    json.dump(export, f)

print("Done! model_export.json created.")