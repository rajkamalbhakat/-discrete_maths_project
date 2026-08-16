# Graph-Based Social Network Analysis and Influence Ranking Using Graph Theory and Linear Algebra

## 📌 Project Overview

This project develops a mathematical and computational system for analyzing a real-world social network using **Graph Theory and Linear Algebra**.

The system uses the **Zachary Karate Club dataset** and represents social relationships mathematically as a graph:

[
G = (V,E)
]

where:

* (V) represents the set of users/nodes.
* (E) represents the set of relationships/edges.

The project analyzes the network to determine influential users, identify communities, calculate shortest paths, study matrix representations, and examine how changes in network structure affect the results.

## 🎯 Main Objective

To develop a mathematical and computational system that analyzes a social network using Graph Theory and Linear Algebra and ranks users according to their structural influence within the network.

## 📊 Dataset

### Zachary's Karate Club Dataset

The primary dataset represents social relationships among members of a university karate club.

* **Nodes:** 34
* **Edges:** 78
* **Graph:** Undirected
* **Connections:** Unweighted

## 🔄 Project Workflow

```text
Real Dataset
     ↓
Data Collection
     ↓
Data Cleaning & Preprocessing
     ↓
Graph Construction G = (V,E)
     ↓
Network Statistics
     ↓
 ┌───────────────────┐
 │                   │
 ↓                   ↓
Graph Theory     Linear Algebra
 │                   │
 ├─ BFS/DFS          ├─ Adjacency Matrix
 ├─ Shortest Path    ├─ Degree Matrix
 ├─ Connectivity     ├─ Laplacian Matrix
 └─ Communities      ├─ Eigenvalues
                     └─ Eigenvectors
 │                   │
 └─────────┬─────────┘
           ↓
   Centrality Analysis
           ↓
   Degree Centrality
           ↓
   Betweenness Centrality
           ↓
   Eigenvector Centrality
           ↓
        PageRank
           ↓
    Influence Score
           ↓
      User Ranking
           ↓
   Community Detection
           ↓
Interactive Visualization
           ↓
    What-If Analysis
           ↓
  Before/After Comparison
           ↓
      Final Conclusion
```

The overall project follows the pipeline:

**Real Social Network Data → Graph Theory → Linear Algebra → Centrality/PageRank → Influence Ranking → Communities → Visualization → What-If Analysis.**

## 👥 Team Members

| Member   | Name          | Main Responsibility                    |
| -------- | ------------- | -------------------------------------- |
| Member 1 | **Vinayak**   | Data Processing & Graph Modeling       |
| Member 2 | **Faraz**     | Linear Algebra & Spectral Analysis     |
| Member 3 | **Raj Kamal** | Centrality & Influence Ranking         |
| Member 4 | **Sanika**    | Graph Algorithms & Community Detection |
| Member 5 | **Anannya**   | Visualization & Network Simulation     |

## 🔢 Module 1 — Data Processing & Graph Modeling

**Responsible Member: Vinayak**

This module forms the foundation of the project.

Main responsibilities:

* Dataset collection
* Dataset understanding
* Data cleaning
* Data preprocessing
* Handling duplicate and invalid data
* Creating nodes and edges
* Graph construction
* Graph representation
* Network statistics

Mathematical concepts include:

* Vertices
* Edges
* Degree
* Graph order
* Graph size
* Directed/undirected graphs
* Weighted/unweighted graphs

## 📐 Module 2 — Linear Algebra & Spectral Analysis

**Responsible Member: Faraz**

Main components:

### Adjacency Matrix

[
A=[a_{ij}]
]

### Degree Matrix

A diagonal matrix containing the degree of every node.

### Graph Laplacian

[
L=D-A
]

### Eigenvalues and Eigenvectors

[
Ax=\lambda x
]

This module provides the project's primary Linear Algebra component.

## ⭐ Module 3 — Centrality & Influence Ranking

**Responsible Member: Raj Kamal**

This module determines which users are important or influential in the network.

### Degree Centrality

[
C_D(v)=\frac{deg(v)}{n-1}
]

### Betweenness Centrality

[
C_B(v)=
\sum_{s\neq v\neq t}
\frac{\sigma_{st}(v)}
{\sigma_{st}}
]

### Eigenvector Centrality

Eigenvector centrality is based on the principle that a user is important when they are connected to other important users.

[
Ax=\lambda x
]

### PageRank

PageRank considers the importance of incoming connections.

### Overall Influence Score

The project combines normalized centrality measures:

[
I=w_1D+w_2B+w_3E+w_4P
]

The weights will be configurable and justified rather than treated as universally correct.

## 🌐 Module 4 — Graph Algorithms & Community Detection

**Responsible Member: Sanika**

Main components:

* BFS
* DFS
* Shortest paths
* Connected components
* Community detection
* Louvain
* Label Propagation

The module identifies groups of densely connected users and studies connectivity within the network.

## 📊 Module 5 — Visualization & Network Simulation

**Responsible Member: Anannya**

This module converts the mathematical analysis into an interactive application.

The dashboard will include:

* Network overview
* Interactive graph
* Matrix analysis
* Influence ranking
* Path and community analysis
* What-If simulation

The What-If simulator will allow users to:

* Add a node
* Remove a node
* Add an edge
* Remove an edge

The system will then recalculate the network analysis and provide a before/after comparison.

## 🛠️ Technology Stack

The recommended technology stack is:

```text
Python
│
├── Pandas       → Dataset Processing
├── NetworkX     → Graph Processing & Algorithms
├── NumPy        → Matrices & Eigenvalues
├── Plotly       → Interactive Visualization
└── Streamlit    → Interactive Dashboard
```

## 📁 Project Structure

```text
discrete-maths-project/
│
├── README.md
│
├── data/
│
├── docs/
│
├── src/
│
├── notebooks/
│
├── results/
│
└── tests/
```

This structure will be expanded as development progresses.

## 🚀 Expected Outcome

The final system will transform social-network data into a mathematical graph, perform Graph Theory and Linear Algebra analysis, calculate centrality and PageRank measures, rank influential users, identify communities, find shortest paths, visualize the network, and demonstrate the effect of network changes through What-If simulation.

## 👨‍💻 Development

This repository will contain:

* Source code
* Dataset and processed data
* Mathematical analysis
* Jupyter notebooks
* Visualizations
* Results
* Project documentation
* Final report

All project development will be version-controlled using **Git and GitHub**.
