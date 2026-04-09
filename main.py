import subprocess

def run_notebook(path):
    subprocess.run(["jupyter", "nbconvert", "--to", "html", "--execute", path, "--allow-errors"], check=True)

if __name__ == "__main__":
    print("Running DCE-KG pipeline...")
    run_notebook("notebooks/1_pmc_download.ipynb")
    run_notebook("notebooks/2_ner_linking.ipynb")
    run_notebook("notebooks/3_relation_extraction.ipynb")
    run_notebook("notebooks/4_neo4j_upload.ipynb")
    run_notebook("notebooks/5_validation.ipynb")
    print("Pipeline finished. Check data/processed/ and Neo4j.")