import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(df_debris):
    """
    Conduct basic exploratory data analysis: descriptive stats, distribution plots, correlation heatmap.
    """
    print("\n=== EDA: Descriptive Statistics ===")
    print(df_debris.describe())

    # Distribution: Semimajor axis
    plt.figure(figsize=(7, 5))
    sns.histplot(df_debris['sma'], kde=True, bins=20, color='blue')
    plt.title("Distribution of Semimajor Axis (km)")
    plt.xlabel("Semimajor Axis (km)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # Distribution: Inclination
    plt.figure(figsize=(7, 5))
    sns.histplot(df_debris['inc'], kde=True, bins=20, color='green')
    plt.title("Distribution of Inclination (deg)")
    plt.xlabel("Inclination (deg)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

    # Correlation Heatmap
    numeric_cols = ['sma', 'ecc', 'inc', 'mean_anomaly', 'arg_perigee', 'raan', 'area_mass_ratio']
    corr_matrix = df_debris[numeric_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()
