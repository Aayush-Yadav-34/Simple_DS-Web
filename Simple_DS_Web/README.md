# Data Structures Visualizer (Python Flask)

This project is a web-based application for visualizing and interacting with various fundamental data structures and algorithms. Built using Python and Flask, it provides educational tools and visualizations for students and enthusiasts to better understand how data structures work.

## Features

- **Binary Tree Visualization**
- **Linked List & Doubly Linked List**
- **Stack & Queue**
- **Priority Queue**
- **Hash Tables** (with and without collision handling, chaining)
- **Graph Traversals** (BFS & DFS)
- **Huffman Coding**
- **Travelling Salesman Problem (TSP)**

Each data structure or algorithm has its own dedicated page with interactive features and visual outputs.

## Modern UI/UX

- All data structure and algorithm pages (except the home page) use a modern, card-based, responsive layout for a unified look and feel.
- Each page includes a clear description and user instructions at the top, making it easy to understand how to interact with the visualizer.
- Both inline CSS (for layout and cards) and an external stylesheet (`style.css`) are used for styling. The external CSS file is included in all templates for easy customization.
- Flask output (such as results and messages) is highlighted using the `.flask-output` CSS class for better visibility.

## Project Structure

```
app.py                              # Main Flask application
binary_tree_logic.py                # Binary tree logic and visualization
double_linked_list_logic.py         # Doubly linked list logic
graph_bfs_logic.py                  # Graph BFS traversal logic
graph_dfs_logic.py                  # Graph DFS traversal logic
hash_table_logic.py                 # Hash table logic (basic)
hash_table_chaining_logic.py        # Hash table with chaining
hash_table_no_collision_logic.py    # Hash table without collision handling
huffman_coding_logic.py             # Huffman coding algorithm
linked_list_logic.py                # Singly linked list logic
priority_queue_logic.py             # Priority queue logic
queue_logic.py                      # Queue logic
stack_logic.py                      # Stack logic
tsp_logic.py                        # Travelling Salesman Problem logic
static/
    style.css                      # CSS styles (included in all templates)
    binary_tree_plot.png           # Example output image
templates/
    binary_tree_app.html           # Binary tree page
    doubly_linked_list_app.html    # Doubly linked list page
    graph_bfs_app.html             # Graph BFS page
    graph_dfs_app.html             # Graph DFS page
    hash_table_app.html            # Hash table page
    hash_table_chaining_app.html   # Hash table with chaining page
    hash_table_no_collision_app.html # Hash table without collision page
    huffman_app.html               # Huffman coding page
    index.html                     # Home page (not card-based)
    linked_list_app.html           # Linked list page
    priority_queue_app.html        # Priority queue page
    queue_app.html                 # Queue page
    stack_app.html                 # Stack page
    tsp_app.html                   # TSP page
    Data-Structure.jpg             # Image asset
```

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- graphviz
- (Optional) matplotlib, networkx, or other libraries for visualization

### Installation
1. Clone the repository:
   ```powershell
   git clone <repo-url>
   cd "Project (Website) ver2"
   ```
2. Install dependencies:
   ```powershell
   pip install flask
   pip install graphviz
   pip install matplotlib networkx  # If required by visualizations
   ```
   - You may also need to install Graphviz system binaries from https://graphviz.gitlab.io/download/ for full functionality.

### Running the App
```powershell
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Usage
- Navigate to the home page and select a data structure or algorithm.
- Each page (except the home page) provides a description and instructions for entering data.
- Interact with the forms to add, remove, or manipulate data.
- Visualizations and results will be displayed on each page, with Flask output highlighted for clarity.

## Screenshots


## License
This project is for educational purposes. Add a license if you intend to share or distribute.

## Credits
Developed by Aayush Yadav.

---
Feel free to contribute or suggest improvements!
