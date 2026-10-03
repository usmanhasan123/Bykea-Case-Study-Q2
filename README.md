
1. Install packages: `pip install -r requirements.txt`.
2. Open Jupyter in this folder: `jupyter lab`.
3. Run **01_data_pipeline.ipynb** from top to bottom.
4. Run **02_modeling_pipeline.ipynb** from top to bottom.

The supplied full dataset is in `data/raw/training.csv`. Notebook 1 outputs
`data/processed/customer_features.csv` with one row per newly acquired customer.
Notebook 2 reads that file, drops missing targets, trains logistic regression
and XGBoost, and displays train/test metrics and ROC curves. It also saves
`data/processed/model_metrics.csv`.

The sticky target means returning on at least three distinct dates during days
1–7 after the first purchase day. Only complete seven-day follow-up produces
a label. The complete-data cutoff is October 29, 2021. update it in notebook 1
when replacing the source. Later purchases define the target and never enter
the predictor list.
