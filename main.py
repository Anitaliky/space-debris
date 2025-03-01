# main.py

import os
import pandas as pd

# Import modules from our package structure
from utils.file_io import read_labels_train
from preprocessing.data_cleaning import load_and_merge_debris_data
from eda.exploration import perform_eda
from visualization.plots import plot_collision_risk_3D, plot_clusters_pairplot
from modeling.clustering import assess_collision_risk


def main():
    # A) Read labels (training set)
    labels_file = 'labels_train.dat'
    if os.path.exists(labels_file):
        df_labels = read_labels_train(labels_file)
    else:
        print(f"Warning: {labels_file} not found. Proceeding without labels.")
        df_labels = pd.DataFrame()

    # B) Load & merge debris data (training set)
    df_debris_merged = load_and_merge_debris_data(deb_folder='deb_train', labels_df=df_labels)
    if df_debris_merged.empty:
        print("No debris data found or merged. Check your folder paths.")
        return

    # C) Perform EDA
    perform_eda(df_debris_merged)

    # Apply collision risk assessment function to df_debris_merged
    df_collision_risk, silhouette_avg = assess_collision_risk(df_debris_merged, eps=1, min_samples=5)

    print(f'silhouette score: {silhouette_avg}')

    # Generate 3D visualization
    plot_collision_risk_3D(df_collision_risk)

    # Generate pairplot visualization
    features = ['sma', 'ecc', 'inc', 'raan', 'arg_perigee', 'cluster']
    plot_clusters_pairplot(df_collision_risk[features])

    print("\n=== Pipeline Complete ===")


# if __name__ == "__main__":
#     main()
