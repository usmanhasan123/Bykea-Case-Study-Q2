
For notebook execution and development
1. Install packages: `pip install -r requirements.txt`.
2. Open Jupyter in this folder: `jupyter lab`.
3. Run **01_data_pipeline.ipynb** from top to bottom using the value of x as *'training'*.
4. Run **02_modeling_pipeline.ipynb** from top to bottom. The evaluation scores and ROC-AUC curve will be stored as separate experiments in the experiments folder.

For using the app
5. Run **01_data_pipeline.ipynb** from top to bottom using the value of x as *'production'*. The resultant data will be saved in **'./data/processed/customer_features_prod_data.csv'**
6. Go to the app (link mentioned below) and upload the csv file resulting from step 5.
7. Alternatively, go to **'./data/processed/customer_features_prod_data.csv'** and use the data already present there as an input for the app
app link: https://bykea-case-study-q2-abzdcfgzgodvpyztjfilkf.streamlit.app/

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
