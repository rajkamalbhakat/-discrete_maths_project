import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

CSV_PATH = "soc-karate.csv"
OUTPUT_IMAGE = "karate_graph.png"


def load_graph(csv_path: str) -> nx.Graph:
    """Loading into undirected graph"""
    df = pd.read_csv(csv_path)

    required_cols = {"Source", "Target"}
    if not required_cols.issubset(df.columns):
        raise ValueError(
            f"CSV must contain columns {required_cols}, found {set(df.columns)}"
        )

    # data cleaning check once
    before = len(df)
    df = df.drop_duplicates()
    df = df[df["Source"] != df["Target"]]
    dropped = before - len(df)
    if dropped:
        print(f"Dropped {dropped} duplicate/self-loop rows during cleaning.")

    G = nx.from_pandas_edgelist(df, "Source", "Target")
    return G


def print_network_statistics(G: nx.Graph) -> None:
    """Print the core Module 1 network statistics."""
    print("=== Network Statistics ===")
    print(f"Graph order (nodes): {G.number_of_nodes()}")
    print(f"Graph size (edges):  {G.number_of_edges()}")
    print(f"Directed:            {G.is_directed()}")
    print(f"Connected:           {nx.is_connected(G)}")

    if not nx.is_connected(G):
        n_components = nx.number_connected_components(G)
        print(f"Connected components: {n_components}")

    degrees = dict(G.degree())
    avg_degree = sum(degrees.values()) / G.number_of_nodes()
    max_node = max(degrees, key=degrees.get)
    min_node = min(degrees, key=degrees.get)

    print(f"Average degree:      {avg_degree:.2f}")
    print(f"Max degree node:     {max_node} (degree={degrees[max_node]})")
    print(f"Min degree node:     {min_node} (degree={degrees[min_node]})")
    density = nx.density(G)
    print(f"Density:             {density:.4f}")
    print("===========================")


def draw_graph(G: nx.Graph, output_path: str) -> None:
    """Draw and save the graph with a fixed layout for reproducibility."""
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)  # deterministic layout for before/after comparisons

    degrees = dict(G.degree())
    node_sizes = [300 + 60 * degrees[n] for n in G.nodes()]  # size reflects influence

    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=node_sizes)
    nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.6)
    nx.draw_networkx_labels(G, pos, font_size=9, font_family="sans-serif")

    plt.title("Zachary's Karate Club Network")
    plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Graph saved to {output_path}")


def main():
    try:
        G = load_graph(CSV_PATH)
    except FileNotFoundError:
        print(f"Error: '{CSV_PATH}' not found. Check the file path.", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print_network_statistics(G)
    draw_graph(G, OUTPUT_IMAGE)

    return G  # hfor other users to use 


if __name__ == "__main__":
    main()