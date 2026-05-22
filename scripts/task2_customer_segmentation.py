# ======================================================
# TASK 2 - ADVANCED CUSTOMER SEGMENTATION PROJECT
# ======================================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA


# =========================
# LOAD DATASET
# =========================

df = pd.read_csv("../data/Mall_Customers.csv")


# =========================
# DISPLAY DATA
# =========================

print("\nFIRST 5 ROWS")
print(df.head())

print("\nDATASET INFO")
print(df.info())

print("\nMISSING VALUES")
print(df.isnull().sum())


# =========================
# DATA PREPROCESSING
# =========================

# Convert Gender into Numeric

df['Gender'] = df['Gender'].map({
    'Male': 0,
    'Female': 1
})


# =========================
# FEATURE SELECTION
# =========================

X = df[['Age',
        'Annual Income (k$)',
        'Spending Score (1-100)']]


# =========================
# FEATURE SCALING
# =========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)


# =========================
# ELBOW METHOD
# =========================

wcss = []

for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)


# =========================
# PLOT ELBOW GRAPH
# =========================

plt.figure(figsize=(8,5))

plt.plot(range(1,11),
         wcss,
         marker='o',
         linewidth=2)

plt.title("Elbow Method")

plt.xlabel("Number of Clusters")

plt.ylabel("WCSS")

plt.grid(True)

plt.savefig("../outputs/elbow_method.png")

plt.show()


# =========================
# APPLY KMEANS
# =========================

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

df['Cluster'] = clusters


# =========================
# SILHOUETTE SCORE
# =========================

score = silhouette_score(X_scaled, clusters)

print("\nSILHOUETTE SCORE")

print(score)


# =========================
# CLUSTER ANALYSIS
# =========================

print("\nCLUSTER ANALYSIS")

cluster_analysis = df.groupby('Cluster').mean()

print(cluster_analysis)


# =========================
# SAVE CLUSTER ANALYSIS
# =========================

cluster_analysis.to_csv(
    "../outputs/cluster_analysis.csv"
)


# =========================
# CUSTOMER SEGMENTS VISUALIZATION
# =========================

plt.figure(figsize=(10,6))

sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    hue='Cluster',
    palette='Set1',
    data=df,
    s=120
)

plt.title("Customer Segmentation Analysis")

plt.xlabel("Annual Income")

plt.ylabel("Spending Score")

plt.legend(title="Cluster")

plt.grid(True)

plt.savefig("../outputs/customer_segments.png")

plt.show()


# =========================
# AGE DISTRIBUTION
# =========================

plt.figure(figsize=(8,5))

sns.histplot(
    df['Age'],
    bins=10,
    kde=True
)

plt.title("Age Distribution")

plt.xlabel("Age")

plt.ylabel("Count")

plt.grid(True)

plt.savefig("../outputs/age_distribution.png")

plt.show()


# =========================
# INCOME VS SPENDING
# =========================

plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Annual Income (k$)',
    y='Spending Score (1-100)',
    data=df,
    hue='Cluster',
    palette='Set2',
    s=100
)

plt.title("Income vs Spending Score")

plt.grid(True)

plt.savefig("../outputs/income_vs_spending.png")

plt.show()


# =========================
# PCA VISUALIZATION
# =========================

pca = PCA(n_components=2)

pca_components = pca.fit_transform(X_scaled)

df['PCA1'] = pca_components[:,0]

df['PCA2'] = pca_components[:,1]


plt.figure(figsize=(10,6))

sns.scatterplot(
    x='PCA1',
    y='PCA2',
    hue='Cluster',
    palette='tab10',
    data=df,
    s=120
)

plt.title("PCA Visualization of Customer Segments")

plt.grid(True)

plt.savefig("../outputs/pca_visualization.png")

plt.show()


# =========================
# SAVE FINAL OUTPUT
# =========================

df.to_csv(
    "../outputs/customer_segments_output.csv",
    index=False
)


# =========================
# FINAL MESSAGE
# =========================

print("\nPROJECT COMPLETED SUCCESSFULLY!")

print("\nFILES GENERATED INSIDE OUTPUTS FOLDER")