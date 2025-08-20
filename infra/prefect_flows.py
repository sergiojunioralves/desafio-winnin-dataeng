from prefect import flow, task
import subprocess

@task
def run_notebook(path: str):
    """
    Executa notebooks Databricks localmente ou via API.
    """
    print(f"Executando notebook: {path}")
    # Simulação: chamar `databricks-cli` ou rodar local
    subprocess.run(["python", path], check=True)

@flow(name="pipeline_creators_posts")
def pipeline():
    run_notebook("notebooks/1 - create_table_creators_scrape_wiki.py")
    run_notebook("notebooks/2 - create_table_posts_creator.py")
    run_notebook("notebooks/3 - create_table_user_yt_from_wikipedia_api.py")
    run_notebook("notebooks/4 - analyze_creators.py")
    run_notebook("notebooks/5 - platinum_features.py")
    run_notebook("notebooks/6 - data_quality_checks.py")

if __name__ == "__main__":
    pipeline()
