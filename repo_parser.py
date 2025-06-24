import ast, os

def extract_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()

    imports = set()
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name.split('.')[0])  # Just the root package
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.add(node.module.split('.')[0])
    except Exception as e:
        print(f"Failed to parse {file_path} for imports: {e}")
    return imports


def parse_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    tree = ast.parse(code)
    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            docstring = ast.get_docstring(node)
            functions.append({
                "file": file_path,
                "name": node.name,
                "docstring": docstring,
                "start_line": node.lineno,
                "code": ast.get_source_segment(code, node)
            })
    return functions

def parse_repo(repo_path):
    parsed = []
    all_imports = set()
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    parsed += parse_python_file(file_path)
                    all_imports |= extract_imports(file_path)  # Merge sets
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
    return parsed, sorted(all_imports)

# def main():
#     import argparse
#     parser = argparse.ArgumentParser(description="Parse Python files in a repository.")
#     parser.add_argument("repo_path", type=str, help="Path to the repository")
#     args = parser.parse_args()
    
#     functions = parse_repo(args.repo_path)
#     for func in functions:
#         print(f"File: {func['file']}")
#         print(f"Function: {func['name']}, Docstring: {func['docstring']}, Start Line: {func['start_line']}")
#         print(func['code'])
#         print("-" * 40)
#     # print(functions)
