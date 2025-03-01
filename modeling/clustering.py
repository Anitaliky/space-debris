import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Function to perform collision risk assessment using clustering
def assess_collision_risk(df, eps=0.5, min_samples=5):
    """
    Identifies high-risk collision zones by clustering debris based on orbital parameters.

    Args:
        df (DataFrame): The dataset containing orbital elements.
        eps (float): Maximum distance between points to be considered in the same cluster (DBSCAN parameter).
        min_samples (int): Minimum number of debris points required to form a dense region.

    Returns:
        DataFrame with cluster labels and a risk score per cluster.
        Silhouette Score value indicating clustering quality.
    """
    # Select relevant orbital elements for clustering
    features = ['sma', 'ecc', 'inc', 'raan', 'arg_perigee']
    df_cluster = df[features].dropna().copy()  # Remove missing values

    # Normalize features
    scaler = StandardScaler()
    df_cluster_scaled = scaler.fit_transform(df_cluster)

    # Apply DBSCAN clustering
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='euclidean')
    df_cluster['cluster'] = dbscan.fit_predict(df_cluster_scaled)

    # Merge back area_mass_ratio for visualization
    df_cluster = df_cluster.merge(df[['area_mass_ratio']], left_index=True, right_index=True)

    # Assign collision risk levels based on cluster density
    cluster_counts = df_cluster['cluster'].value_counts()
    df_cluster['risk_score'] = df_cluster['cluster'].map(lambda x: cluster_counts.get(x, 0))
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(df_cluster_scaled, df_cluster['cluster'])

    return df_cluster, silhouette_avg



