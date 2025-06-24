# from embedder import index_chunks
# from qa import answer_query
from makeREADME import generate_readme
from summarizer import summarize_function
from repo_parser import parse_repo
import argparse

def main():
    parser = argparse.ArgumentParser(description="Parse Python files in a repository.")
    parser.add_argument("repo_path", type=str, help="Path to the repository")
    args = parser.parse_args()
    print(args)
    functions, imports = parse_repo(args.repo_path)
    # for func in functions:
    #     print(f"File: {func['file']}")
    #     print(f"Function: {func['name']}, Docstring: {func['docstring']}, Start Line: {func['start_line']}")
    #     print(func['code'])
    #     print("-" * 40)
    for func in functions:
        func['docstring'] = summarize_function(func['code'])
    chunks_by_file = {}
    for func in functions:
        if func['file'] not in chunks_by_file:
            chunks_by_file[func['file']] = []
        chunks_by_file[func['file']].append(func)
    
    # print(chunks_by_file)
    readme_content = generate_readme(chunks_by_file, imports=imports, project_name=args.repo_path.split("/")[-1])
    readme_path = f"{args.repo_path}/README.md"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"README generated at {readme_path}")

if __name__ == "__main__":
    main()
