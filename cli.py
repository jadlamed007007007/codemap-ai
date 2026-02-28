import sys
from analyzer import analyze_repo, export_graph
from explainer import explain_file

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python cli.py analyze <path>")
        print("  python cli.py explain <file>")
        return

    command = sys.argv[1]

    if command == "analyze":
        path = sys.argv[2] if len(sys.argv) > 2 else "."
        data = analyze_repo(path)
        export_graph(data)
        print("Dependency graph saved.")

    elif command == "explain":
        file = sys.argv[2]
        explanation = explain_file(file)
        print(explanation)

if __name__ == "__main__":
    main()
