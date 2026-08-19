import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("your_file.csv")

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())


# ==========================================
# 2. CHECK DATA
# ==========================================

print("\n========== DATASET INFORMATION ==========")

print("Number of relationships:", len(df))
print("Columns:", df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())


# ==========================================
# 3. CREATE THE GRAPH
# ==========================================

G = nx.from_pandas_edgelist(
    df,
    source="Source",
    target="Target"
)

print("\nGraph created successfully!")


# ==========================================
# 4. GRAPH INFORMATION
# ==========================================

print("\n========== GRAPH INFORMATION ==========")

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

print("Is directed?:", G.is_directed())

print(
    "Number of connected components:",
    nx.number_connected_components(G)
)


# ==========================================
# 5. NETWORK STATISTICS
# ==========================================

degrees = dict(G.degree())

average_degree = sum(degrees.values()) / G.number_of_nodes()

print("\n========== NETWORK STATISTICS ==========")

print("Average degree:", average_degree)
print("Maximum degree:", max(degrees.values()))
print("Minimum degree:", min(degrees.values()))
print("Network density:", nx.density(G))


# ==========================================
# 6. FIND MOST CONNECTED NODE
# ==========================================

most_connected = max(degrees, key=degrees.get)

print("\n========== MOST CONNECTED NODE ==========")

print("Node:", most_connected)
print("Connections:", degrees[most_connected])


# ==========================================
# 7. CREATE GRAPH LAYOUT
# ==========================================

print("\nCreating global network graph...")

pos = nx.spring_layout(
    G,
    seed=42
)


# ==========================================
# 8. DRAW GRAPH
# ==========================================

plt.figure(figsize=(14, 10))

# Draw nodes
nx.draw_networkx_nodes(
    G,
    pos,
    node_size=300,
    alpha=0.8
)

# Draw edges
nx.draw_networkx_edges(
    G,
    pos,
    width=1,
    alpha=0.5
)

# Add node labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=8
)

plt.title(
    "Global Social Network Graph",
    fontsize=18
)

plt.axis("off")

plt.tight_layout()

plt.show()