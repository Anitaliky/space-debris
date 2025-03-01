import matplotlib.pyplot as plt
import seaborn as sns

# def plot_debris_by_satellite(df_debris):
#     """
#     Example: group debris by sat_id and visualize inclination distribution (box plot).
#     """
#     if 'sat_id' not in df_debris.columns:
#         print("No sat_id column in DataFrame. Skipping plot.")
#         return

#     plt.figure(figsize=(9, 5))
#     sns.boxplot(x='sat_id', y='inc', data=df_debris, palette='Set3')
#     plt.title("Inclination by Satellite of Origin")
#     plt.xlabel("Satellite ID")
#     plt.ylabel("Inclination (deg)")
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()

# Function to visualize clusters using a scatter plot
def plot_clusters_2D(df):
    """
    Plots debris clusters in 2D space (Area-to-Mass Ratio vs. Semimajor Axis).
    
    Args:
        df (DataFrame): Clustered dataset with 'area_mass_ratio' and 'sma'.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='area_mass_ratio', y='sma', hue='cluster', palette='viridis', alpha=0.7)
    plt.title("Debris Clustering Based on Area-to-Mass Ratio and Semimajor Axis")
    plt.xlabel("Area-to-Mass Ratio")
    plt.ylabel("Semimajor Axis (km)")
    plt.legend(title="Cluster")
    plt.grid()
    plt.show()

# Function to visualize clusters using pairplot
def plot_clusters_pairplot(df):
    """
    Creates a pairplot to show the distribution of clusters across multiple features.
    
    Args:
        df (DataFrame): Clustered dataset.
    """
    sns.pairplot(df, hue="cluster", palette="viridis", diag_kind="kde")
    plt.suptitle("Pairplot of Orbital Features by Cluster", y=1.02)
    plt.savefig('plots/Pairplot of Orbital Features by Cluster.jpg')
    plt.show()

# Function to visualize clusters in 3D space
def plot_collision_risk_3D(df):
    """
    Creates a 3D scatter plot to visualize debris clusters based on orbital elements.

    Args:
        df (DataFrame): Clustered dataset with orbital parameters.
    """
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')

    # Scale bubble size for visualization (avoid overly large/small bubbles)
    bubble_size = df['area_mass_ratio']  # Adjust scaling factor as needed

    scatter = ax.scatter(df['raan'], df['inc'], df['sma'], c=df['cluster'], s=bubble_size, cmap='coolwarm', alpha=0.7)
    ax.set_xlabel("RAAN (deg)")
    ax.set_ylabel("Inclination (deg)")
    ax.set_zlabel("Semimajor Axis (km)")
    ax.set_title("3D Collision Risk Visualization")

    plt.colorbar(scatter, ax=ax, label="Cluster")
    plt.savefig('plots/3D Collision Risk Visualization.jpg')
    plt.show()