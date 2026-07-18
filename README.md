# ML Concept Visualizer

Turn any machine learning concept — or your own trained model — into a polished, interactive, explained visualization in seconds. Built for **OpenAI Build Week**, powered by **GPT-5.6** and **Codex**.

## 🔗 Live Demos

- **[Gradient Descent Simulator](https://poojashree54.github.io/ml-concept-visualizer/sim.html)** — see how gradient descent can get stuck at local minima vs. saddle points
- **[Logistic Regression Classifier](https://poojashree54.github.io/ml-concept-visualizer/classifier_viz.html)** — a real trained model's decision boundary, visualized automatically
- **[Overfitting vs. Underfitting](https://poojashree54.github.io/ml-concept-visualizer/overfitting_viz.html)** — watch a polynomial fit go from underfit to overfit in real time

## 💡 The Idea

Abstract ML concepts are hard to teach with text and static diagrams alone. This project uses AI to generate **functional, interactive learning modules on the fly** — either from a plain-English description of a concept, or from a real trained ML model.

Instead of writing custom visualization code by hand for every concept or every model, an AI pipeline does it:

1. **GPT-5.6** takes a concept description (or a model's exported prediction data) and designs a structured specification: what should be visualized, what the interactive controls are, and what the accompanying explanation should say.
2. **Codex** takes that specification and writes a complete, self-contained, working HTML/JavaScript interactive module — including the simulation logic, the UI, and an explanation panel — with no manual coding required.
3. A **verification step** checks the generated module actually runs correctly, feeding any errors back to Codex to fix automatically.

## 🧠 How GPT-5.6 and Codex Work Together

| Step | Model | Role |
|---|---|---|
| 1. Concept/Model Understanding | GPT-5.6 | Turns a plain-English concept or a model's raw prediction data into a structured spec (variables, math, what to visualize, plain-language explanation) |
| 2. Code Generation | Codex | Builds a self-contained, functional HTML/JS interactive module from that spec |
| 3. Verification & Repair | Codex | Detects rendering/runtime errors and iteratively fixes them until the module works |

This is a genuine division of labor: GPT-5.6 handles **understanding and structuring**, Codex handles **building and fixing working software** — reflecting how each model is best used.

## 📦 What's in this repo

```
ml-concept-visualizer/
├── sim.html                 # Gradient descent simulator (concept-based)
├── classifier_viz.html      # Real trained model's decision boundary (model-based)
├── overfitting_viz.html     # Overfitting/underfitting demo (concept-based)
├── model_export.json        # Exported prediction data from the trained classifier
├── train_and_export.py      # Script that trains a simple classifier and exports its data for visualization
└── README.md
```

## 🚀 Running it locally

All three HTML files are self-contained and can be opened directly, though `classifier_viz.html` fetches its data from `model_export.json`, which requires a local server to avoid browser `file://` restrictions:

```bash
# From the project folder:
python -m http.server 8000
```

Then open in your browser:
```
http://localhost:8000/sim.html
http://localhost:8000/classifier_viz.html
http://localhost:8000/overfitting_viz.html
```

(`sim.html` and `overfitting_viz.html` embed their data directly and can also be opened by double-clicking the file.)

## 🔬 Bringing your own model

To visualize your own trained classifier:

1. Run `train_and_export.py` (or adapt it) with your own model and data to produce `model_export.json`. It exports:
   - A grid of predictions across the feature space (for the decision boundary)
   - The real training data points (for overlay)
2. Place `model_export.json` in the project folder.
3. Prompt Codex with a description of your model and what it predicts, and it will generate a new visualization matching your data's shape and classes.

## 🎯 Why this matters

- **For learners**: instantly generated, interactive explanations of ML concepts, rather than static textbook diagrams.
- **For practitioners**: point it at your own trained model and get an explained visualization of its actual behavior — useful for debugging, teaching, or presenting your work.
- **For builders**: a working example of an AI pipeline where one model (GPT-5.6) plans and structures, and another (Codex) builds and verifies real, functional software — end to end, autonomously.

## 🛠️ Built With

- GPT-5.6 (concept/model understanding and spec generation)
- Codex (autonomous code generation and self-correction)
- Python + scikit-learn (model training/export)
- Vanilla JavaScript + HTML5 Canvas (all generated visualizations — no external libraries)

---

Built for OpenAI Build Week 2026.
