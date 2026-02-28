import os
import ast
import json

def analyze_repo(path):
    dependency_map = {}

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, path)

                dependency_map[relative_path] = []

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read())

                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                dependency_map[relative_path].append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            if node.module:
                                dependency_map[relative_path].append(node.module)

                except Exception:
                    pass

    return dependency_map


def export_graph(data, output="dependency_graph.json"):
    with open(output, "w") as f:
        json.dump(data, f, indent=2)
